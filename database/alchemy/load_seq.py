#!/usr/bin/python
from Bio import SeqIO
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.alchemy.models import *
from py_scripts.common_helpers.make_outdir import *

def load_fasta(session, fasta_path, seqtype, organism='unknown organism', source=False):
    for record in SeqIO.parse(fasta_path, "fasta"):
        seqid = record.id
        if not source: source = file_from_path(fasta_path, endcut=6)
        new_seq = Sequence(seqid=seqid, seqtype=seqtype, organism=organism, source=source, extra_data={}, mitoscore=mitoscore)
        new_seq.extra_data['sequence'] = str(record.seq)
        new_seq.extra_data['description'] = str(record.description)
        session.add(new_seq)
    session.commit()
    return 0

def load_functions(session, csv_path):
    return 0

def load_ogs(session, ogs_path):
    return 0