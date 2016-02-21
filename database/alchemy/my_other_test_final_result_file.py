#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.alchemy.models import *
from database.alchemy.load_seq import *
from database.alchemy.load_bh import *


db_path = 'sqlite:////home/anna/Dropbox/phd/db/mito.db'
engine = create_engine(db_path)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# load_functions(session, "/home/anna/Dropbox/phd/db/proteomes/homo/data/human_mito.csv")


q = session.query(Sequence).filter("id = 512").first().subjects

ids = []
a = 0
for i in q:
    ids.append(i.id)
    a += i.id
ids = sorted(ids)

print a

