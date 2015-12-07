#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from blast.classes.blast import Blast
from blast.classes.blast_parser import BlastParser

query_pathes = {
'human' : '/home/anna/bioinformatics/euglenozoa/mitocarta/Human.MitoCarta2.0.fasta',
'yeast' : '/home/anna/bioinformatics/euglenozoa/yeast/orf_trans_all_yeast.fasta',
'tripanosoma' : '/home/anna/bioinformatics/euglenozoa/tripanosoma/tr_proteins.fasta',
'euglena' : '/home/anna/bioinformatics/euglenozoa/euglena/sequences/E_gracilis_transcriptome_final.PROTEINS.fasta',
}

db_pathes = {
'human' : '/home/anna/bioinformatics/euglenozoa/mitocarta/Human.MitoCarta2.0/blast_db/Human.MitoCarta2.0.db',
'yeast' : '/home/anna/bioinformatics/euglenozoa/yeast/orf_trans_all_yeast/blast_db/orf_trans_all_yeast.db',
'tripanosoma' : '/home/anna/bioinformatics/euglenozoa/tripanosoma/tr_proteins/blast_db/tr_proteins.db',
'euglena' : '/home/anna/bioinformatics/euglenozoa/euglena/sequences/E_gracilis_transcriptome_final.PROTEINS/blast_db/E_gracilis_transcriptome_final.PROTEINS.db'
}

query_path = query_pathes['tripanosoma']
db_path = db_pathes['yeast']

new_blast = Blast(query_path=query_path, db_path=db_path, db_type='prot')

custom_outfmt = 'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'

blast_csv_path = new_blast.blast(bl_type='blastp', evalue=0.01, outfmt='comma_values', custom_outfmt=custom_outfmt, word_size=3)

blast_dicts = BlastParser(blast_csv_path, features=custom_outfmt).read_hits()