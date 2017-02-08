#!/usr/bin/python
from Bio import SeqIO
cds="/home/anna/Dropbox/PhD/bioinformatics/trypanosomatids/blasto/transcriptome/all_bh_0_e_format_best_4.fna"

stops = {
'TGAA' : 0,
'TGAG' : 0,
'TGAC' : 0,
'TGAT' : 0,
'TAGA' : 0,
'TAGG' : 0,
'TAGC' : 0,
'TAGT' : 0,
'TAAA' : 0,
'TAAG' : 0,
'TAAC' : 0,
'TAAT' : 0,
'other' : 0
}

non_stops = {
'TGAA' : 0,
'TGAG' : 0,
'TGAC' : 0,
'TGAT' : 0,
'TAGA' : 0,
'TAGG' : 0,
'TAGC' : 0,
'TAGT' : 0,
'TAAA' : 0,
'TAAG' : 0,
'TAAC' : 0,
'TAAT' : 0
}

for record in SeqIO.parse(cds, "fasta"):
    seq=record.seq
    for i in range(0,len(seq)-4,3):
        frame=str(seq[i:i+4])
        if frame in non_stops.keys():
            non_stops[frame] += 1
    stop=str(seq[-4:])
    if stop in stops.keys():
        stops[stop] += 1
    else:
        stops['other'] += 1

for key in non_stops.keys():
    print key, non_stops[key], stops[key]

