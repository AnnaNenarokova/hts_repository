#!/usr/bin/python
from Bio import SeqIO

record_id = []
start = 1408
end = 1719
fasta_file = '/home/anna/Dropbox/phd/bioinformatics/kinetoplastids/CLC_assemblies/Angomonas_ambiguus_HiSeqMiSeq_assembly.fa'

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        result = record[start:end]

outpath = '/home/anna/Dropbox/phd/bioinformatics/kinetoplastids/CLC_assemblies/genes/Angomonas_ambiguus_SSU.fst'

SeqIO.write(result, outpath, "fasta")
