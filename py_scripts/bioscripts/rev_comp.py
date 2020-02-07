#!/usr/bin/python
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

fasta_path = "/home/anna/bioinformatics/blasto_local/ambar/trp-tRNA/Order_11106670028-1_Results/fasta/clipped/reverse.fasta"
outpath = "/home/anna/bioinformatics/blasto_local/ambar/trp-tRNA/Order_11106670028-1_Results/fasta/clipped/reverse_reversed.fasta"
results = []
for record in SeqIO.parse(fasta_path, "fasta"):
    reversed_seq = record.seq.reverse_complement()
    record_output = SeqRecord(reversed_seq,
        id=record.id, name=record.name,
        description=record.description)
    results.append(record_output)
SeqIO.write(results, open(outpath, 'w'), "fasta")
