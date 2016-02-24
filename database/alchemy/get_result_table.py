#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.alchemy.models import *
from sqlalchemy.orm import joinedload
from py_scripts.common_helpers.parse_csv import *

def get_result_table(db_path, outpath):
    engine = create_engine(db_path)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    seqs = session.query(Sequence).options(joinedload('query_blasthits'))
    i = 0

    fieldnames = ['seqid', 'og', 'mitochondrial', 'loc', 'locrate', 'function', 'subj_id', 'subj_og', 'organism', 'subj_function', 'evalue', 'alen_slen', 'rev_evalue', 'rev_alen_qlen', 'best_rev_hit']
    default_seq_dict = {}
    for name in fieldnames:
        default_seq_dict[name] = ''

    result_table = []
    for seq in seqs:
        if seq.organism == 'Euglena gracilis' : #and seq.mitochondrial==True: # and not(seq.loc == 'M' and seq.locrate == 1):
            if i%1000==0:print i
            i+=1

            seq_dict = default_seq_dict.copy()

            seq_dict['seqid'] = seq.seqid
            seq_dict['og'] = seq.og
            seq_dict['mitochondrial'] = seq.mitochondrial
            seq_dict['loc'] = seq.loc
            seq_dict['locrate'] = seq.locrate
            seq_dict['function'] = seq.function

            bs = seq.best_subject()
            if bs:
                bsseq = bs[0]
                seq_dict['subj_id'] = bsseq.seqid
                seq_dict['subj_og'] = bsseq.og
                seq_dict['organism'] = bsseq.organism
                seq_dict['subj_function'] = bsseq.function

                bsh = bs[1]
                seq_dict['evalue'] = bsh.evalue
                seq_dict['alen_slen'] = bsh.alen_slen

                reverse_hit = seq.get_reverse_blasthit(bsseq)
                if reverse_hit:
                    seq_dict['rev_evalue'] = reverse_hit[0].evalue
                    seq_dict['rev_alen_qlen'] = reverse_hit[0].alen_qlen
                    seq_dict['best_rev_hit'] = reverse_hit[1]
            # if (seq_dict['og'] == seq_dict['subj_og']) and (seq_dict['evalue'] < 0.00001) and (seq_dict['rev_evalue'] < 0.00001): # and (seq_dict['best_rev_hit'] == True)
            if True:
                result_table.append(seq_dict)
    write_list_of_dicts(result_table, outpath, fieldnames=fieldnames)
    return outpath


db_path = 'sqlite:////home/anna/Dropbox/phd/db/mito.db'
outpath = '/home/anna/Dropbox/phd/db/result_all.csv'
get_result_table(db_path, outpath)