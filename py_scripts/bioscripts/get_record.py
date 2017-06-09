#!/usr/bin/python
from Bio import SeqIO

record_id ="NODE_22_length_26044_cov_154.023"

start=10100
end=11950
fasta_file = '/media/anna/data/Dropbox/PhD/projects/blasto/blastocrithidia/genome/assembly/triat_DNA_scaffolds.fa'
# fasta_file = '/home/anna/bioinformatics/blasto/p57_DNA_scaffolds.fa'

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        result = record
        result = record[start:end].reverse_complement()
        result.id="triatomae_ND5_with_flangs"
        result.description=""
        break


outpath = '/home/anna/bioinformatics/blasto/mito/triatomae_ND5_with_flangs.fa'

SeqIO.write(result, outpath, "fasta")
