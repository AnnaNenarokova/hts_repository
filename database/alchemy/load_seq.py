#!/usr/bin/python
from Bio import SeqIO
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.alchemy.models import *
from py_scripts.common_helpers.make_outdir import *
from py_scripts.common_helpers.parse_csv import *

def load_fasta(session, fasta_path, seqtype, organism='unknown organism', source=False, description_path=False):
    if description_path:
        dict_of_functions = csv_to_dict(description_path, main_key='seqid')
    for record in SeqIO.parse(fasta_path, "fasta"):
        seqid = record.id
        if not source: source = file_from_path(fasta_path, endcut=6)
        new_seq = Sequence(seqid=seqid, seqtype=seqtype, organism=organism, source=source, extra_data={})
        new_seq.extra_data['sequence'] = str(record.seq)
        new_seq.extra_data['description'] = str(record.description)

        if description_path:
            cur_dic = dict_of_functions[seqid]
            new_seq.function = cur_dic['function']
            new_seq.og = cur_dic['og']
            if cur_dic['mitochondrial'] == 'yes': new_seq.mitochondrial=True
            elif cur_dic['mitochondrial'] == 'no': new_seq.mitochondrial=False
            else:
                print "Error in field 'mitochondrial', seqid", seqid
                sys.exit(1)
        session.add(new_seq)
    session.commit()
    return 0

def load_ogs(session, ogs_path):
    return 0