#!python3
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"

input_path = "/home/vl18625/bioinformatics/diplonema/refdataset/ready_tables/euk_sps_list.csv"
output_path = "/home/vl18625/bioinformatics/diplonema/refdataset/ready_tables/euk_sps_list_taxids.csv"
delimiter = ","
species_n_column = 1
with open(input_path) as input_f, open(output_path,"w") as output_f:
    i = 0
    for line in input_f:
        i += 1
        print (i)
        line_split = line.rstrip().split(delimiter)
        species_name = line_split[species_n_column - 1]
        entrez_handle = Entrez.esearch(db="taxonomy",retmax=10,term=species_name)
        data_parsed = Entrez.read(entrez_handle)
        taxid = "#N/A"
        if ("ErrorList" not in data_parsed.keys() and data_parsed["Count"] == "1"):
            taxid = data_parsed["IdList"][0]
        outline = line[:-1] + delimiter + taxid + "\n"
        output_f.write(outline)