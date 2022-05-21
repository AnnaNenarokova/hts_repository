#!/usr/bin/python
from Bio import SeqIO
cds="/home/anna/Dropbox/PhD/bioinformatics/trypanosomatids/blasto/transcriptome/Trinity-GG_p57_6_frames_translat/blast_reports/mitochondrial_riboso_bl_report_best_4.fna"

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
total_len = 0
n_seqs = 0
for record in SeqIO.parse(cds, "fasta"):
    n_seqs += 1
    seq=record.seq
    total_len += len(seq)/3
    for i in range(0,len(seq)-4,3):
        frame=str(seq[i:i+3])
        if frame in non_stops.keys():
            non_stops[frame] += 1
    stop=str(seq[-3:])
    if stop in stops.keys():
        stops[stop] += 1
    else:
        stops['other'] += 1

print "number of seqs", n_seqs
print "total length", total_len
for key in non_stops.keys():
    print key, non_stops[key], non_stops[key]/float(total_len), stops[key]

