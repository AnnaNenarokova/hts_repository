#!/usr/bin/python
from Bio import SeqIO

record_id ="NODE_100_length_23389_cov_103.978"

start=0
end=3000

fasta_file="/Users/annanenarokova/work/blasto_local/jaculum_scaffolds.fa"

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        # result = record
        result = record[start:end]#.reverse_complement()
        result.description=""
        break


outpath = '/Users/annanenarokova/work/blasto_local/cytidine_deaminase/NODE_100_jaculum_first_3000nt.fna'

SeqIO.write(result, outpath, "fasta")
