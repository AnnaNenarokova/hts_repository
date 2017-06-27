#!/usr/bin/python
from Bio import SeqIO
from Bio.SeqUtils import GC

# fasta="/media/anna/data/Dropbox/PhD/projects/blasto/blastocrithidia/genes/insertions/p57_insertions.fa"
# fasta="/media/anna/data/Dropbox/PhD/projects/blasto/blastocrithidia/genes/rRNA/p57_kinetoplast.fa"
fasta="/media/anna/data/Dropbox/PhD/projects/blasto/blastocrithidia/genes/rRNA/mito_rDNA_trbucei.fasta"
result_seq=""
l=0
for record in SeqIO.parse(fasta, "fasta"):
    result_seq+=record.seq
    l+=len(record.seq)

print GC(result_seq)

print l
