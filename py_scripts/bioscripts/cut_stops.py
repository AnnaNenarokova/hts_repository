#!/usr/bin/python
from Bio import SeqIO
inpath = "/home/anna/bioinformatics/all_tryp_references/cds/TriTrypDB-34_TbruceiTREU927_AnnotatedCDSs.fasta"
outpath = inpath[:-6]+"_without_stops.fna"
result = []
for record in SeqIO.parse(inpath, "fasta"):
    result_record = record[0:-3]
    if "pseudogenic_transcript" not in record.id:
        result.append(result_record)
SeqIO.write(result, outpath, "fasta")
