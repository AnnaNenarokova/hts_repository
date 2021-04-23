#!/usr/bin/python
import sys
sys.path.insert(0, "/Users/annanenarokova/work/code/ngs")
sys.path.insert(0, "/home/nenarokova/ngs/")
sys.path.insert(0, "../../")
from py_scripts.blast.classes.blast import Blast
from py_scripts.bioscripts.best_hits import *
from py_scripts.helpers.parse_csv import *

def blast_many(blast_pairs, custom_outfmt):
    blast_csv_paths = []
    for pair in blast_pairs:
        new_blast = Blast(query_path=pair['query'], db_path=pair['subj_db'], db_type='prot')
        blast_csv_path = new_blast.blast(bl_type='blastp', evalue=10, outfmt='comma_values', custom_outfmt=custom_outfmt, word_size=2)
        print (blast_csv_path)
        blast_csv_paths.append(blast_csv_path)
    for blast_path in blast_csv_paths:
        print (blast_path)
    return 0

def add_qlen_alen (blast_csv_path, fieldnames):
    blast_hits = csv_to_list_of_dicts(blast_csv_path)[0]
    result = []
    for bh in blast_hits:
        bh['alen_qlen'] = float(bh['length'])/ float(bh['qlen'])
        result.append(bh)
    fieldnames = fieldnames.split(' ')
    write_list_of_dicts(result, blast_csv_path, fieldnames=fieldnames)
    return 0

def add_header(blast_csv_path, custom_outfmt):
    blast_hits = parse_csv(blast_csv_path)
    header = custom_outfmt.split(' ')
    write_list_of_lists(blast_hits, blast_csv_path, header=header)
    return blast_csv_path

custom_outfmt = 'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'

query_paths= [
    "/home/nenarokova/amoebozoa/AmoebozoaOnlySSUHomeDatabase_all.fna"
    ]

subj_paths = [
    "/home/blastdb/nt_v5"
    ]

for query_path in query_paths:
    for subj_path in subj_paths:
        new_blast = Blast(query_path=query_path,subj_db=subj_path, db_type='nucl', threads=125)
        blast_csv_path = new_blast.blast(
                                         bl_type='blastn',
                                         evalue=0.001,
                                         outfmt='comma_values',
                                         #outfmt='pairwise',
                                         custom_outfmt=custom_outfmt,
                                         word_size=7
                                         )
        add_header(best_hits(blast_csv_path), custom_outfmt)
        add_header(blast_csv_path, custom_outfmt)
