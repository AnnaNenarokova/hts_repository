#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.alchemy.models import *
from database.alchemy.load_seq import *
from database.alchemy.load_bh import *
from py_scripts.common_helpers.parse_dicts import *

def load_functions(session, csv_path, exact_ids=True, organism=''):
    for dic in csv_to_list_of_dicts(csv_path):
        seqid = dic['seqid']
        function = dic['function']

        if dic['mitochondrial'] == 'yes': mitochondrial = True
        elif dic['mitochondrial'] == 'no': mitochondrial = False
        else:
            print "Error in field 'mitochondrial' "
            sys.exit(1)

        if exact_ids: cur_seq = session.query(Sequence).filter(Sequence.seqid == dic['seqid']).one()
        else:
            cur_seq = session.query(Sequence).filter(Sequence.seqid.like("%" + dic['seqid'] + "%"), Sequence.organism == organism).one()
        cur_seq.function = function
        cur_seq.mitochondrial = mitochondrial
        session.add(cur_seq)
    session.commit()
    return 0

def load_targetp(session, targetp_csv_path):
    for dic in csv_to_list_of_dicts(targetp_csv_path):
        seqid = dic['seqid']
        loc = dic['loc']
        locrate = dic['locrate']
        cur_seq = session.query(Sequence).filter(Sequence.seqid == seqid).one()
        cur_seq.loc = loc
        cur_seq.locrate = locrate
        session.add(cur_seq)
    session.commit()
    return 0

def load_ogs(session, og_path):
    ogs = csv_to_list_of_dicts(og_path)
    i = 0
    for seq in session.query(Sequence):
        i+=1
        if i%1000 == 0: print i, 'sequences have been loaded'
        seqid = seq.seqid
        organism = seq.organism
        for og in ogs:
            if organism == 'Homo sapiens':
                break
            else:
                if seqid in og[organism]:
                    seq.og = og['OrthoGroup']
                    session.add(seq)
                    break
        else:
            print seqid, 'og has not been loaded'
    session.commit()
    return 0