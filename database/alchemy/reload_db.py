#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Bio import SeqIO
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.alchemy.models import *
from py_scripts.common_helpers.make_outdir import *
from blast.classes.blast_parser import BlastParser

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

def load_from_blast_csv(session, blast_csv_path, custom_outfmt=False):
    if not custom_outfmt:
        custom_outfmt = 'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'
    blast_dicts = BlastParser(blast_csv_path, features=custom_outfmt).read_hits()
    for blast_dict in blast_dicts:
        query_id, subject_id = blast_dict['qseqid'], blast_dict['sseqid']
        evalue, length = blast_dict['evalue'], blast_dict['length']
        qlen, slen = blast_dict['qlen'], blast_dict['slen']
        alen_qlen, alen_slen = float(length/float(qlen)), float(length/float(slen))
        other_features = {}
        for feature in blast_dict:
            if feature not in ['qseqid', 'sseqid', 'evalue', 'length']:
                other_features[feature] = blast_dict[feature]

        query = Sequence.select().where(Sequence.seqid == query_id).get()
        subject = Sequence.select().where(Sequence.seqid == subject_id).get()
        BlastHit.create(query=query, subject=subject, evalue=evalue, length=length,
                        qlen=qlen, slen=slen, alen_qlen=alen_qlen, alen_slen=alen_slen,
                        extra_data=other_features)

def reload_db(db_path, fasta_pathes, blast_csv_pathes, blast_outfmt, reload_seq=True, reload_bh=True):
    engine = create_engine(db_path)
    if reload_seq: Sequence.__table__.drop(engine, checkfirst=True)
    BlastHit.__table__.drop(engine, checkfirst=True)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    if reload_seq:
        for organism in fasta_pathes:
            if organism == 'Euglena gracilis': mitoscore=0.0
            else: mitoscore=1.0
            load_fasta(session, fasta_path=fasta_pathes[organism], seqtype='prot', organism=organism, mitoscore=mitoscore)
    if reload_bh:
        for blast_csv_path in blast_csv_pathes:
            blast_dicts = BlastParser(blast_csv_path, features=blast_outfmt).read_hits()
            load_from_blast_csv(session, blast_csv_path, custom_outfmt=blast_outfmt)
    return 0

db_path = 'sqlite:////home/anna/Dropbox/phd/db/mito.db'

fasta_pathes = {
    'Arabidopsis thaliana': '/home/anna/Dropbox/phd/db/mitoproteomes/arabidopsis/arabidopsis_mito.fasta',
    'Caenorhabditis elegans': '/home/anna/Dropbox/phd/db/mitoproteomes/caenorhabditis/worm_mitoproteins.fasta',
    'Homo sapiens': '/home/anna/Dropbox/phd/db/mitoproteomes/mitocarta/Human.MitoCarta2.0.fasta',
    'Mus musculus': '/home/anna/Dropbox/phd/db/mitoproteomes/mitocarta/Mouse.MitoCarta2.0.fasta',
    'Saccharomyces cerevisiae': '/home/anna/Dropbox/phd/db/mitoproteomes/saccharomyces/yeast_orf_trans_all.fasta',
    'Tetrahymena thermophilia': '/home/anna/Dropbox/phd/db/mitoproteomes/tetrahymena/tetrahymena_mito_gb.fasta',
    'Trypanosoma brucei': '/home/anna/Dropbox/phd/db/mitoproteomes/trypanosoma/trypa_mitoproteins.fasta',
    'Euglena gracilis': '/home/anna/Dropbox/phd/db/mitoproteomes/euglena/E_gracilis_transcriptome_final.PROTEINS.fasta'
                }

blast_csv_pathes = [
'/home/anna/Dropbox/phd/db/mitoproteomes/mitocarta/Human.MitoCarta2.0/blast_reports/E_gracilis_transcriptome_final.PROTEINS_bl_report.csv'
]

blast_outfmt = 'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'
reload_db(db_path, fasta_pathes, blast_csv_pathes, blast_outfmt, reload_seq=True, reload_bh=False)