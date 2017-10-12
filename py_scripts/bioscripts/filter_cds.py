#!/usr/bin/python
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import sys

def check_start(translated_seq):
    if translated_seq[0] == "M":
        return True
    else:
        return False

def check_inframe(translated_seq):
    if "*" in translated_seq:
        return False
    else:
        return True

def check_finish(translated_seq):
    if translated_seq[-1] == "*":
        return True
    else:
        return False

def cds_correct(translated_cds, stop_included=True):
    start_correct = check_start(translated_cds)
    if stop_included:
        inframe_correct = check_inframe(translated_cds[:-1])
        finish_correct = True
    else:
        inframe_correct = check_inframe(translated_cds)
        finish_correct = check_finish(translated_seq)

    if start_correct and inframe_correct and finish_correct:
        return True
    else:
        return False

def filter_cds(fasta_path, translated=False, translate=True, stop_included=True):
    result_correct = []
    result_incorrect = []
    for record in SeqIO.parse(fasta_path, "fasta"):
        seq = record.seq
        if translated:
            translated_cds = seq()
        elif ( len(seq) % 3 == 0 ):
            translated_cds = seq.translate()
        else:
            print "Error! Len % 3 not equal 0"

        if translate:
            if stop_included:
                result_seq = translated_cds[:-1]
            else:
                result_seq = translated_cds
        else:
            if stop_included:
                result_seq = seq[:-3]
            else:
                result_seq = seq

        result_record = SeqRecord(result_seq, id=record.id, name=record.name, description=record.description)

        if cds_correct(translated_cds, stop_included=stop_included):
            result_correct.append(result_record)
        else:
            result_incorrect.append(result_record)

    outpath_correct = fasta_path[:-6]+"_filtered.fna"
    SeqIO.write(result_correct, outpath_correct, "fasta")
    outpath_incorrect = fasta_path[:-6]+"_incorrect.fna"
    SeqIO.write(result_incorrect, outpath_incorrect, "fasta")

    correct = len(result_correct)
    incorrect = len(result_incorrect)

    print fasta_path
    print "correct genes", correct
    print "incorrect genes", incorrect
    return 0

# fasta_path = sys.argv[1]
# filter_cds(fasta_path)
fasta_path = "/home/anna/bioinformatics/all_tryp_references/cds/TriTrypDB-34_TbruceiTREU927_AnnotatedCDSs.fasta"
filter_cds(fasta_path, translated = False, translate = False)
