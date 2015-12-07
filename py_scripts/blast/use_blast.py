#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from blast.classes.blast import Blast
from blast.classes.blast_parser import BlastParser

# query_path = '/home/anna/bioinformatics/euglenozoa/mitocarta/Human.MitoCarta2.0.fasta'
# db_path = '/home/anna/bioinformatics/euglenozoa/mitocarta/Human.MitoCarta2.0/blast_db/Human.MitoCarta2.0.db'

query_path = '/home/anna/bioinformatics/euglenozoa/tripanosoma/tr_proteins.fasta'
db_path = '/home/anna/bioinformatics/euglenozoa/tripanosoma/tr_proteins/blast_db/tr_proteins.db'

new_blast = Blast(db_path=db_path, query_path=query_path, db_type='prot')

custom_outfmt = ' qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send  '

new_blast.blast(bl_type='blastp', evalue=0.01, outfmt='comma_values', custom_outfmt=custom_outfmt, word_size=3)
