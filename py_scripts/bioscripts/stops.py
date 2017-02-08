#!/usr/bin/python
from Bio import SeqIO
cds="/home/anna/Dropbox/PhD/bioinformatics/trypanosomatids/blasto/transcriptome/all_bh_0_e_format_best_4.fna"
uga=0
uag=0
uaa=0
other=0

for record in SeqIO.parse(cds, "fasta"):
    seq=record.seq
    stop=seq[-4:-1]
    if stop == "TGA":
        uga += 1
    elif stop == "TAG":
        uag += 1
    elif stop == "TAA":
        uaa += 1
    else:
        other+=1

print "uga", uga
print "uag", uag
print "uaa", uaa
print "other", other



