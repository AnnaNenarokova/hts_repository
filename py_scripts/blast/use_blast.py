#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from blast.classes.blast import Blast
# query_path = '/home/anna/bioinformatics/euglena/Tripanosoma_Verner/Tr_proteins.fasta'
# query_path = '/home/anna/bioinformatics/euglena/mDNA/Euglena_mito_genes/rnsR_Path_24504_1.fa'
query_path = '/home/anna/bioinformatics/euglena/Tripanosoma_Verner/ATP_synthase_proteins.fasta'
# query_path = '/home/anna/bioinformatics/euglena/223_mitogenes/223_mitogenes_b2go.fasta'
db_path ='/home/anna/bioinformatics/euglena/Tripanosoma_Verner/Tr_proteins/blast_db/Tr_proteins.db'
# db_path = '/home/anna/bioinformatics/euglena/E_gracilis_transcriptome_final.PROTEINS/blast_db/E_gracilis_transcriptome_final.PROTEINS.db'
# db_path ='/home/anna/bioinformatics/euglena/E_gracilis_transcriptome_cds/db_folder/E_gracilis_transcriptome_cds.db'
# db_path ='/home/anna/bioinformatics/euglena/Euglena_gracilis_genome_V1/db_folder/Euglena_gracilis_genome_V1.db'

# new_blast = Blast(ref_path=ref_path, query_path=query_path, db_type='prot')
new_blast = Blast(db_path=db_path, query_path=query_path, db_type='prot')
new_blast.blast(bl_type='blastp', evalue=10, outfmt='tabular_comment_lines')

# new_blast = Blast(ref_path=ref_path, query_path=query_path, db_type='nucl')
# new_blast = Blast(db_path=db_path, query_path=query_path, db_type='nucl')
# new_blast.blast(bl_type='blastn', evalue=10, outfmt='comma_values')