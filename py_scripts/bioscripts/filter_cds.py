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
    outpath_filtered = infasta_path[:-6]+"_filtered.fasta"
    outpath_incorrect = infasta_path[:-6]+"_incorrect.fasta"
    outpath_truncated = infasta_path[:-6]+"_truncated.fasta"
    filtered_proteins = []
    incorrect_proteins = []
    truncated_proteins = []
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
                filtered_proteins.append(record)
            else:
                truncated_proteins.append(record)

    SeqIO.write(filtered_proteins, outpath_filtered, "fasta")
    SeqIO.write(incorrect_proteins, outpath_incorrect, "fasta")
    SeqIO.write(truncated_proteins, outpath_truncated, "fasta")
    print "filtered proteins", len(filtered_proteins)
    print "incorrect proteins", len(incorrect_proteins)
    print "truncated proteins", len(truncated_proteins)
    return 0


def filter_cds(fasta_path, finish_included=True):
    result_correct = []
    result_incorrect = []
    for record in SeqIO.parse(fasta_path, "fasta"):
        seq = record.seq
        if ( len(seq) % 3 == 0 ):
            translated_cds = seq.translate()
        else:
            print "Error! Len % 3 not equal 0"

        if finish_included:
            result_seq = seq[:-3]
        else:
            result_seq = seq

        result_record = SeqRecord(result_seq, id=record.id, name=record.name, description=record.description)

        if cds_correct(translated_cds, finish_included=finish_included):
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

fasta_path = "/home/anna/bioinformatics/references/ncbi/filtered/GCA_000442575.2_Angomonas_deanei_Genome_protein.faa"
# fasta_path = sys.argv[1]
filter_proteins(fasta_path, finish_included = False, translated=True)
