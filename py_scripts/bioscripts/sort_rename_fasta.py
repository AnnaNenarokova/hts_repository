#!/usr/bin/python
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import sys

def rename_sort(fasta_path, outpath):
    records = []
    rename_dict = {"Jac_":"00_Jac_","Bp57":"01_Bp57","Btri":"02_Btri","Bexl":"03_Bexl"}

    for record in SeqIO.parse(fasta_path, "fasta"):
        in_id = record.id
        sp_code = in_id[0:4]
        if sp_code in rename_dict.keys():
            out_id = rename_dict[sp_code] + in_id[4::]
            record.id = out_id
        records.append(record)
    result = sorted(records, key=lambda record: record.id)
    SeqIO.write(result, open(outpath, 'w'), "fasta")
    return 0

#fasta_path = "/home/anna/bioinformatics/tryps_algs/alignments/OG0002170.marker001.OG0002170_replaced.fa.aln"
fasta_path = sys.argv[1]

outpath = fasta_path + ".sorted"

rename_sort(fasta_path, outpath)

