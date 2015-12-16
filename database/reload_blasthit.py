#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.blast.classes.blast_parser import BlastParser
from database.models import *
from py_scripts.biohelpers.seq_info_to_dict import *

BlastHit.drop_table()
db.create_table(BlastHit)
blast_csv_pathes = [
'/home/anna/bioinformatics/euglenozoa/euglena/all_euglena_proteins/E_gracilis_transcriptome_final.PROTEINS/blast_reports/tr_proteins_bl_report.csv',
'/home/anna/bioinformatics/euglenozoa/euglena/all_euglena_proteins/E_gracilis_transcriptome_final.PROTEINS/blast_reports/Human.MitoCarta2.0_bl_report.csv',
'/home/anna/bioinformatics/euglenozoa/euglena/all_euglena_proteins/E_gracilis_transcriptome_final.PROTEINS/blast_reports/yeast_orf_trans_all_bl_report.csv',
'/home/anna/bioinformatics/euglenozoa/tripanosoma/tr_proteins/blast_reports/human_mitocarta_bl_report.csv',
'/home/anna/bioinformatics/euglenozoa/tripanosoma/tr_proteins/blast_reports/yeast_orf_trans_all_bl_report.csv',
'/home/anna/bioinformatics/euglenozoa/tripanosoma/tr_proteins/blast_reports/E_gracilis_transcriptome_final.PROTEINS_bl_report.csv',
'/home/anna/bioinformatics/euglenozoa/mitocarta/Human.MitoCarta2.0/blast_reports/yeast_orf_trans_all_bl_report.csv',
'/home/anna/bioinformatics/euglenozoa/mitocarta/Human.MitoCarta2.0/blast_reports/tr_proteins_bl_report.csv',
'/home/anna/bioinformatics/euglenozoa/mitocarta/Human.MitoCarta2.0/blast_reports/E_gracilis_transcriptome_final.PROTEINS_bl_report.csv',
'/home/anna/bioinformatics/euglenozoa/yeast/orf_trans_all_yeast/blast_reports/Human.MitoCarta2.0_bl_report.csv',
'/home/anna/bioinformatics/euglenozoa/yeast/orf_trans_all_yeast/blast_reports/tr_proteins_bl_report.csv',
'/home/anna/bioinformatics/euglenozoa/yeast/orf_trans_all_yeast/blast_reports/E_gracilis_transcriptome_final.PROTEINS_bl_report.csv'
]

custom_outfmt = 'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'
for blast_csv_path in blast_csv_pathes:
    blast_dicts = BlastParser(blast_csv_path, features=custom_outfmt).read_hits()
    BlastHit.create_from_dicts(blast_dicts)