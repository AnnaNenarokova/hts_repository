#!/usr/bin/python
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import csv
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from common_helpers.make_outdir import *
from common_helpers.lookahead import lookahead
from common_helpers.parse_csv import parse_csv, csv_to_dict



def add_functions(self, q_path,  q_delimiter, s_path, s_delimiter, hits=False):
        q_info = parse_csv(q_path, delimiter=q_delimiter)
        s_info = parse_csv(s_path, delimiter=s_delimiter)
        if not hits: hits = self.hits
        for hit in hits:
            for row in q_info:
                if hit['qseqid'] == row[0]:
                    hit['q_function'] = row[1]
            for row in s_info:
                if hit['sseqid'] == row[0]:
                    hit['s_function'] = row[1]
                    hit['s_GO_terms'] = row[2]

        qseqid_index = self.features.index('qseqid')
        self.features.insert(qseqid_index+1, 'q_function')
        sseqid_index = self.features.index('sseqid')
        self.features.insert(sseqid_index+1, 's_GO_terms')
        self.features.insert(sseqid_index+1, 's_function')

        outfile_path = new_file(self.blreport_path, new_end='_with_functions.csv')
        self.write_blast_csv(outfile_path=outfile_path, hits=hits, header=True)
        return hits

csv_path=''
