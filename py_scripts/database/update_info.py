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
        other_new_info = {}
        for key in seq_info:
            if key not in ('function', 'mitoscore'):
                other_new_info[key] = seq_info[key]
        sequence = Sequence.get(Sequence.seqid == seqid)
        extra_data = sequence.extra_data
        extra_data.update(other_new_info)
        query = Sequence.update(function=seq_info['function'], mitoscore=seq_info['mitoscore'], extra_data=extra_data).where(Sequence.seqid==seqid)
        query.execute()