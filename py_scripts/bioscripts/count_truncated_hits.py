#!/usr/bin/python
import sys
sys.path.insert(0, "/Users/annanenarokova/work/code/ngs/")
sys.path.insert(0, "/home/users/nenarokova/ngs/")
from py_scripts.helpers.parse_csv import *

'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'

def count_truncated_hits(blast_csv_path):
    blast_hits = parse_csv(blast_csv_path)
    disrupted_left_end=[]
    disrupted_right_end=[]
    first = True
    for bh in blast_hits:
        if first:
            first = False
        else:
            qstart = int(bh[10])
            qend = int(bh[11])
            qlen = bh[1]
            sseqid = bh[2]
            slen = int(bh[3])
            sstart = int(bh[12])
            send = int(bh[13])
            if (sstart == 1) and (sseqid not in disrupted_left_end) and (qstart != 1):
                disrupted_left_end.append(sseqid)
            elif send == slen and (sseqid not in disrupted_right_end) and (qlen != qend):
                disrupted_right_end.append(sseqid)

    print "Truncated left end", len(disrupted_left_end)
    print "Truncated right end", len(disrupted_right_end)

    discrupted_into_2_contigs = []

    for contig in disrupted_left_end:
        if contig in disrupted_right_end:
            discrupted_into_2_contigs.append(contig)

    print "Discrupted into 2 contigs", len (discrupted_into_2_contigs)

    return 0

blast_csv_path = "/home/anna/bioinformatics/blasto/jaculum/all_kinetoplastid_references.faa_bl_report_best.csv"

count_truncated_hits(blast_csv_path)
