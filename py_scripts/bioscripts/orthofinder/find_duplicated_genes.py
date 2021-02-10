#!/usr/bin/python
import sys
sys.path.insert(0, "/Users/annanenarokova/work/code/ngs/")
sys.path.insert(0, "/home/users/nenarokova/ngs/")
from py_scripts.helpers.parse_csv import *

def read_og_file(og_path):
    GENE_DELIMETER = ", "
    og_dict = csv_to_dict(og_path, "Orthogroup", delimiter='\t')
    for og in og_dict:
        for species in og_dict[og]:
            og_dict[og][species] = og_dict[og][species].split(GENE_DELIMETER)
    return og_dict

def find_duplicated_genes(og_path, query_species_list):
    DUPLICATION_THRESHOLD = 10
    duplicated_genes_dict = {}
    og_dict = read_og_file(og_path)
    for og in og_dict:
        gene_dict = {}
        for species in og_dict[og]:
            gene_dict[species] = og_dict[og][species]

        max_genes = {"species" : "", "gene_number" : 0}
        for species in gene_dict:
            current_gene_number = len(gene_dict[species])
            if current_gene_number > max_genes["gene_number"]:
                max_genes["species"] = species
                max_genes["gene_number"] = current_gene_number

        if max_genes["species"] in query_species_list:
            og_not_unique = False
            og_passes_threshold = True
            for species in gene_dict:
                gene_number = len(gene_dict[species])
                if species not in query_species_list:
                    if gene_number > 0:
                        og_not_unique = True
                    if (max_genes["gene_number"] / gene_number) < DUPLICATION_THRESHOLD:
                        og_passes_threshold = False
                        break
            if og_passes_threshold and og_not_unique:
                duplicated_genes_dict[og] = gene_dict

    return duplicated_genes_dict

def write_dupl_gene_list(duplicated_genes_dict, outpath, target_species):
    duplicated_genes = []
    for og in duplicated_genes_dict:
        duplicated_genes.extend(duplicated_genes_dict[og][target_species])

    with open(outpath, 'w') as outf:
        for gene in duplicated_genes:
            outf.write("%s\n" % gene)

    return duplicated_genes

og_path = "/Users/annanenarokova/Google Drive/projects/myxozoans/Orthogroups_no_Smol_tr.txt"
outpath = "/Users/annanenarokova/Google Drive/projects/myxozoans/duplicated_genes.txt"


species_list = ['Sphaerospora_molnari_G', 'Buddenbrockia_plumatellae_EST','Ceratonova_shasta_T','Henneguya_salminicola','Henneguya_salminicola_G','Kudoa_iwatai_G','Kudoa_iwatai_T','Myxidium_liberkuehni_T','Myxobolus_squamalis_G','Myxobolus_squamalis_T','Sphaerospora_molnari_G','Sphaerospora_molnari_T','Tetracapsuloides_bryosalmonae_EST','Tetracapsuloides_bryosalmonae_br_T','Tetracapsuloides_bryosalmonae_fish_T','Tetracapsuloides_bryosalmonae_intersect_T','Thelohanellus_kitauei_G']
target_species = 'Sphaerospora_molnari_G'

duplicated_genes_dict = find_duplicated_genes(og_path, species_list)

write_dupl_gene_list(duplicated_genes_dict, outpath, target_species)






