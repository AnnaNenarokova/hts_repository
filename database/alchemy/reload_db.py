#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Bio import SeqIO
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.alchemy.models import *
from py_scripts.common_helpers.make_outdir import *

def load_fasta(session, fasta_path, seqtype, organism='unknown organism', source=False, mitoscore=0.0):
    for record in SeqIO.parse(fasta_path, "fasta"):
        seqid = record.id
        if not source: source = file_from_path(fasta_path, endcut=6)
        new_seq = Sequence(seqid=seqid, seqtype=seqtype, organism=organism, source=source, extra_data={}, mitoscore=mitoscore)
        new_seq.extra_data['sequence'] = str(record.seq)
        new_seq.extra_data['description'] = str(record.description)
        session.add(new_seq)
    session.commit()
    return 0

# def load_

db_path = 'sqlite:////home/anna/Dropbox/phd/db/mito.db'
engine = create_engine(db_path)
Sequence.__table__.drop(engine)
# BlastHit.__table__.drop(engine)
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

fasta_pathes = {
    'Trypanosoma brucei': '/home/anna/Dropbox/phd/db/mitoproteomes/trypanosoma/trypa_mitoproteins.fasta',
    'Arabidopsis thaliana': '/home/anna/Dropbox/phd/db/mitoproteomes/arabidopsis/arabidopsis_mito.fasta',
    'Caenorhabditis elegans': '/home/anna/Dropbox/phd/db/mitoproteomes/caenorhabditis/worm_mitoproteins.fasta',
    'Homo sapiens': '/home/anna/Dropbox/phd/db/mitoproteomes/mitocarta/Human.MitoCarta2.0.fasta',
    'Mus musculus': '/home/anna/Dropbox/phd/db/mitoproteomes/mitocarta/Mouse.MitoCarta2.0.fasta'
                }
for organism in fasta_pathes:
    load_fasta(session, fasta_path=fasta_pathes[organism], seqtype='prot', organism=organism, mitoscore=1.0)

euglena_path = '/home/anna/Dropbox/phd/db/mitoproteomes/euglena/E_gracilis_transcriptome_final.PROTEINS.fasta'
load_fasta(session, fasta_path=euglena_path, seqtype='prot', organism='Euglena gracilis', mitoscore=0.0)