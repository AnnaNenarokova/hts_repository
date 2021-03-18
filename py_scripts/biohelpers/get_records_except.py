#!/usr/bin/python
from Bio import SeqIO

l = [
"NODE_2_length_844906_cov_870.704",
"NODE_822_length_1318_cov_1863.76",
"NODE_346_length_5920_cov_1555.3",
"NODE_121_length_88224_cov_845.318",
"NODE_106_length_108046_cov_858.69",
"NODE_104_length_108845_cov_889.343"
]
results = []

# for record in SeqIO.parse(fasta, "fasta"):
#   if record.id not in l:
#     results.append(record)



fasta = "/home/anna/bioinformatics/references/ncbi/GCA_000982615.1_AKI_PRJEB1539_v1_Phytomonas_Hart1_protein.faa"
outpath = "/home/anna/bioinformatics/references/ncbi/GCA_000982615.1_AKI_PRJEB1539_v1_Phytomonas_Hart1_full_proteins.faa"
for record in SeqIO.parse(fasta, "fasta"):
  if "partial" not in record.description:
    results.append(record)

SeqIO.write(results, outpath, "fasta")
