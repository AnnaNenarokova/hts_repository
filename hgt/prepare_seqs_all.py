#!python3
from Bio import SeqIO
from Bio import Entrez


diamond_refdataset="/projects/Diplonema_genome_evolution/hgt/results/dpapi_hgt_cand_diamond_dpapi_refdataset.tsv"
outfmt_opts_ref="qseqid qlen sseqid slen length evalue bitscore"

diamond_nr="/projects/Diplonema_genome_evolution/hgt/hgt_nr_diamond.tsv"
outfmt_opts_nr="qseqid qlen sseqid slen staxids length evalue bitscore"

infasta_path = "/projects/Diplonema_genome_evolution/hgt/dpapi_hgt_candidates.faa"
ref_fasta_path = "/projects/Diplonema_genome_evolution/refdataset_diplonema/dpapi_refdataset.faa"

outdir="/projects/Diplonema_genome_evolution/hgt/results/fasta/"

dpapi_seqs = {}
for record in SeqIO.parse(infasta_path, "fasta"):
    dpapi_seqs[record.id] = record

outfmt_opt_list = outfmt_opts.split(" ")

results = {}

with open(diamond_result_path) as diamond_f:
    current_qseqid = None
    i = 0
    for line in diamond_f:
        i += 1
        # print (i)
        line_split = line.rstrip().split("\t")
        qseqid = line_split[outfmt_opt_list.index("qseqid")]
        sseqid = line_split[outfmt_opt_list.index("sseqid")]
        evalue = float(line_split[outfmt_opt_list.index("evalue")])
        if qseqid != current_qseqid:
            print (current_qseqid)
            if current_qseqid:
                SeqIO.write(records, current_path, "fasta")
            current_qseqid = qseqid
            current_path = outdir + current_qseqid + ".faa"
            records = [dpapi_seqs[qseqid]]
            print (current_path)
        ref_record = ref_seqs[sseqid]
        records.append(ref_record)

outfmt_opt_list = outfmt_opts.split(" ")

dpapi_seqs = {}
for record in SeqIO.parse(infasta_path, "fasta"):
    dpapi_seqs[record.id] = record

with open(diamond_result_path) as diamond_f:
    current_qseqid = None
    current_f = None
    i = 0
    for line in diamond_f:
        i += 1
        print (i)
        line_split = line.rstrip().split("\t")
        qseqid = line_split[outfmt_opt_list.index("qseqid")]
        sseqid = line_split[outfmt_opt_list.index("sseqid")]
        taxid = line_split[outfmt_opt_list.index("staxids")]
        evalue = float(line_split[outfmt_opt_list.index("evalue")])
        
        print (current_qseqid)


        if qseqid != current_qseqid:
            if current_f: current_f.close()
            current_qseqid = qseqid
            current_path = outdir + current_qseqid + ".faa"
            dpapi_record = [dpapi_seqs[qseqid]]
            SeqIO.write(dpapi_record, current_path, "fasta")
            current_f = open(current_path, "a")
            print (current_path)
        ncbi_record = Entrez.efetch(db="protein", id=sseqid, rettype="fasta").read()[:-1]
        current_f.write(ncbi_record)
    current_f.close()