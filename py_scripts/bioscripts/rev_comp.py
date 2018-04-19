#!/usr/bin/python
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

fasta_path = "D:/anna_drive/projects/blastocrithidia/blasto/p57_scaffolds.fasta"
outpath = "D:/anna_drive/projects/blastocrithidia/blasto/test_reversed.fasta"
results = []
for record in SeqIO.parse(fasta_path, "fasta"):
    reversed_seq = record.seq.reverse_complement()
    record_output = SeqRecord(reversed_seq,
        id=record.id, name=record.name,
        description=record.description)
    results.append(record_output)
SeqIO.write(results, open(outpath, 'w'), "fasta")
