#!/usr/bin/python
from Bio import SeqIO

l = [
"TBRUC_GLU_TTC",
"PCON_GLU_TTC",
"LBRAZ_GLU_TTC",
"CFAS_GLU_TTC",
"LPYR_GLU_TTC",
"BP57_GLU_TTC",
"BP57_STOP_TTA",
"BAYA_GLU_TTC",
"BAYA_GLU_CTC2",
"BAYA_GLU_CTC",
"BP57_GLU_CTC",
"LSEY_GLU_CTC3",
"LPYR_GLU_CTC",
"LPYR_GLU_CTC2",
"CFAS_GLU_CTC",
"LBRAZ_GLU_CTC",
"BP57_PYL_CTA",
"BAYA_ASP_GTC"
]

fasta = '/home/anna/Dropbox/PhD/bioinformatics/blasto/blastocrithidia/genes/tRNAs/trna_phylogeny_deduplicated.fna'
results = []

for record in SeqIO.parse(fasta, "fasta"):
    if record.id in l:
        results.append(record)

outpath = '/home/anna/Dropbox/PhD/bioinformatics/blasto/blastocrithidia/genes/tRNAs/trna_glu_dataset.fna'

SeqIO.write(results, outpath, "fasta")
