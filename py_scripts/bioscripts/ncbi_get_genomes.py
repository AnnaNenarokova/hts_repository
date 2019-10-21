#!python3
from Bio import SeqIO
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"

for species in species_dict:
    outpath = outdir + species + ".fna"
    with open(outpath, "a") as outfile:
        ncbi_id = species_dict[species]
        ncbi_record = Entrez.efetch(db="genome", id=ncbi_id, rettype="fasta").read()[:-1]
        outfile.write(ncbi_record)
