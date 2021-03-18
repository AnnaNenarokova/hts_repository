#!/usr/bin/python


from Bio import SeqIO

records = SeqIO.parse("THIS_IS_YOUR_INPUT_FILE.fasta-2line")
count = SeqIO.write(records, "THIS_IS_YOUR_OUTPUT_FILE.fasta-2line", "fasta-2line")
