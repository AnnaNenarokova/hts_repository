#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from blast.classes.blast import Blast
from blast.classes.blast_parser import BlastParser

# query_path = '/home/anna/bioinformatics/euglena/mDNA/mDNA_genes/mDNA_genes.fasta'
# query_path = '/home/anna/bioinformatics/euglena/Tripanosoma/atp6.fasta'
# query_path = '/home/anna/bioinformatics/euglena/Tripanosoma/Tr_proteins.fasta'
# query_path = '/home/anna/bioinformatics/euglena/223_mitogenes/223_mitogenes_b2go.fasta'

# ref_path = '/home/anna/bioinformatics/euglena/223_mitogenes/223_mitogenes.fasta'
# db_path ='/home/anna/bioinformatics/euglena/Tripanosoma/Tr_proteins/blast_db/Tr_proteins.db'
# db_path = '/home/anna/bioinformatics/euglena/E_gracilis_transcriptome_final.PROTEINS/blast_db/E_gracilis_transcriptome_final.PROTEINS.db'

# new_blast = Blast(ref_path=ref_path, query_path=query_path, db_type='nucl')
# new_blast = Blast(db_path=db_path, query_path=query_path, db_type='nucl')

# new_blast = Blast(ref_path=ref_path, query_path=query_path, db_type='prot')
# new_blast = Blast(db_path=db_path, query_path=query_path, db_type='prot')
# bl_report = new_blast.blast(bl_type='blastp', evalue=10, outfmt='comma_values', word_size=3)
# bl_report = '/home/anna/bioinformatics/euglena/E_gracilis_transcriptome_final.PROTEINS/blast_db/bl_reports/E_gracilis_transcriptome_final.PROTE/Tr_proteins_bl_report.csv'
# bl_report = '/home/anna/bioinformatics/euglena/Tripanosoma/Tr_proteins/blast_db/bl_reports/Tr_prote/223_mitogenes_b2go_bl_report.csv'
# blparser = BlastParser(bl_report, 'csv')
# q_path='/home/anna/bioinformatics/euglena/Tripanosoma/mitoproteome.csv'
# s_path='/home/anna/bioinformatics/euglena/E_gracilis_transcriptome_final.PROTEINS/blast2go_annotdescriptions_20151104_1903.csv'
# blparser.extract_unique_hits()
# blparser.add_functions(q_path=q_path,  q_delimiter=';', s_path=s_path, s_delimiter='\t')
# blparser.add_functions(q_path=q_path,  q_delimiter=';', s_path=s_path, s_delimiter='\t', hits = blparser.extract_unique_hits())

query_path = '/home/anna/bioinformatics/euglenozoa/Three excavates_editing proteins_sequences.fasta'
db_path = '/home/anna/bioinformatics/euglenozoa/euglena/sequences/Euglena_gracilis_genome_V1/db_folder/Euglena_gracilis_genome_V1.db'
new_blast = Blast(db_path=db_path, query_path=query_path, db_type='nucl')
new_blast.blast(bl_type='tblastn', evalue=10, outfmt='comma_values', word_size=3)