#!python3
from Bio import SeqIO
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"

def add_diamond_dict(diamond_path, seq_dict, outfmt_opts=False, ncbi=False, delimeter="\t"):
    if not outfmt_opts:
        outfmt_opts="qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore"
    outfmt_opt_list = outfmt_opts.split(" ")
    with open(diamond_path) as diamond_f:
        for line in diamond_f:
            line_split = line.rstrip().split(delimeter)
            qseqid = line_split[outfmt_opt_list.index("qseqid")]
            sseqid = line_split[outfmt_opt_list.index("sseqid")]
            evalue = float(line_split[outfmt_opt_list.index("evalue")])
            if qseqid not in seq_dict.keys():
                seq_dict[qseqid] = {"ncbi":[], "refset":[]}
            if ncbi:
                seq_dict[qseqid]["ncbi"].append(sseqid)
            else:
                seq_dict[qseqid]["refset"].append(sseqid)
    return seq_dict

def write_seqs(seq_dict, refset_fasta_path, outdir):
    print ("Preparing refset ids")
    refset_ids = []
    for qseqid in seq_dict:
        refset_ids.extend(seq_dict[qseqid]["refset"])
    print ("Loading refset")
    refset_seqs = {}
    i = 0
    for record in SeqIO.parse(refset_fasta_path, "fasta"):
        if i % 100000 == 0:
            print (i)
        i += 1
        record_id = record.id
        if record_id in refset_ids:
            refset_seqs[record_id] = record
    for qseqid in seq_dict:
        print ("Writing down seqs for", qseqid)
        outpath = outdir + qseqid + ".faa"
        out_records = []
        for refset_id in seq_dict[qseqid]["refset"]:
            out_records.append(refset_seqs[refset_id])
        SeqIO.write(out_records, outpath, "fasta")
        with open(outpath, "a") as outfile:
            ncbi_ids_string = ""
            for ncbi_id in seq_dict[qseqid]["ncbi"]:
                ncbi_ids_string = ncbi_ids_string + ncbi_id + ","
            ncbi_records = Entrez.efetch(db="protein", id=ncbi_ids_string, rettype="fasta").read()[:-1]
            outfile.write(ncbi_records)

diamond_ncbi="/Users/annanenarokova/work/dpapi_local/results_21_07/dpapi_recoded_cand_nr_dmnd_tax.tsv"
ncbi_outfmt_opts = "qseqid qlen sseqid slen staxids length evalue bitscore"
diamond_refset="/Users/annanenarokova/work/dpapi_local/results_21_07/dpapi_recoded_cand_refset_dmnd.tsv"
refset_fasta_path="/Users/annanenarokova/work/dpapi_local/dpapi_full_dataset.faa"

outdir="/Users/annanenarokova/work/dpapi_local/results_21_07/fasta"

seq_dict = {}


print ("Adding refset diamond results")
seq_dict = add_diamond_dict(diamond_refset, seq_dict)
print ("Adding ncbi diamond results")
seq_dict = add_diamond_dict(diamond_ncbi, seq_dict, outfmt_opts=ncbi_outfmt_opts, ncbi=True)

write_seqs(seq_dict, refset_fasta_path, outdir)
