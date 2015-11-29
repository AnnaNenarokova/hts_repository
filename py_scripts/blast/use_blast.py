#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from blast.classes.blast import Blast
from blast.classes.blast_parser import BlastParser

# query_path = '/home/anna/bioinformatics/euglenozoa/Three excavates_editing proteins_sequences.fasta'
# query_path = '/home/anna/bioinformatics/euglenozoa/tripanosoma/tr_proteins.fasta'
query_path = '/home/anna/bioinformatics/euglenozoa/tripanosoma/editing proteins.fasta'

# db_path = '/home/anna/bioinformatics/euglenozoa/euglena/sequences/223_mitogenes/223_mitogenes/blast_db/223_mitogenes.db'
db_path = '/home/anna/bioinformatics/euglenozoa/euglena/sequences/E_gracilis_transcriptome_final.PROTEINS/blast_db/E_gracilis_transcriptome_final.PROTEINS.db'

# new_blast = Blast(db_path=db_path, query_path=query_path, db_type='nucl')
new_blast = Blast(db_path=db_path, query_path=query_path, db_type='prot')
# new_blast = Blast(ref_path=ref_path, query_path=query_path, db_type='nucl')
# new_blast = Blast(ref_path=ref_path, query_path=query_path, db_type='prot')

custom_outfmt = ' qseqid qlen sseqid slen length pident mismatch gaps qstart qend sstart send evalue '
bl_report = new_blast.blast(bl_type='blastp', evalue=10, outfmt='comma_values', custom_outfmt=custom_outfmt, word_size=3)
# bl_report = new_blast.blast(bl_type='blastp', evalue=10, outfmt='comma_values', word_size=3)

# bl_report = '/home/anna/bioinformatics/euglenozoa/euglena/sequences/E_gracilis_transcriptome_final.PROTEINS/blast_reports/tr_proteins_bl_report.csv'
# bl_report = '/home/anna/bioinformatics/euglenozoa/euglena/sequences/E_gracilis_transcriptome_final.PROTEINS/blast_reports/editing_ proteins_bl_report_proteome.csv'
# bl_report = '/home/anna/bioinformatics/euglenozoa/euglena/sequences/223_mitogenes/223_mitogenes/blast_reports/Three excavates_editing proteins_sequences_bl_report.csv'
blparser = BlastParser(bl_report, custom_outfmt)

q_path='/home/anna/bioinformatics/euglenozoa/tripanosoma/mitoproteome.csv'
s_path='/home/anna/bioinformatics/euglenozoa/euglena/sequences/E_gracilis_transcriptome_final.PROTEINS/blast2go_annotdescriptions_20151104_1903.csv'

blparser.extract_best()
blparser.add_functions(q_path=q_path, q_delimiter=';', s_path=s_path, s_delimiter='\t')