#!/usr/bin/python
from Bio import SeqIO

record_id ="NODE_58_length_183348_cov_19.5163"

start=0
end=800

fasta_file="/home/anna/bioinformatics/novymonas/novymonas_no_pand_scaffolds.fasta"

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        # result = record
        result = record[start:end]#.reverse_complement()
        result.description=""
        break


outpath = '/home/anna/bioinformatics/novymonas/U6_novymonas_full_flangs.fna'

SeqIO.write(result, outpath, "fasta")
