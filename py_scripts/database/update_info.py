#!/usr/bin/python
from peewee import *
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from blast.classes.blast_parser import BlastParser
from database.models import *
from common_helpers.parse_csv import *

csv_info_path = '/home/anna/bioinformatics/euglenozoa/mitocarta/Human.MitoCarta.2.0.csv'

info_dict = csv_to_dict(csv_info_path, main_key='seqid')
with db.atomic():
    for seqid in info_dict:
        seq_info = info_dict[seqid]
        other_info = {}
        for key in seq_info:
            if key not in ('function', 'mitoscore') and key in info_dict:
                other_info[key] = info_dict[key]

        Sequence.update(function=seq_info['function'], mitoscore=seq_info['mitoscore']).where(Sequence.seqid == seqid)
