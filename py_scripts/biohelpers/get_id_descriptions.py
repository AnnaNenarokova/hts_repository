#!/usr/bin/python3
from Bio import SeqIO
import sys
sys.path.insert(0, "/Users/annanenarokova/work/code/ngs/")
sys.path.insert(0, "/home/users/nenarokova/ngs/")
from py_scripts.helpers.parse_csv import *
import re
from os import listdir

def write_ids(infasta, out_csv_path):
    results=[["seqid", "description"]]
    species_regex = re.compile(r" \[.*\]$")
    i = 0
    for record in SeqIO.parse(infasta, "fasta"):
        i+=1
        if i % 100000 == 0: print (i)
        seqid = record.id
        description = record.description
        id_regex = re.compile(rf"^{seqid} ")
        description_no_ids = id_regex.sub("", description)
        description_no_species = species_regex.sub("", description_no_ids)
        results.append([seqid, description_no_species])
    write_list_of_lists(results, out_csv_path, delimiter='\t')
    return 0

infasta_folder = "/Users/annanenarokova/work/hypsa_local/jana_m/ref_proteomes/polyplax_ref_proteomes/"
out_csv_folder = "/Users/annanenarokova/work/hypsa_local/jana_m/ref_proteomes/proteomes_info/"

for infasta in listdir(infasta_folder):
    name = infasta[:-4]
    print (infasta)
    out_csv_path = out_csv_folder + name + ".tsv"
    write_ids(infasta_path, out_csv_path)
