#!/usr/bin/python
from Bio import SeqIO

l = [
"NODE_1_length_844906_cov_871.097",
"NODE_62_length_108845_cov_889.51",
"NODE_65_length_108046_cov_859.19",
"NODE_95_length_88224_cov_845.745",
"NODE_700_length_5920_cov_1556.22",
"NODE_1304_length_1318_cov_1864.36",
"NODE_1110_length_1849_cov_675.416"
]
fasta = '/home/anna/Dropbox/PhD/bioinformatics/genomes/trypanosomatids/novymonas/wt_scaffolds.fa'
results = []

for record in SeqIO.parse(fasta, "fasta"):
    for id in l:
        if id == record.id:
            results.append(record)

outpath = '/home/anna/Dropbox/PhD/bioinformatics/genomes/trypanosomatids/novymonas/pandorea_final.fa'

SeqIO.write(results, outpath, "fasta")
