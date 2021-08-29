#!/usr/bin/python3
import re
import sys
import csv
from Bio import SeqIO
from os import listdir

def dict_list_to_csv_dict(dict_list, main_key):
    csv_dict = {}
    for dic in dict_list:
        key = dic[main_key]
        csv_dict[key] = {}
        for k in dic:
            if not k == main_key:
                csv_dict[key][k] = dic[k]
    return csv_dict

def csv_to_list_of_dicts(csv_path, delimiter=',', fieldnames=None):
    with open(csv_path) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter=delimiter)
        list_of_dicts = []
        for row in reader:
            list_of_dicts.append(row)
        csvfile.close
    return list_of_dicts

def csv_to_dict(csv_path, main_key, delimiter=','):
    list_of_dicts = csv_to_list_of_dicts(csv_path, delimiter=delimiter)
    csv_dict = dict_list_to_csv_dict(list_of_dicts, main_key)
    return csv_dict

def write_list_of_dicts(list_of_dicts, outpath, fieldnames=False):
    with open(outpath, 'w') as csvfile:
        if not fieldnames:
            fieldnames = list_of_dicts[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in list_of_dicts:
            writer.writerow(row)
        csvfile.close()
    return outpath

def write_dict_of_dicts(dict_of_dicts, outpath, key_name=False, fieldnames=False):
    list_of_dicts = []
    for key in dict_of_dicts:
        cur_dict = {}
        cur_dict[key_name] = key
        for k in dict_of_dicts[key]:
            cur_dict[k] = dict_of_dicts[key][k]
        list_of_dicts.append(cur_dict)
    write_list_of_dicts(list_of_dicts, outpath, fieldnames)
    return outpath

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

fasta_folder="/mnt/data/martij04/Poly_Genome_annotation/orthofinder/polyplax_ref_proteomes/"
orthogroups_path="/mnt/data/martij04/Poly_Genome_annotation/orthofinder/orthofinder_out/Results_Aug09/Orthogroups/Orthogroups.tsv"
outpath = orthogroups_path[:-4] + "_annotations.tsv"

print ("Reading annotations from fasta files")
annotation_dict = read_annotations(fasta_folder)
print ("Adding annotations")
new_og_dict = add_annotations_orthogroups(annotation_dict, orthogroups_path)
print ("Writing the results")
write_dict_of_dicts(new_og_dict, outpath, key_name="Orthogroup")
