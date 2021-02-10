#!/usr/bin/python
import sys
sys.path.insert(0, "/Users/annanenarokova/work/code/ngs/")
sys.path.insert(0, "/home/users/nenarokova/ngs/")
from py_scripts.helpers.parse_csv import *
from Bio import SeqIO

def back_translate(nt_seq, frame, aa_start, aa_end, add_nt=0):
    if frame in (1, 2, 3):
        nt_start = (aa_start-1) * 3 + (frame-1)
        nt_end = aa_end * 3 + (frame-1) + add_nt
        outseq = nt_seq[nt_start:nt_end]
        return outseq
    elif frame in (4, 5, 6):
        outseq = nt_seq.reverse_complement()
        nt_start = (aa_start-1) * 3 + (frame-4)
        nt_end = aa_end * 3 + (frame-4) + add_nt
        outseq = outseq[nt_start:nt_end]
        return outseq
    else:
        print "Error in frame"
        return 1

def cds_from_query(blast_hits, nt_records, add_nt=0):
    results = []
    for record in nt_records:
        for bh in blast_hits:
            query_id = bh[0]
            if query_id != "qseqid":
                nt_id = query_id[:-2]
                frame = int(query_id[-1])
                aa_start = int(bh[10])
                aa_end = int(bh[11])
                if record.id == nt_id:
                    cds = back_translate(record, frame, aa_start, aa_end, add_nt=add_nt)
                    results.append(cds)
                    if len(cds.seq)%3!= 0:
                        print "Len error", record.id
    return results

def cds_from_subject(blast_hits, nt_records, add_nt=0):
    results = []
    for record in nt_records:
        for bh in blast_hits:
            subject_id = bh[2]
            if subject_id != "sseqid":
                nt_id = subject_id[:-2]
                frame = int(subject_id[-1])
                aa_start = int(bh[12])
                aa_end = int(bh[13])
                if record.id == nt_id:
                    cds = back_translate(record, frame, aa_start, aa_end, add_nt=add_nt)
                    results.append(cds)
                    if len(cds.seq)%3!= 0:
                        print "Len error", record.id
    return results

nt_fasta_path = '/home/anna/Dropbox/PhD/bioinformatics/blasto/p57_scaffolds.fa'
blast_csv_path = '/home/anna/Dropbox/PhD/bioinformatics/blasto/eIF3j/bl_eif3j.csv'
outpath = blast_csv_path[:-4]+"_4.fna"

nt_records = SeqIO.parse(nt_fasta_path, 'fasta')
blast_hits = parse_csv(blast_csv_path)

results = cds_from_subject(blast_hits, nt_records, add_nt=0)

SeqIO.write(results, outpath, "fasta")




