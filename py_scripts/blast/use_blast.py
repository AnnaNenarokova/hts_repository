#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from blast.classes.blast import Blast
from blast.classes.blast_parser import BlastParser

query_pathes = [
'/home/anna/bioinformatics/euglenozoa/mitocarta/Human.MitoCarta2.0.fasta',
'/home/anna/bioinformatics/euglenozoa/tripanosoma/tr_proteins.fasta',
'/home/anna/bioinformatics/euglenozoa/euglena/sequences/E_gracilis_transcriptome_final.PROTEINS.fasta'
]

db_pathes = [
'/home/anna/bioinformatics/euglenozoa/mitocarta/Human.MitoCarta2.0/blast_db/Human.MitoCarta2.0.db',
'/home/anna/bioinformatics/euglenozoa/tripanosoma/tr_proteins/blast_db/tr_proteins.db',
'/home/anna/bioinformatics/euglenozoa/euglena/sequences/E_gracilis_transcriptome_final.PROTEINS/blast_db/E_gracilis_transcriptome_final.PROTEINS.db'
]

new_blast = Blast(query_path=query_path, db_path=db_path, db_type='prot')

custom_outfmt = ' qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send  '

new_blast.blast(bl_type='blastp', evalue=0.01, outfmt='comma_values', custom_outfmt=custom_outfmt, word_size=3)
