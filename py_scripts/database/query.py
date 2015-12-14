#!/usr/bin/python
from peewee import *
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from blast.classes.blast_parser import BlastParser
from database.models import *
from common_helpers.parse_csv import *

select = Sequence.select().join(Blasthit).where(
    query.organism =='Euglena gracilis' and
        (subject.organism = 'Tripanosoma brucei' or  subject.organism = 'Homo sapiens' or
            (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore=100)
        )
    and blasthit.evalue < 0.00001 and blasthit.alen_qlen > 0.3
    )