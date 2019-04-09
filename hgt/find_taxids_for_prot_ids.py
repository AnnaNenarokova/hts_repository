#!python3
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"

input_path = "/home/vl18625/bioinformatics/diplonema/hgt/seqnames_ncbi_nr.csv"
output_path = "/home/vl18625/bioinformatics/diplonema/hgt/seqnames_ncbi_nr_taxids.csv"
delimiter = ","
prot_id_column = 1
with open(input_path) as input_f, open(output_path,"w") as output_f:
    i = 0
    for line in input_f:
        i += 1
        print (i)
        line_split = line.rstrip().split(delimiter)
        prot_id = line_split[prot_id_column - 1]
        entrez_handle = Entrez.efetch(db="protein", id=prot_id, rettype="fasta", retmode="xml")
        data_parsed = Entrez.read(entrez_handle)
        taxid = "#N/A"
        taxid = data_parsed[0]['TSeq_taxid'] 
        outline = line[:-1] + delimiter + taxid + "\n"
        output_f.write(outline)