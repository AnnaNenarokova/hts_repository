#!python3
from Bio import SeqIO
from Bio import Entrez

Entrez.email = "a.nenarokova@gmail.com"
diamond_result_path = "/projects/Diplonema_genome_evolution/hgt/hgt_nr_diamond_0e.tsv"
taxid_into_path = "/projects/Diplonema_genome_evolution/hgt/hgt_nr_diamond_0e_taxids.tsv"


with open diamond_result_path as diamond_f, open taxid_into_path as taxid_f:
    for line in diamond_f:
        line_split = line.rstrip().split("\t")
        query_id = line_split[0]
        subject_id = line_split[0]
        taxid_f.


handle = Entrez.efetch(db="protein", id="WP_014997480.1", rettype="fasta") 

