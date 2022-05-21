#!python3
from Bio import SeqIO
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"

diamond_result_path = "/home/users/nenarokova/myxo/smol_diamond_nr_normal.tsv"

infasta_path = "/home/users/nenarokova/myxo/augustus_6_annot_prot.aa"

outdir="/home/users/nenarokova/myxo/hgt/fasta/"
outfmt_opts="qseqid qlen sseqid slen staxids length evalue bitscore"

outfmt_opt_list = outfmt_opts.split(" ")

query_seqs = {}
for record in SeqIO.parse(infasta_path, "fasta"):
    query_seqs[record.id] = record

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
            query_record = [query_seqs[qseqid]]
            SeqIO.write(query_record, current_path, "fasta")
            current_f = open(current_path, "a")
            print (current_path)
        ncbi_record = Entrez.efetch(db="protein", id=sseqid, rettype="fasta").read()[:-1]
        current_f.write(ncbi_record)
    current_f.close()