#!/usr/bin/python
from Bio import Entrez
from Bio import SeqIO

global EMAIL
EMAIL = 'a.nenarokova@gmail.com'

Entrez.email = EMAIL
query = 'NBS-LRR AND cds NOT BAC NOT PAC NOT scaffold NOT contig'
# query = "((Triticum[Organism]) OR (Aegilops[Organism])) AND (NBS OR RGA) AND cds NOT BAC NOT PAC NOT scaffold NOT contig"
handle = Entrez.esearch(db="nucleotide", term=query, retmax=1024)
record = Entrez.read(handle)

idlist = ",".join(record["IdList"])
result = Entrez.efetch(db="nuccore", id=idlist, rettype="fasta", retmode="text")
fasta = result.read()
# out_file = '/home/anna/bioinformatics/wheat/NBS_LRR_wheat.fasta'
out_file = '/home/nenarokova/wheat/NBS_LRR_all_plants.fasta'
out = open(out_file, 'w')
out.write(fasta)
out.close()