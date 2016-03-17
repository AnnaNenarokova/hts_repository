#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from blast.classes.blast import Blast
from py_scripts.biohelpers.best_hits import *

def blast_many(blast_pairs, custom_outfmt):
    blast_csv_paths = []
    for pair in blast_pairs:
        new_blast = Blast(query_path=pair['query'], db_path=pair['subj_db'], db_type='prot')
        blast_csv_path = new_blast.blast(bl_type='blastp', evalue=10, outfmt='comma_values', custom_outfmt=custom_outfmt, word_size=2)
        print blast_csv_path
        blast_csv_paths.append(blast_csv_path)

    for blast_path in blast_csv_paths:
        print blast_path
    return 0

def add_header(blast_csv_path, custom_outfmt):
    blast_hits = parse_csv(blast_csv_path)
    header = custom_outfmt.split(' ')
    write_list_of_lists(blast_hits, blast_csv_path, header=header)
    return blast_csv_path

blast_pairs = [
 {
    'query':'/home/anna/Dropbox/phd/mitoproteomes/proteomes/trypanosoma/MT_ATP6.fasta',
    'query':'/home/anna/Dropbox/phd/mitoproteomes/proteomes/euglena/article/mch00883-mmc7.fasta',
    'subj_db':'/home/anna/Dropbox/phd/mitoproteomes/proteomes/euglena/data/E_gracilis_transcriptome_final.PROTEINS/blast_db/E_gracilis_transcriptome_final.PROTEINS.db'
      }
        ]

query_path = '/home/anna/Dropbox/phd/mitoproteomes/proteomes/euglena/article/egra_all.fasta'
db_path = '/home/anna/Dropbox/phd/mitoproteomes/proteomes/euglena/data/E_gracilis_transcriptome_final.PROTEINS/blast_db/E_gracilis_transcriptome_final.PROTEINS.db'

custom_outfmt = 'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'

# new_blast = Blast(query_path=query_path, db_path=db_path, db_type='prot')
# blast_csv_path = new_blast.blast(bl_type='blastp', evalue=0.01, outfmt='comma_values', custom_outfmt=custom_outfmt, word_size=2)

blast_csv_path = '/home/anna/Dropbox/phd/mitoproteomes/454mitoAllCont/blast_reports/egra_all_bl_report.csv'
add_header(best_hits(blast_csv_path), custom_outfmt)