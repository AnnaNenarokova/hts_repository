#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Bio import SeqIO
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.alchemy.models import *
from py_scripts.common_helpers.make_outdir import *

db_path = 'sqlite:////home/anna/Dropbox/phd/db/mito.db'
engine = create_engine(db_path)
Sequence.__table__.drop(engine)
# BlastHit.__table__.drop(engine)
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

blast_pathes = {
                }
for organism in fasta_pathes:
    load_fasta(session, fasta_path=fasta_pathes[organism], seqtype='prot', organism=organism, mitoscore=1.0)

euglena_path = '/home/anna/Dropbox/phd/db/mitoproteomes/euglena/E_gracilis_transcriptome_final.PROTEINS.fasta'
load_fasta(session, fasta_path=euglena_path, seqtype='prot', organism='Euglena gracilis', mitoscore=0.0)

