#!/usr/bin/python
from Bio import SeqIO

# record_id = 'NODE_399_length_12721_cov_299.805'
# record_id = "NODE_480_length_8410_cov_643.285"
# record_id = "NODE_368_length_15062_cov_139.327"
record_id ="NODE_399_length_12721_cov_299.805"

start=4989
end=5201
# fasta_file = '/media/anna/data/Dropbox/PhD/projects/blasto/blastocrithidia/genome/assembly/triat_DNA_scaffolds.fa'
fasta_file = '/home/anna/bioinformatics/blasto/p57_DNA_scaffolds.fa'

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        result = record
        result = record[start:end].reverse_complement()
        result.id="rRNA_M1_220"
        result.description=""
        break


outpath = '/home/anna/bioinformatics/blasto/P57_rRNA_M1_220.fa'

SeqIO.write(result, outpath, "fasta")
