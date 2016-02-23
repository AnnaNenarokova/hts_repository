#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.alchemy.models import *
from database.alchemy.load_seq import *
from database.alchemy.load_bh import *
from sqlalchemy.orm import joinedload
from py_scripts.common_helpers.parse_dicts import *

db_path = 'sqlite:////home/anna/Dropbox/phd/db/mito.db'
engine = create_engine(db_path)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

seqs = session.query(Sequence).options(joinedload('query_blasthits'))
i = 0
j = 0
k = 0
l = 0
for seq in seqs:
    if seq.organism == 'Euglena gracilis':
        if i%1000==0:print i
        i+=1
        bs = seq.best_subject()
        if bs:
            j+=1
            best = seq.get_reverse_blasthit(bs[0])
            if best[0]:
                k+=1
                if best[1]:
                    l+=1

print j, k, l