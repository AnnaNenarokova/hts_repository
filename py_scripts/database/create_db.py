#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from blast.classes.blast_parser import BlastParser
from database.models import *

Sequence.drop_table()
BlastHit.drop_table()
db.create_tables([Sequence, BlastHit])