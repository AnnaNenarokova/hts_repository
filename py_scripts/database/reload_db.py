#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from blast.classes.blast_parser import BlastParser
from database.models import *
from biohelpers.seq_info_to_dict import *

Sequence.drop_table()
db.create_table(Sequence)

fasta_path = '/home/anna/bioinformatics/euglenozoa/euglena/all_euglena_proteins/E_gracilis_transcriptome_final.PROTEINS.fasta'
function_csv = '/home/anna/bioinformatics/euglenozoa/euglena/all_euglena_proteins/euglena_function_info.csv'
function_dict = seq_info_to_dict(function_csv)

loc_csv = '/home/anna/bioinformatics/euglenozoa/euglena/all_euglena_proteins/E_gracilis_transcriptome_final_PROTEINS_first_130_targetp_out.csv'
loc_dict = seq_info_to_dict(loc_csv)
Sequence.read_from_f(fasta_path, seqtype='protein', organism='Euglena gracilis', source='E_gracilis_transcriptome_final.PROTEINS', loc_dict=loc_dict, function_dict=function_dict)

fasta_path = '/home/anna/bioinformatics/euglenozoa/tripanosoma/tr_proteins.fasta'
loc_csv = '/home/anna/bioinformatics/euglenozoa/tripanosoma/tr_proteins_targetp_out.csv'
loc_dict = seq_info_to_dict(loc_csv)
function_csv = '/home/anna/bioinformatics/euglenozoa/tripanosoma/tr_proteins_functions.csv'
function_dict = seq_info_to_dict(function_csv)
Sequence.read_from_f(fasta_path, seqtype='protein', organism='Tripanosoma brucei', source='T. brucei table', loc_dict=loc_dict, function_dict=function_dict)

# fasta_path = '/home/anna/bioinformatics/euglenozoa/yeast/yeast_orf_trans_all.fasta'
# Sequence.read_from_f(fasta_path, seqtype='protein', organism='Saccharomyces cerevisiae', source='yeast_orf_trans_all')

# fasta_path = '/home/anna/bioinformatics/euglenozoa/mitocarta/Human.MitoCarta2.0.fasta'
# Sequence.read_from_f(fasta_path, seqtype='protein', organism='Homo sapiens', source='Human.MitoCarta2.0')


# BlastHit.drop_table()
# db.create_table(BlastHit)

# blast_csv_path = '/home/anna/bioinformatics/euglenozoa/mitocarta/Human.MitoCarta2.0/blast_reports/tr_proteins_bl_report.csv'
# custom_outfmt = 'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'

# blast_dicts = BlastParser(blast_csv_path, features=custom_outfmt).read_hits()

# BlastHit.create_from_dicts(blast_dicts)