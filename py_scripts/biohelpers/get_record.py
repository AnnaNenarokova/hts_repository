#!/usr/bin/python3
from Bio import SeqIO

record_id ="Ctg32_length_42107"

start=299
end=470

fasta_file="/Users/annanenarokova/work/blasto_local/p57_ra_polished.fa"

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        result = record
        #result = record[start:end]#.reverse_complement()
        result.description=""
        break


outpath = '/Users/annanenarokova/work/blasto_local/p57_ctg32_kinetoplast.fa'

SeqIO.write(result, outpath, "fasta")
