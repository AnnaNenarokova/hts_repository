#!/usr/bin/python
from Bio import SeqIO

fasta_files = [
"/home/anna/bioinformatics/biotools/TransDecoder-3.0.1/novymonas_no_pand_scaffolds.fasta.transdecoder_dir/stringtie_transcripts.fasta.transdecoder_dir/longest_orfs.pep"
]

for fasta_file in fasta_files:
    results = []
    outpath = fasta_file[:-2]+ "_complete_ORFs_100.fa"
    for record in SeqIO.parse(fasta_file, "fasta"):
        seq = record.seq
        if seq[0] == "M" and seq[-1] == "*" and len(seq) >= 100:
            results.append(record)
    SeqIO.write(results, outpath, "fasta")
