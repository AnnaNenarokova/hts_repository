#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.alchemy.models import *
from database.alchemy.load_seq import *
from database.alchemy.load_bh import *

def reload_db(db_path, fasta_pathes, blast_csv_pathes=False, blast_outfmt=False, reload_seq=True, reload_bh=True, load_functions=True):
    engine = create_engine(db_path)
    if reload_seq: Sequence.__table__.drop(engine, checkfirst=True)
    if reload_bh: BlastHit.__table__.drop(engine, checkfirst=True)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    if reload_seq:
        for organism in fasta_pathes:
            if organism == 'Euglena gracilis': mitoscore=0.0
            else: mitoscore=1.0
            load_fasta(session, fasta_path=fasta_pathes[organism], seqtype='prot', organism=organism)
    if reload_bh:
        for blast_csv_path in blast_csv_pathes:
            print blast_csv_path, 'is loading'
            load_blast_csv(session, blast_csv_path, custom_outfmt=blast_outfmt)
    if load_functions:
        pass
    return 0

db_path = 'sqlite:////home/anna/Dropbox/phd/db/mito.db'

fasta_pathes = {
    'Arabidopsis thaliana': '/home/anna/Dropbox/phd/db/proteomes/arabidopsis/data/arabidopsis_mito.fasta',
    'Euglena gracilis': '/home/anna/Dropbox/phd/db/proteomes/euglena/data/euglena_all_proteins.fasta',
    'Giardia intestinalis': '/home/anna/Dropbox/phd/db/proteomes/giardia/data/giardia_mito.fasta',
    'Homo sapiens': '/home/anna/Dropbox/phd/db/proteomes/homo/data/human_mito.fasta',
    'Saccharomyces cerevisiae': '/home/anna/Dropbox/phd/db/proteomes/saccharomyces/data/yeast_mito.fasta',
    'Trichomonas vaginalis': '/home/anna/Dropbox/phd/db/proteomes/trichomonas/data/trichomonas_mito.fasta',
    'Trypanosoma brucei': '/home/anna/Dropbox/phd/db/proteomes/trypanosoma/data/trypanosoma_mito.fasta'
                }

blast_csv_pathes = [
'/home/anna/Dropbox/phd/db/proteomes/reference_mitoproteomes/blast_reports/euglena_all_proteins_bl_report.csv',
'/home/anna/Dropbox/phd/db/proteomes/euglena/data/E_gracilis_transcriptome_final.PROTEINS/blast_reports/reference_mitoproteomes_bl_report.csv'
]

blast_outfmt = 'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'
reload_db(db_path, fasta_pathes, blast_csv_pathes, blast_outfmt, reload_seq=True, reload_bh=True)