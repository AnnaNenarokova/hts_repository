#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from blast.classes.blast import Blast
from blast.classes.blast_parser import BlastParser

query_pathes = {
'human' : '/home/anna/bioinformatics/euglena_project/mitocarta/Human.MitoCarta2.0.fasta',
'yeast' : '/home/anna/bioinformatics/euglena_project/yeast/yeast_orf_trans_all.fasta',
'trypanosoma' : '/home/anna/bioinformatics/euglena_project/tripanosoma/tr_proteins.fasta',
'euglena' : '/home/anna/bioinformatics/euglena_project/euglena/all_euglena_proteins/E_gracilis_transcriptome_final.PROTEINS.fasta',
'trypa_editing': '/home/anna/bioinformatics/euglena_project/tryp_editing.fasta'
}

db_pathes = {
'human' : '/home/anna/bioinformatics/euglena_project/mitocarta/Human.MitoCarta2.0/blast_db/Human.MitoCarta2.0.db',
'yeast' : '/home/anna/bioinformatics/euglena_project/yeast/orf_trans_all_yeast/blast_db/orf_trans_all_yeast.db',
'trypanosoma' : '/home/anna/bioinformatics/euglena_project/tripanosoma/tr_proteins/blast_db/tr_proteins.db',
'euglena' : '/home/anna/bioinformatics/euglena_project/euglena/all_euglena_proteins/E_gracilis_transcriptome_final.PROTEINS/blast_db/E_gracilis_transcriptome_final.PROTEINS.db'
}

# blast_csv_pathes = []
# for query in query_pathes:
#     for db in db_pathes:
#         new_blast = Blast(query_path=query_pathes[query], db_path=db_pathes[db], db_type='prot')
#         custom_outfmt = 'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'
#         blast_csv_path = new_blast.blast(bl_type='blastp', evalue=0.01, outfmt='comma_values', custom_outfmt=custom_outfmt, word_size=3)
#         print blast_csv_path
#         blast_csv_pathes.append(blast_csv_path)

# for blast_path in blast_csv_pathes:
#     print blast_path
# blast_dicts = BlastParser(blast_csv_path, features=custom_outfmt).read_hits()

new_blast = Blast(query_path=query_pathes['trypa_editing'], db_path=db_pathes['euglena'], db_type='prot')
custom_outfmt = 'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'
blast_csv_path = new_blast.blast(bl_type='blastp', evalue=0.01, outfmt='comma_values', custom_outfmt=custom_outfmt, word_size=3)