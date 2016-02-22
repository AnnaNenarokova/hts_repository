#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.alchemy.models import *
from database.alchemy.load_seq import *
from database.alchemy.load_bh import *

def reload_db(db_path, fasta_paths, blast_csv_paths=False, blast_outfmt=False, reload_seq=True, reload_bh=True, load_functions=True):
    engine = create_engine(db_path)
    if reload_seq: Sequence.__table__.drop(engine, checkfirst=True)
    if reload_bh: BlastHit.__table__.drop(engine, checkfirst=True)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    if reload_seq:
        for organism in data_paths:
            fasta_path=data_paths[organism]['fasta_path']
            description_path=data_paths[organism]['description_path']
            seqtype=data_paths[organism]['seqtype']
            load_fasta(session, fasta_path=fasta_path, description_path=description_path, seqtype=seqtype, organism=organism)
    if reload_bh:
        for blast_csv_path in blast_csv_paths:
            print blast_csv_path, 'is loading'
            load_blast_csv(session, blast_csv_path, custom_outfmt=blast_outfmt)
    if load_functions:
        pass
    return 0

db_path = 'sqlite:////home/anna/Dropbox/phd/db/mito.db'

data_paths = {
    'Arabidopsis thaliana': {'fasta_path': '/home/anna/Dropbox/phd/db/proteomes/arabidopsis/data/arabidopsis_mito.fasta', 'description_path': '/home/anna/Dropbox/phd/db/proteomes/arabidopsis/data/arabidopsis_mito.csv', 'seqtype': 'prot'},
    'Euglena gracilis': {'fasta_path':'/home/anna/Dropbox/phd/db/proteomes/euglena/data/euglena_all_proteins.fasta', 'description_path': '/home/anna/Dropbox/phd/db/proteomes/euglena/data/euglena_all_proteins.csv', 'seqtype': 'prot'},
    'Giardia intestinalis': {'fasta_path': '/home/anna/Dropbox/phd/db/proteomes/giardia/data/giardia_mito.fasta', 'description_path': '/home/anna/Dropbox/phd/db/proteomes/giardia/data/giardia_mito.csv', 'seqtype': 'prot'},
    'Homo sapiens': {'fasta_path': '/home/anna/Dropbox/phd/db/proteomes/homo/data/human_mito.fasta', 'description_path': '/home/anna/Dropbox/phd/db/proteomes/homo/data/human_mito.csv', 'seqtype': 'prot'},
    'Saccharomyces cerevisiae': {'fasta_path': '/home/anna/Dropbox/phd/db/proteomes/saccharomyces/data/yeast_mito.fasta', 'description_path': '/home/anna/Dropbox/phd/db/proteomes/saccharomyces/data/yeast_mito.csv', 'seqtype': 'prot'},
    'Trichomonas vaginalis': {'fasta_path': '/home/anna/Dropbox/phd/db/proteomes/trichomonas/data/trichomonas_mito.fasta', 'description_path': '/home/anna/Dropbox/phd/db/proteomes/trichomonas/data/trichomonas_mito.csv', 'seqtype': 'prot'},
    'Trypanosoma brucei': {'fasta_path': '/home/anna/Dropbox/phd/db/proteomes/trypanosoma/data/trypanosoma_mito.fasta', 'description_path': '/home/anna/Dropbox/phd/db/proteomes/trypanosoma/data/trypanosoma_mito.csv', 'seqtype': 'prot'}
                }

blast_csv_paths = [
'/home/anna/Dropbox/phd/db/proteomes/all_reference_mitoproteomes/blast_reports/euglena_all_proteins_bl_report.csv',
'/home/anna/Dropbox/phd/db/proteomes/euglena/data/E_gracilis_transcriptome_final.PROTEINS/blast_reports/reference_mitoproteomes_bl_report.csv'
]

blast_outfmt = 'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'
reload_db(db_path, data_paths, blast_csv_paths, blast_outfmt, reload_seq=True, reload_bh=True)