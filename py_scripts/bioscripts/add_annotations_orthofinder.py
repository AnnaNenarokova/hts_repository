#!/usr/bin/python
from os import listdir
import re
from Bio import SeqIO
import sys
sys.path.insert(0, "/Users/annanenarokova/work/code/ngs/")
sys.path.insert(0, "/home/users/nenarokova/ngs/")
from py_scripts.helpers.parse_csv import *

def read_annotations(fasta_folder):
    annotation_dict = {}
    for filename in listdir(fasta_folder):
        species = filename[:-4]
        annotation_dict[species] = {}
        fasta_path = fasta_folder + filename
        for record in SeqIO.parse(fasta_path, "fasta"):
            record_id = record.id
            record_annotation = record.description
            annotation_no_ids = record_annotation.replace(f"{record_id} ", "")
            species_regex = re.compile(r" \[.*\]$")
            annotation = species_regex.sub("", annotation_no_ids)
            annotation_dict[species][record_id] = annotation
    return annotation_dict

def add_annotations_orthogroups(annotation_dict, orthogroups_path):
    og_dict = csv_to_dict(orthogroups_path, "Orthogroup", delimiter='\t')
    for og in og_dict:
        for species in og_dict[og]:
            genes = og_dict[og][species]
            if genes:
                gene_ids = og_dict[og][species].split(", ")
                new_genes = []
                for gene_id in gene_ids:
                    annotation = annotation_dict[species][gene_id]
                    new_gene = gene_id + ": " + annotation
                    new_genes.append(new_gene)
                new_genes_string = "; ".join(new_genes)
                og_dict[og][species] = new_genes_string
    return og_dict

fasta_folder="/Users/annanenarokova/work/hypsa_local/jana_m/ref_proteomes/polyplax_ref_proteomes/"
orthogroups_path="/Users/annanenarokova/work/hypsa_local/jana_m/orthofinder/Orthogroups.tsv"
outpath="/Users/annanenarokova/work/hypsa_local/jana_m/orthofinder/orthogroups_annotations.tsv"

print ("Reading annotations from fasta files")
annotation_dict = read_annotations(fasta_folder)
print ("Adding annotations")
new_og_dict = add_annotations_orthogroups(annotation_dict, orthogroups_path)
print ("Writing the results")
write_dict_of_dicts(new_og_dict, outpath, key_name="Orthogroup")
