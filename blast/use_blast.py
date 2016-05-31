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
     }
        ]

query_path = '/home/anna/Dropbox/phd/bioinformatics/euglena_results/SufCB.fasta'
subj_path = '/home/anna/bioinformatics/phd/euglena_project/euglena/euglena/Euglena_gracilis_genome_V1/blast_db/Euglena_gracilis_genome_V1.db'
# subj_path = '/home/anna/Dropbox/phd/mitoproteome_project/genomes/trypanosoma/data/trypanosoma_mito/blast_db/trypanosoma_mito.db'
custom_outfmt = 'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'

new_blast = Blast(query_path=query_path, db_path=subj_path, db_type='nucl')
blast_csv_path = new_blast.blast(bl_type='tblastn',
                                 evalue=0.001,
                                 outfmt='comma_values',
                                 custom_outfmt=custom_outfmt,
                                 word_size=2)

add_header(best_hits(blast_csv_path), custom_outfmt)
