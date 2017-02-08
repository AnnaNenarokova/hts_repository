#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from py_scripts.helpers.parse_csv import *
from Bio import SeqIO

nt_fasta_path = '/home/anna/Dropbox/PhD/bioinformatics/trypanosomatids/blasto/transcriptome/Trinity-GG_p57.fasta'
blast_csv_path = '/home/anna/Dropbox/PhD/bioinformatics/trypanosomatids/blasto/transcriptome/all_bh_0_e_format_best.csv'
outpath = blast_csv_path[:-4]+"_4.fna"

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

nt_records = SeqIO.parse(nt_fasta_path, 'fasta')
results = []
blast_hits = parse_csv(blast_csv_path)
for record in nt_records:
    for bh in blast_hits:
        query_id = bh[0]
        if query_id != "qseqid":
            nt_id = query_id[:-2]
            frame = int(query_id[-1])
            aa_start = int(bh[10])
            aa_end = int(bh[11])
            if record.id == nt_id:
                cds = back_translate(record, frame, aa_start, aa_end, add_nt=4)
                results.append(cds)
                # if len(cds.seq)%3!= 0:
                    # print "Len error", record.id
SeqIO.write(results, outpath, "fasta")




