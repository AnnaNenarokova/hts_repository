#!/usr/bin/python
from Bio import SeqIO
from Bio.SeqUtils import GC

def count_total_gc(fasta):
    result_seq=""
    l=0
    for record in SeqIO.parse(fasta, "fasta"):
        result_seq+=record.seq
        l+=len(record.seq)
    print 'GC = ' + str(GC(result_seq))
    print 'length = ' + str(l)

def report_contig_gc(fasta, output_path):
    delimiter = ","
    with open(output_path,"w") as output_f:
        first_line = "id" + delimiter + "gc" + "\n"
        output_f.write(first_line)
        for record in SeqIO.parse(fasta, "fasta"):
            id = record.id
            gc = GC(record.seq)
            new_line = id + delimiter + str(gc) + "\n"
            output_f.write(new_line)

fasta="/home/anna/bioinformatics/novymonas/novymonas_no_pand_scaffolds.fasta"

output_path = "/home/anna/bioinformatics/novymonas/novymonas_no_pand_scaffolds_gc_report.fasta"

report_contig_gc(fasta, output_path)
