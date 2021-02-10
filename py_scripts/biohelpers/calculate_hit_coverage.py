#!/usr/bin/python
import sys
sys.path.insert(0, "/Users/annanenarokova/work/code/ngs/")
sys.path.insert(0, "/home/users/nenarokova/ngs/")
from py_scripts.helpers.parse_csv import *

def merge_intervals(intervals):
    intervals.sort(key=lambda interval: interval[0])
    merged_intervals = [intervals[0]]
    for current in intervals:
        previous = merged_intervals[-1]
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged_intervals.append(current)
    return merged_intervals

def sum_interval_length(intervals):
    sum_int_length = 0
    for interval in intervals:
        length = interval[1] - interval[0]
        sum_int_length += length
    return sum_int_length

def calculate_hit_cov_query(blast_hits):
    if blast_hits == []:
        hit_coverage = float(0)
    else:
        total_length = int(blast_hits[0]['qlen'])

        intervals = []
        for blast_hit in blast_hits:
            new_interval = sorted( [ int(blast_hit['qstart']), int(blast_hit['qend']) ] )
            intervals.append(new_interval)
        intervals = merge_intervals(intervals)

        hit_sum_length = sum_interval_length(intervals)

        hit_coverage = float(hit_sum_length)/float(total_length)
    return hit_coverage

def get_contigs_hits(blast_csv_path):
    blast_hits = parse_csv(blast_csv_path, '\t')
    contigs_hits = {}
    for bh in blast_hits:
        qseqid = bh[qseqid_index]
        qlen = int(bh[qlen_index])
        qstart = int(bh[qstart_index])
        qend = int(bh[qend_index])
        if qseqid not in contigs_hits.keys():
            contigs_hits[qseqid] = []
        contigs_hits[qseqid].append([qstart, qend])
    return contigs_hits  