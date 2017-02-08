#!/usr/bin/python
from Bio import SeqIO
cds="/home/anna/Dropbox/PhD/bioinformatics/trypanosomatids/blasto/transcriptome/Trinity-GG_p57_6_frames_translat_bl_report_best_exact_end_>30_4.fna"

stops = {
'TGA' : 0,
'TAG' : 0,
'TAA' : 0,
'other' : 0
}

non_stops = {
'TGA' : 0,
'TAG' : 0,
'TAA' : 0
}

for record in SeqIO.parse(cds, "fasta"):
    seq=record.seq
    for i in range(0,len(seq)-4,3):
        frame=str(seq[i:i+3])
        if frame in non_stops.keys():
            non_stops[frame] += 1
    stop=str(seq[-4:-1])
    if stop in stops.keys():
        stops[stop] += 1
    else:
        stops['other'] += 1

for key in non_stops.keys():
    print key, non_stops[key], stops[key]

