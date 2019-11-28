#!/usr/bin/python
from Bio import SeqIO

record_id ="NODE_239_length_28967_cov_73.6657"

start=0
end=800

fasta_file="/home/anna/bioinformatics/blasto_local/p57_scaffolds.fasta"

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        result = record
        # result = record[start:end]#.reverse_complement()
        result.description=""
        break


outpath = '/home/anna/bioinformatics/NODE_239_p57.fna'

SeqIO.write(result, outpath, "fasta")
