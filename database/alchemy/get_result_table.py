#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
sys.path.insert(0, "/home/nenarokova/ngs/")
from database.alchemy.models import *
from sqlalchemy.orm import joinedload
from py_scripts.common_helpers.parse_csv import *

def get_result_table_euglena(db_path, outpath):
    engine = create_engine(db_path)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    heap_size = 100000
    total_amount = session.query(Sequence).count()
    n_pages = total_amount/heap_size

    fieldnames = ['seqid', 'og', 'b2go_mito', 'loc', 'locrate', 'function', 'subj_id', 'subj_og', 'organism', 'subj_function', 'evalue', 'alen_slen', 'pident', 'rev_evalue', 'rev_pident', 'rev_alen_qlen', 'is_best?', 'best_rev_evalue', 'best_rev_pident']
    default_seq_dict = {}

    for name in fieldnames:
        default_seq_dict[name] = ''
    result_table = []

    print 'total pages: ', (n_pages + 1)
    for page in range(n_pages + 1):
        print 'page ', page
        seqs = session.query(Sequence).order_by('id').limit(heap_size).offset(heap_size*page).options(joinedload('query_blasthits'))
        for seq in seqs:
            if seq.organism == 'Euglena gracilis':
                seq_dict = default_seq_dict.copy()

                seq_dict['seqid'] = seq.seqid
                seq_dict['og'] = seq.og
                seq_dict['b2go_mito'] = seq.mitochondrial
                seq_dict['loc'] = seq.loc
                seq_dict['locrate'] = seq.locrate
                seq_dict['function'] = seq.function

                bs = seq.best_subject()
                if bs:
                    bsseq = bs['sequence']
                    seq_dict['subj_id'] = bsseq.seqid
                    seq_dict['subj_og'] = bsseq.og
                    seq_dict['organism'] = bsseq.organism
                    seq_dict['subj_function'] = bsseq.function

                    bsh = bs['hit']
                    seq_dict['evalue'] = bsh.evalue
                    seq_dict['alen_slen'] = bsh.alen_slen
                    seq_dict['pident'] = bsh.extra_data['pident']
                    reverse_hit = seq.get_reverse_blasthit(bsseq)

                    if reverse_hit:
                        seq_dict['rev_evalue'] = reverse_hit['hit'].evalue
                        seq_dict['rev_alen_qlen'] = reverse_hit['hit'].alen_qlen
                        seq_dict['rev_pident'] = reverse_hit['hit'].extra_data['pident']
                        seq_dict['is_best?'] = reverse_hit['is_best']
                        seq_dict['best_rev_evalue'] = reverse_hit['bsh'].evalue
                        seq_dict['best_rev_pident'] = reverse_hit['bsh'].extra_data['pident']
                if (seq_dict['evalue'] < 0.00001) and (seq_dict['rev_evalue'] < 0.01) and (seq_dict['alen_slen'] >= 0.3) and bsseq.mitochondrial:
                    result_table.append(seq_dict)
    write_list_of_dicts(result_table, outpath, fieldnames=fieldnames)
    return outpath


def get_result_table_perk(db_path, outpath):
    engine = create_engine(db_path)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    heap_size = 2500
    total_amount = session.query(Sequence).count()
    n_pages = total_amount/heap_size

    fieldnames = ['seqid', 'loc', 'locrate', 'subj_id','organism', 'subj_function', 'evalue', 'alen_slen', 'pident', 'rev_evalue', 'rev_pident', 'rev_alen_qlen', 'is_best?', 'best_rev_evalue', 'best_rev_pident']
    default_seq_dict = {}

    for name in fieldnames:
        default_seq_dict[name] = ''
    result_table = []

    print 'total pages: ', (n_pages + 1)
    for page in range(n_pages + 1):
        print 'page ', page
        seqs = session.query(Sequence).order_by('id').limit(heap_size).offset(heap_size*page).options(joinedload('query_blasthits'))
        for seq in seqs:
            if seq.organism == 'Perkinsela amoebae':
                seq_dict = default_seq_dict.copy()

                seq_dict['seqid'] = seq.seqid
                seq_dict['loc'] = seq.loc
                seq_dict['locrate'] = seq.locrate

                bs = seq.best_subject()
                if bs:
                    bsseq = bs['sequence']
                    seq_dict['subj_id'] = bsseq.seqid
                    seq_dict['organism'] = bsseq.organism
                    seq_dict['subj_function'] = bsseq.function

                    bsh = bs['hit']
                    seq_dict['evalue'] = bsh.evalue
                    seq_dict['alen_slen'] = bsh.alen_slen
                    seq_dict['pident'] = bsh.extra_data['pident']
                    reverse_hit = seq.get_reverse_blasthit(bsseq)

                    if reverse_hit:
                        seq_dict['rev_evalue'] = reverse_hit['hit'].evalue
                        seq_dict['rev_alen_qlen'] = reverse_hit['hit'].alen_qlen
                        seq_dict['rev_pident'] = reverse_hit['hit'].extra_data['pident']
                        seq_dict['is_best?'] = reverse_hit['is_best']
                        seq_dict['best_rev_evalue'] = reverse_hit['bsh'].evalue
                        seq_dict['best_rev_pident'] = reverse_hit['bsh'].extra_data['pident']
                if ((seq_dict['evalue'] < 0.00001) and (seq_dict['rev_evalue'] < 0.01) and (seq_dict['alen_slen'] >= 0.3) and bsseq.mitochondrial) or (seq_dict['loc']=="M"):
                    result_table.append(seq_dict)
    write_list_of_dicts(result_table, outpath, fieldnames=fieldnames)
    return outpath

def get_targetp_table(db_path, outpath, inlist):
    engine = create_engine(db_path)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    seqs = session.query(Sequence)
    fieldnames = ['seqid', 'og', 'b2go_mito', 'loc', 'locrate', 'function', 'subj_id', 'subj_og', 'organism', 'subj_function', 'evalue', 'alen_slen', 'pident', 'rev_evalue', 'rev_pident', 'rev_alen_qlen', 'is_best?', 'best_rev_evalue', 'best_rev_pident']
    default_seq_dict = {}
    for name in fieldnames:
        default_seq_dict[name] = ''
    result_table = []
    i = 0
    for seq in seqs:
        if seq.organism == 'Euglena gracilis' and seq.loc == 'M' and seq.locrate == 1 and seq.seqid not in inlist:
            i+=1
            print i

            seq_dict = default_seq_dict.copy()
            seq_dict['seqid'] = seq.seqid
            seq_dict['og'] = seq.og
            seq_dict['b2go_mito'] = seq.mitochondrial
            seq_dict['loc'] = seq.loc
            seq_dict['locrate'] = seq.locrate
            seq_dict['function'] = seq.function

            bs = seq.best_subject()
            if bs:
                bsseq = bs['sequence']
                seq_dict['subj_id'] = bsseq.seqid
                seq_dict['subj_og'] = bsseq.og
                seq_dict['organism'] = bsseq.organism
                seq_dict['subj_function'] = bsseq.function

                bsh = bs['hit']
                seq_dict['evalue'] = bsh.evalue
                seq_dict['alen_slen'] = bsh.alen_slen
                seq_dict['pident'] = bsh.extra_data['pident']
                reverse_hit = seq.get_reverse_blasthit(bsseq)

                if reverse_hit:
                    seq_dict['rev_evalue'] = reverse_hit['hit'].evalue
                    seq_dict['rev_alen_qlen'] = reverse_hit['hit'].alen_qlen
                    seq_dict['rev_pident'] = reverse_hit['hit'].extra_data['pident']
                    seq_dict['is_best?'] = reverse_hit['is_best']
                    seq_dict['best_rev_evalue'] = reverse_hit['bsh'].evalue
                    seq_dict['best_rev_pident'] = reverse_hit['bsh'].extra_data['pident']
                    seq_dict['best_rev_pident'] = reverse_hit['bsh'].extra_data['pident']
            result_table.append(seq_dict)
            fieldnames = []
            default_seq_dict = {}
    write_list_of_dicts(result_table, outpath, fieldnames=fieldnames)
    return outpath

def get_idlist_table(db_path, outpath, idlist):
    engine = create_engine(db_path)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    seqs = session.query(Sequence).filter(Sequence.seqid.in_(idlist)).all()
    fieldnames = ['seqid', 'og', 'b2go_mito', 'loc', 'locrate', 'function', 'subj_id', 'subj_og', 'organism', 'subj_function', 'evalue', 'alen_slen', 'pident', 'rev_evalue', 'rev_pident', 'rev_alen_qlen', 'is_best?', 'best_rev_evalue', 'best_rev_pident']
    default_seq_dict = {}
    for name in fieldnames:
        default_seq_dict[name] = ''
    result_table = []
    i = 0
    for seq in seqs:
        i+=1
        print i
        seq_dict = default_seq_dict.copy()
        seq_dict['seqid'] = seq.seqid
        seq_dict['og'] = seq.og
        seq_dict['b2go_mito'] = seq.mitochondrial
        seq_dict['loc'] = seq.loc
        seq_dict['locrate'] = seq.locrate
        seq_dict['function'] = seq.function

        bs = seq.best_subject()
        if bs:
            bsseq = bs['sequence']
            seq_dict['subj_id'] = bsseq.seqid
            seq_dict['subj_og'] = bsseq.og
            seq_dict['organism'] = bsseq.organism
            seq_dict['subj_function'] = bsseq.function

            bsh = bs['hit']
            seq_dict['evalue'] = bsh.evalue
            seq_dict['alen_slen'] = bsh.alen_slen
            seq_dict['pident'] = bsh.extra_data['pident']
            reverse_hit = seq.get_reverse_blasthit(bsseq)

            if reverse_hit:
                seq_dict['rev_evalue'] = reverse_hit['hit'].evalue
                seq_dict['rev_alen_qlen'] = reverse_hit['hit'].alen_qlen
                seq_dict['rev_pident'] = reverse_hit['hit'].extra_data['pident']
                seq_dict['is_best?'] = reverse_hit['is_best']
                seq_dict['best_rev_evalue'] = reverse_hit['bsh'].evalue
                seq_dict['best_rev_pident'] = reverse_hit['bsh'].extra_data['pident']
                seq_dict['best_rev_pident'] = reverse_hit['bsh'].extra_data['pident']
        result_table.append(seq_dict)
    write_list_of_dicts(result_table, outpath, fieldnames=fieldnames)
    return outpath

def get_id_table(db_path, outpath, id):
    engine = create_engine(db_path)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    seq = session.query(Sequence).filter(Sequence.seqid == id).one()
    query_blasthits = seq.query_blasthits
    subject_blasthits = seq.subject_blasthits
    result_table = []
    fieldnames = ['query_id', 'subject_id', 'evalue', 'length', 'alen_qlen', 'alen_slen', 'slen', 'qlen', 'pident']
    for bhs in query_blasthits, subject_blasthits:
        for bh in bhs:
            seq_dict = {}
            seq_dict['query_id'] = bh.query_id
            seq_dict['subject_id'] = bh.subject_id
            seq_dict['evalue'] = bh.evalue
            seq_dict['length'] = bh.length
            seq_dict['alen_qlen'] = bh.alen_qlen
            seq_dict['alen_slen'] = bh.alen_slen
            seq_dict['slen'] = bh.slen
            seq_dict['qlen'] = bh.qlen
            seq_dict['pident'] = bh.extra_data['pident']
            result_table.append(seq_dict)
    write_list_of_dicts(result_table, outpath, fieldnames=fieldnames)
    return outpath


db_path = 'sqlite:////home/anna/Dropbox/phd/mitoproteomes/db/perkinsela_mito.db'
# db_path = 'sqlite:////home/nenarokova/mito_all.db'
# db_path = 'sqlite:////home/anna/Dropbox/phd/db/mito1.db'
# db_path = 'sqlite:////home/nenarokova/mito_all.db'
# db_path = 'sqlite:////home/nenarokova/db/hemistasia_mito.db'

# outpath = '/home/nenarokova/result_all_proteomes.csv'
# outpath = '/home/anna/Dropbox/phd/db/result_test.csv'
# outpath = '/home/nenarokova/db/result_hemistasia.csv'
outpath = '/home/anna/Dropbox/phd/mitoproteomes/perkinsela_mito.csv'

id_list = ["EG_transcript_10773","EG_transcript_11225","EG_transcript_12497","EG_transcript_13899","EG_transcript_13947","EG_transcript_15660","EG_transcript_1590","EG_transcript_17752","EG_transcript_21706","EG_transcript_22111","EG_transcript_22381","EG_transcript_3480","EG_transcript_35473","EG_transcript_37041","EG_transcript_43895","EG_transcript_47790","EG_transcript_57369","EG_transcript_60280","EG_transcript_7573","EG_transcript_7601","EG_transcript_8364","EG_transcript_9333",]
# get_idlist_table(db_path, outpath, idlist = id_list)
get_result_table_perk(db_path, outpath)