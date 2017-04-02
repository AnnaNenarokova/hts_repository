#!/usr/bin/python
from Bio import SeqIO

fasta_files = [
"/home/anna/bioinformatics/euglenozoa_anzhelika/Dataset_cd_hit_est_0_9/Ngruberi_GCF_000004985.1_V1.0_protein.fa"
]

for fasta_file in fasta_files:
    results = []
    outpath = fasta_file[:-2]+ "_complete_ORFs.fa"
    for record in SeqIO.parse(fasta_file, "fasta"):
        if record.seq[0] == "M":
            results.append(record)
    SeqIO.write(results, outpath, "fasta")
