#!/usr/bin/python
import sys
import csv
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from common_helpers.make_outdir import *
from common_helpers.parse_csv import parse_csv
from blast.classes.blast_parser import BlastParser
from database.models import *

Sequence.drop_table()
BlastHit.drop_table()

db.create_table(Sequence)
db.create_table(BlastHit)

fasta_path = '/home/anna/bioinformatics/euglenozoa/mitocarta/Human.MitoCarta2.0.fasta'
seq_type = 'protein'
Sequence.read_from_fasta(fasta_path, seq_type, organism='Homo sapiens', source='Human.MitoCarta2.0')

fasta_path = '/home/anna/bioinformatics/euglenozoa/tripanosoma/tr_proteins.fasta'
seq_type = 'protein'
Sequence.read_from_fasta(fasta_path, seq_type, organism='Tripanosoma brucei', source='T.brucei table')

blast_csv_path = '/home/anna/bioinformatics/euglenozoa/mitocarta/Human.MitoCarta2.0/blast_reports/tr_proteins_bl_report.csv'
custom_outfmt = 'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'

blast_dicts = BlastParser(blast_csv_path, features=custom_outfmt).read_hits()

BlastHit.create_from_dicts(blast_dicts)