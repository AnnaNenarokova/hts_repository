#!/usr/bin/python3
from Bio import SeqIO

record_id="p57_illumina.fa"

start=0
end=689

fasta_file="/Users/anna/work/blasto_local/genomes/ref_genomes/p57_ra_polished.fa"

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        result = record
        #result = record[start:end]#.reverse_complement()
        result.description=""
        break


outpath='/Users/anna/work/blasto_local/genomes/ref_genomes/Ctg28_length_81690.fasta'

SeqIO.write(result, outpath, "fasta")
