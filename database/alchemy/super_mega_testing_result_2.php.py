#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.alchemy.models import *
from database.alchemy.load_seq import *
from database.alchemy.load_bh import *
from py_scripts.common_helpers.parse_dicts import *

db_path = 'sqlite:////home/anna/Dropbox/phd/db/mito.db'
engine = create_engine(db_path)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

a = session.query(Sequence)
s = a[7635]
bh = s.best_subject_hit()

print "For: id =", s.id, " (", s.organism, ")"
print bh.id if bh else 'suka'
