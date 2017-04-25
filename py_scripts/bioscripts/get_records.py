#!/usr/bin/python
from Bio import SeqIO

l = [
"NODE_28927_length_57_cov_4231.5",
"NODE_27739_length_58_cov_2806.67",
"NODE_23515_length_63_cov_2887",
"NODE_18227_length_73_cov_2403.94",
"NODE_17488_length_75_cov_7438.8",
"NODE_11954_length_93_cov_28",
"NODE_11911_length_93_cov_43.3947",
"NODE_11851_length_94_cov_2018.21",
"NODE_8741_length_108_cov_11.3396",
"NODE_8740_length_108_cov_8.49057",
"NODE_28926_length_57_cov_7771",
"NODE_9780_length_102_cov_12.766",
"NODE_19236_length_70_cov_94.6",
"NODE_18474_length_72_cov_117.118",
"NODE_6092_length_127_cov_24.5556",
"NODE_2204_length_379_cov_1341.47",
"NODE_5372_length_142_cov_24.4828",
"NODE_15841_length_79_cov_17.7917",
"NODE_8313_length_111_cov_3067.02",
"NODE_532_length_5205_cov_208.292",
"NODE_452_length_8935_cov_136.013",
"NODE_452_length_8935_cov_136.013",
"NODE_917_length_1653_cov_155.282"
]

fasta = '/home/anna/bioinformatics/blasto/p57_DNA_scaffolds.fa'
results = []

for record in SeqIO.parse(fasta, "fasta"):
    if record.id in l:
        results.append(record)

outpath = '/home/anna/bioinformatics/blasto/P57_all_SL_contigs.fa'

SeqIO.write(results, outpath, "fasta")

# n = 3000
# fasta = '/home/anna/bioinformatics/blasto/jaculum/jaculum_scaffolds.fasta'
# results = []
# i = 0
# for record in SeqIO.parse(fasta, "fasta"):
#     if i < n:
#         results.append(record)
#     i+=1

# outpath = '/home/anna/bioinformatics/blasto/jaculum/jaculum_first3000.fasta'

# SeqIO.write(results, outpath, "fasta")
