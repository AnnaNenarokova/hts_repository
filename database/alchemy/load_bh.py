#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.alchemy.models import *

def load_blast_csv(session, blast_csv_path, custom_outfmt=False):
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

        query = session.query(Sequence).filter(Sequence.seqid == query_id).one()
        subject = session.query(Sequence).filter(Sequence.seqid == subject_id).one()
        new_bh = BlastHit(query=query, subject=subject, evalue=evalue, length=length,
                        qlen=qlen, slen=slen, alen_qlen=alen_qlen, alen_slen=alen_slen,
                        extra_data=other_features)
        session.add(new_bh)
    session.commit()