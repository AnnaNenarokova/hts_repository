#!python3
from Bio import SeqIO
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"

def add_diamond_dict(diamond_path, outfmt_opts, seq_dict, ncbi=False, delimeter="\t"):
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

def write_seqs(seq_dict, qfasta_path, refset_fasta_path, outdir):
    q_seqs = {}
    for record in SeqIO.parse(qfasta_path, "fasta"):
        q_seqs[record.id] = record

    refset_seqs = {}
    for record in SeqIO.parse(refset_fasta_path, "fasta"):
        refset_seqs[record.id] = record

    for qseqid in seq_dict:
        print (qseqid)
        outpath = outdir + qseqid + ".faa"
        out_records = [q_seqs[qseqid]]
        for refset_id in seq_dict[qseqid]["refset"]:
            out_records.append(refset_seqs[refset_id])
        SeqIO.write(out_records, outpath, "fasta")
        with open(outpath, "a") as outfile:
            ncbi_ids_string = ""
            for ncbi_id in seq_dict[qseqid]["ncbi"]:
                ncbi_ids_string = ncbi_ids_string + ncbi_id + ","
            ncbi_records = Entrez.efetch(db="protein", id=ncbi_ids_string, rettype="fasta").read()[:-1]
            outfile.write(ncbi_records)

diamond_refset="/projects/Diplonema_genome_evolution/hgt/results/hgt_refset_diamond.tsv"
outfmt_opts_refset="qseqid qlen sseqid slen length evalue bitscore"

diamond_ncbi="/home/users/nenarokova/diplonema/hgt_new/diamond_results/dpapi_nr_dmnd.tsv"
outfmt_opts_ncbi="qseqid qlen sseqid slen length evalue bitscore"

qfasta_path="/projects/Diplonema_genome_evolution/hgt/dpapi_hgt_candidates.faa"
refset_fasta_path="/projects/Diplonema_genome_evolution/refdataset_diplonema/no_dpapi_refdataset.faa"

outdir="/projects/Diplonema_genome_evolution/hgt/results/fasta/"

seq_dict = {}

seq_dict = add_diamond_dict(diamond_refset, outfmt_opts_refset, seq_dict)
seq_dict = add_diamond_dict(diamond_ncbi, outfmt_opts_ncbi, seq_dict, ncbi=True)

write_seqs(seq_dict, qfasta_path, refset_fasta_path, outdir)
