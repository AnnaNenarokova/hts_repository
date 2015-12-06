#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from blast.classes.blast import Blast
from blast.classes.blast_parser import BlastParser

new_blast = Blast(ref_path=ref_path, query_path=query_path, db_type='prot')

custom_outfmt = ' qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send  '

bl_report = new_blast.blast(bl_type='blastp', evalue=0.00001, outfmt='comma_values', custom_outfmt=custom_outfmt, word_size=3)

blparser = BlastParser(bl_report, custom_outfmt)

q_path='/home/anna/bioinformatics/euglenozoa/tripanosoma/mitoproteome.csv'
q_path='/home/anna/bioinformatics/euglenozoa/mitocarta/mitocarta_human_functions.csv'
s_path='/home/anna/bioinformatics/euglenozoa/euglena/sequences/E_gracilis_transcriptome_final.PROTEINS/blast2go_annotdescriptions_20151104_1903.csv'