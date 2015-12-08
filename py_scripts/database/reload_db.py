#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from blast.classes.blast_parser import BlastParser
from database.models import *
from biohelpers.seq_info_to_dict import *

Sequence.drop_table()
db.create_table(Sequence)

seq_type = 'protein'
# fasta_path = '/home/anna/bioinformatics/euglenozoa/euglena/sequences/E_gracilis_transcriptome_final.PROTEINS.fasta'
# Sequence.read_from_fasta(fasta_path, seq_type, organism='Euglena gracilis', source='E_gracilis_transcriptome_final.PROTEINS')

fasta_path = '/home/anna/bioinformatics/euglenozoa/tripanosoma/tr_proteins.fasta'

loc_csv = '/home/anna/bioinformatics/euglenozoa/tripanosoma/tr_proteins_targetp_out.csv'
loc_dict = seq_info_to_dict(loc_csv)
function_csv = '/home/anna/bioinformatics/euglenozoa/tripanosoma/tr_proteins_functions.csv'
function_dict = seq_info_to_dict(function_csv)

Sequence.read_from_f(fasta_path, seq_type, organism='Tripanosoma brucei', source='T. brucei table', loc_dict=loc_dict, function_dict=function_dict)

# fasta_path = '/home/anna/bioinformatics/euglenozoa/yeast/yeast_orf_trans_all.fasta'
# Sequence.read_from_f(fasta_path, seq_type, organism='Saccharomyces cerevisiae', source='yeast_orf_trans_all')

# fasta_path = '/home/anna/bioinformatics/euglenozoa/mitocarta/Human.MitoCarta2.0.fasta'
# Sequence.read_from_f(fasta_path, seq_type, organism='Homo sapiens', source='Human.MitoCarta2.0')


# BlastHit.drop_table()
# db.create_table(BlastHit)

# blast_csv_path = '/home/anna/bioinformatics/euglenozoa/mitocarta/Human.MitoCarta2.0/blast_reports/tr_proteins_bl_report.csv'
# custom_outfmt = 'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'

# blast_dicts = BlastParser(blast_csv_path, features=custom_outfmt).read_hits()

# BlastHit.create_from_dicts(blast_dicts)