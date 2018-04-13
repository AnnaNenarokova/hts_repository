#!/usr/bin/python
from Bio import Entrez

def find_organism(id):
    search_handle = Entrez.esearch(db="protein", retmax=10, term=id)
    search_record = Entrez.read(search_handle)
    search_handle.close()
    find_count = int(search_record["Count"])
    #if find_count != 1: print (find_count, "records found for id", id)
    if find_count > 0:
        ncbi_id = search_record['IdList'][0]
        protein_handle = Entrez.efetch(db="protein", id=ncbi_id, retmode="xml")
        protein_record = Entrez.read(protein_handle)
        protein_handle.close()
        organism = protein_record[0]["GBSeq_organism"]
        return organism
    else:
        return ""

Entrez.email = "a.nenarokova@gmail.com"

# idlist_path = "D:/anna_drive/projects/ku70/apicomplexa_eggnog/api_nog_ids.txt"
idlist_path = "/home/nenarokova/api_nog_ids.txt"

# outpath = "D:/anna_drive/projects/ku70/apicomplexa_eggnog/api_nog_ids_ncbi_species.txt"
outpath = "/home/nenarokova/api_nog_ids_ncbi_species.txt"

with open(idlist_path) as idlist_file, open(outpath, "w") as outfile:
    for line in idlist_file:
        id = line.rstrip()
        organism = find_organism(id)
        # print (organism)
        outfile.write('{}\t{}'.format(id,organism))