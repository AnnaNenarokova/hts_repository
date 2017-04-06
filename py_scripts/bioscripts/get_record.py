#!/usr/bin/python
from Bio import SeqIO

# record_id = 'NODE_399_length_12721_cov_299.805'
# record_id = "NODE_480_length_8410_cov_643.285"
record_id = "NODE_368_length_15062_cov_139.327"
start=13156
end=13438
# fasta_file = '/media/anna/data/Dropbox/PhD/projects/blasto/blastocrithidia/genome/assembly/triat_DNA_scaffolds.fa'
fasta_file = '/home/anna/bioinformatics/blasto/p57_DNA_scaffolds.fa'

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        # result = record
        result = record[start:end].reverse_complement()
        result.id="P57_12S_mito"
        result.description=""
        break

outpath = '/home/anna/bioinformatics/blasto/rRNA/P57_12S_mito.fa'

SeqIO.write(result, outpath, "fasta")

