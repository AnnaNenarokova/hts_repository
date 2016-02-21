#!/usr/bin/python
from Bio import SeqIO
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.alchemy.models import *
from py_scripts.common_helpers.make_outdir import *
from py_scripts.common_helpers.parse_csv import *

def load_fasta(session, fasta_path, seqtype, organism='unknown organism', source=False):
    for record in SeqIO.parse(fasta_path, "fasta"):
        seqid = record.id
        if not source: source = file_from_path(fasta_path, endcut=6)
        new_seq = Sequence(seqid=seqid, seqtype=seqtype, organism=organism, source=source, extra_data={})
        new_seq.extra_data['sequence'] = str(record.seq)
        new_seq.extra_data['description'] = str(record.description)
        session.add(new_seq)
    session.commit()
    return 0

def load_functions(session, csv_path):
    for dic in csv_to_list_of_dicts(csv_path):
        seqid = dic['seqid']
        function = dic['function']

        if dic['mitochondrial'] == 'yes': mitochondrial = True
        elif dic['mitochondrial'] == 'no': mitochondrial = False
        else:
            print "Error in mitochondrial format"
            sys.exit(1)

        result = session.query(Sequence).filter(Sequence.seqid.like("%" + dic['seqid'] + "%"))
        cnt = result.count()
        print dic['seqid']
        if cnt == 0:
            print "Cannot find Sequence with seqid = " + dic['seqid']
            sys.exit(1)
        elif cnt > 1:
            print "Sequence with seqid = " + dic['seqid'] + " is ambigous"

    print "Everything is ok"
    return 0

def load_ogs(session, ogs_path):
    return 0