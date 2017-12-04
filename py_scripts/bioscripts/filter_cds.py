#!/usr/bin/python
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import sys

def check_start(translated_seq):
    if translated_seq[0] == "M":
        return True
    else:
        return False

def check_stops_inframe(translated_seq, stops=["*", "+", "$", "!"]):
    if any(stop in translated_seq for stop in stops):
        return False
    else:
        return True

def check_stops_inframe(translated_seq, stops=["*", "+", "$", "!"]):
    if any(stop in translated_seq for stop in stops):
        return False
    else:
        return True

def check_aa_symbols(translated_seq, aa_symbols="ACDEFGHIKLMNPQRSTVWYX"):
    for symbol in translated_seq:
        if symbol not in aa_symbols:
            return False
    return True

def check_finish(translated_seq, finish_included=True):
    if translated_seq[-1] == "*" or finish_included == False:
        return True
    else:
        return False

def check_protein(translated_seq, finish_included=True):
    if finish_included:
        finish_correct = check_finish(translated_seq)
    else:
        finish_correct = True
    if (finish_correct and check_start(translated_seq) and check_aa_symbols(translated_seq)):
        return True
    else:
        return False

def filter_proteins(infasta_path, translated=True, finish_included=True):
    print infasta_path
    outpath_incorrect = infasta_path[:-6]+"_incorrect.fasta"
    outpath_truncated = infasta_path[:-6]+"_truncated.fasta"
    outpath_x = infasta_path[:-6]+"_Xs.fasta"
    outpath_filtered = infasta_path[:-6]+"_filtered.fasta"
    incorrect_proteins = []
    truncated_proteins = []
    x_proteins = []
    filtered_proteins = []
    for record in SeqIO.parse(infasta_path, "fasta"):
        seq = record.seq
        truncated = False
        if not translated:
            if ( len(seq) % 3 == 0 ):
                seq = seq.translate()
            else:
                truncated = True
        if finish_included:
            orf = seq[:-1]
        else:
            orf = seq
        if not check_aa_symbols(orf):
            incorrect_proteins.append(record)
        else:
            if check_start(seq) and check_finish(seq, finish_included=finish_included) and not truncated:
                if "X" in seq:
                    x_proteins.append(record)
                else:
                    filtered_proteins.append(record)
            else:
                truncated_proteins.append(record)

    SeqIO.write(filtered_proteins, outpath_filtered, "fasta")
    SeqIO.write(incorrect_proteins, outpath_incorrect, "fasta")
    SeqIO.write(truncated_proteins, outpath_truncated, "fasta")
    print "incorrect proteins", len(incorrect_proteins)
    print "truncated proteins", len(truncated_proteins)
    print "proteins with Xs", len(x_proteins)
    print "filtered proteins", len(filtered_proteins)
    return 0

# fasta_path = sys.argv[1]
fasta_path = "/home/anna/bioinformatics/references/tritrypdb_references/tritrypdb_33/TriTrypDB-33_TbruceiTREU927_AnnotatedProteins.fasta"
filter_proteins(fasta_path, finish_included = False, translated=True)
