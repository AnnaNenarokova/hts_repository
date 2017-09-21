#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.helpers.parse_csv import *

'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'

blast_csv_path = "/home/anna/bioinformatics/blasto/kinetoplastid_proteoms_bl_report_best.csv"

blast_hits = parse_csv(blast_csv_path)
disrupted_left_end=[]
disrupted_right_end=[]
first = True
for bh in blast_hits:
    if first:
        first = False
    else:
        sseqid = bh[2]
        slen = int(bh[3])
        sstart = int(bh[12])
        send = int(bh[13])
        if sstart == 1 and sseqid not in disrupted_left_end:
            disrupted_left_end.append(sseqid)
        elif send == slen and sseqid not in disrupted_right_end:
            disrupted_right_end.append(sseqid)

print len(disrupted_left_end)
print len(disrupted_right_end)
