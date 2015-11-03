#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from blast.classes.blast import Blast
from blast.classes.blast_parser import BlastParser

# query_path = '/home/anna/bioinformatics/euglena/Tripanosoma_Verner/Tr_proteins.fasta'
query_path = '/home/anna/bioinformatics/euglena/223_mitogenes/223_mitogenes_b2go.fasta'

db_path ='/home/anna/bioinformatics/euglena/Tripanosoma_Verner/Tr_proteins/blast_db/Tr_proteins.db'
# db_path = '/home/anna/bioinformatics/euglena/E_gracilis_transcriptome_final.PROTEINS/blast_db/E_gracilis_transcriptome_final.PROTEINS.db'

# new_blast = Blast(ref_path=ref_path, query_path=query_path, db_type='prot')

# new_blast = Blast(ref_path=ref_path, query_path=query_path, db_type='nucl')
# new_blast = Blast(db_path=db_path, query_path=query_path, db_type='nucl')
# new_blast.blast(bl_type='blastn', evalue=10, outfmt='comma_values')

# new_blast = Blast(db_path=db_path, query_path=query_path, db_type='prot')
# bl_report = new_blast.blast(bl_type='blastp', evalue=0.1, outfmt='comma_values')
bl_report = '/home/anna/bioinformatics/euglena/E_gracilis_transcriptome_final.PROTEINS/blast_db/bl_reports/E_gracilis_transcriptome_final.PROTE/Tr_proteins_bl_report.csv'
BlastParser(bl_report, 'csv').extract_unique_hits()