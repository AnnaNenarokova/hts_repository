#!python3
from Bio import SeqIO
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"

diamond_result_path = "/projects/Diplonema_genome_evolution/hgt/hgt_nr_diamond_0e.tsv"
diamond_refset_path = "/projects/Diplonema_genome_evolution/hgt/dpapi_hgt_cand_diamond_euglenozoans.tsv"
infasta_path = "/projects/Diplonema_genome_evolution/hgt/dpapi_hgt_candidates.faa"
outdir="/projects/Diplonema_genome_evolution/hgt/results/fasta/"
outfmt_opts="qseqid qlen sseqid slen staxids length evalue bitscore"

# diamond_result_path = "/projects/Diplonema_genome_evolution/hgt/dpapi_hgt_cand_diamond_euglenozoans.tsv"
# infasta_path = "/projects/Diplonema_genome_evolution/hgt/dpapi_hgt_candidates.faa"
# outdir="/projects/Diplonema_genome_evolution/hgt/results/fasta2/"
# outfmt_opts="qseqid qlen sseqid slen length evalue bitscore"

# diamond_result_path = "/home/vl18625/bioinformatics/diplonema/hgt/hgt_nr_diamond_0e.tsv"
# infasta_path = "/home/vl18625/bioinformatics/diplonema/hgt/dpapi_hgt_candidates.faa"
# outdir="/home/vl18625/bioinformatics/diplonema/hgt/results/fasta/"


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