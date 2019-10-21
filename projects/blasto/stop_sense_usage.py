#!/usr/bin/python
from Bio import SeqIO
import os
import statistics
from Bio.SeqUtils import GC

def count_codon_usage(seq, codons):
    seq = seq.upper()
    seq_length = len(seq)
    if len(seq) % 3 != 0:
        print "Seqlen error"
    codon_usage = {}
    for codon in codons:
        codon_usage[codon]=0
    for i, k in enumerate(range(0, seq_length, 3)):
        codon = str(seq[k:k+3])
        if codon in codons:
            codon_usage[codon]+= 1
    return codon_usage

def count_cov_median (coords, bam_path):
    ex = "samtools depth -r '%s' %s | cut -f3" % (coords, bam_path)
    median = statistics.median([int(f) for f in os.popen(ex).read().strip().split("\n")])
    return median

fasta_path = "/media/anna/data/anna_drive/projects/blastocrithidia/blasto/annotation_og/p57_CDs.fna"
bam_path = "/media/anna/data/big_files/p57_DNA_bw2_sorted.bam"
codons = ['TGA', 'TAG', 'TAA', 'TGG', 'GAG', 'GAA']
outpath = fasta_path[:-4]+ "_stop_analysis.tsv"
delimeter="\t"
median = "n"

with open(outpath, 'w') as outfile:
    header = ['id', 'len', 'gc', 'median_cov']
    header.extend(codons)
    outfile.write(delimeter.join(header) + '\n')
    i = 0
    for record in SeqIO.parse(fasta_path, "fasta"):
        i+=1
        if i%100 == 0: print i
        result = []
        id = record.id
        seq = record.seq
        gc_content = GC(seq)
        seq_length = len(seq)
        # coords = id[:-3]
        coords = record.description.split(' ')[1][0:-3]
        # print coords
        median = count_cov_median(coords, bam_path)
        # print median
        codon_usage = count_codon_usage(seq, codons)
        codon_counts = [str(codon_usage[codon]) for codon in codons]
        result = [id, str(seq_length), str(gc_content), str(median)]
        result.extend(codon_counts)
        outfile.write(delimeter.join(result) + '\n')
    outfile.close()
