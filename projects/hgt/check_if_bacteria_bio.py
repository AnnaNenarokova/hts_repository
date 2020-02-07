#!python3
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"

with open(input_path) as input_f:
    for line in input_f:
        taxid = line.rstrip()
        entrez_handle = Entrez.efetch(db="taxonomy", id=taxid)
        is_bacteria = (data_parsed[0]["Lineage"].split("; ")[1] == "Bacteria")
        print taxid, is_bacteria
