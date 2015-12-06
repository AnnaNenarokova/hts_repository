#!/usr/bin/python
import sys
import csv
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from common_helpers.make_outdir import *
from common_helpers.parse_csv import parse_csv
from blast.classes.blast_parser import BlastParser
from database.models import *

csv_data = parse_csv(csv_path, delimiter=delimiter)

db_path = '/home/anna/bioinformatics/euglenozoa/mitoproteome.db'

db = SqliteDatabase(db_path)

Protein.drop_table()
BlastHit.drop_table()
 
db.create_tables([Protein, BlastHit])

fasta_path = '/home/anna/bioinformatics/euglenozoa/mitocarta/Human.MitoCarta2.0.fasta'
seq_type = 'protein'
Sequence.read_from_fasta(fasta_path, seq_type, organism='Homo sapiens', source='Human.MitoCarta2.0')