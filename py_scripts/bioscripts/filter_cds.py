#!/usr/bin/python
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import sys

def filter_cds(fasta_path):
    non_truncated = 0
    truncated = 0
    has_stops = 0
    result = []
    result_stops = []
    for record in SeqIO.parse(fasta_path, "fasta"):
        if len(record.seq) % 3 == 0:
            translated_seq = record.seq.translate()
            if (translated_seq[0] == 'M') and (translated_seq[-1] == '*'):
                non_truncated += 1
                result_seq = translated_seq[:-1]
                result_record = SeqRecord(result_seq, id=record.id, name=record.name, description=record.description)
                if "*" in result_seq:
                    has_stops += 1
                    result_stops.append(result_record)
                else:
                    result.append(result_record)
            else:
                truncated += 1
        else:
            truncated += 1
    outpath = fasta_path[:-6]+"_filtered.faa"
    SeqIO.write(result, outpath, "fasta")
    outpath_stops = fasta_path[:-6]+"_inframe_stops.faa"
    SeqIO.write(result_stops, outpath_stops, "fasta")

    print fasta_path
    print "non truncated genes", non_truncated
    print "truncated genes", truncated
    print "genes with in-frame stop codons", has_stops
    return 0

fasta_path = sys.argv[1]
filter_cds(fasta_path)
