#!/usr/bin/python
import sys
sys.path.insert(0, "/Users/annanenarokova/work/code/ngs/")
sys.path.insert(0, "/home/users/nenarokova/ngs/")
from py_scripts.helpers.parse_csv import *

def read_og_counts(og_count_path, target_species):
    csv_dict = csv_to_dict(og_count_path, "Orthogroup", delimiter="\t")
    species_list = list(csv_dict["OG0000000"].keys())
    species_list.remove("Total")
    og_count_dict= {}
    for og in csv_dict:
        gene_count_dict = {}
        for species in species_list:
            gene_count_dict[species] = csv_dict[og][species]
        og_count_dict[og] = gene_count_dict
    return og_count_dict

def check_og_target(gene_count_dict, target_species, duplication_threshold = 5):
    is_duplicated = False
    max_gene_number = 0
    target_species_gene_number = int(gene_count_dict[target_species])
    del gene_count_dict[target_species]

    for species in gene_count_dict:
        species_gene_number = int(gene_count_dict[species])
        if species_gene_number > max_gene_number:
            max_gene_number = species_gene_number
    if target_species_gene_number > 0 and max_gene_number > 0:
        if (target_species_gene_number / max_gene_number) > duplication_threshold:
            is_duplicated = True
    return is_duplicated

def write_duplicated_ogs_target(og_count_dict, target_species, outpath):
    duplicated_ogs = []
    for og in og_count_dict:
        if check_if_duplicated_target(og_count_dict[og], target_species):
            duplicated_ogs.append(og)
    with open(outpath, "w") as outfile:
        for og in duplicated_ogs:
            outfile.write(og + "\n")
    return duplicated_ogs

def check_og_group(gene_count_dict, target_list, ref_list, duplication_threshold = 5):
    result = ""

    max_gene_number_target = 0
    for species in target_list:
        species_gene_number = int(gene_count_dict[species])
        if species_gene_number > max_gene_number_target:
            max_gene_number_target = species_gene_number

    max_gene_number_ref = 0
    for species in ref_list:
        species_gene_number = int(gene_count_dict[species])
        if species_gene_number > max_gene_number_ref:
            max_gene_number_ref = species_gene_number

    if max_gene_number_target == 0:
        result = "not found"
    elif max_gene_number_ref == 0:
        result = "unique"
    elif (max_gene_number_target / max_gene_number_ref) > duplication_threshold:
        result = "duplicated"
    else:
        result = "not duplicated"

    return result

def analyse_ogs(og_count_path, target_list, ref_list, target_species):
    og_count_dict = read_og_counts(og_count_path, target_species)

    single_target_list = [target_species]
    ref_single_target_set = set(target_list) - set(single_target_list)
    ref_single_target_set.update(set(ref_list))
    ref_single_target_list = list(ref_single_target_set)

    og_result_dict = {}

    for og in og_count_dict:
        og_result_dict[og] = {}
        gene_count_dict = og_count_dict[og]

        result_group = check_og_group(gene_count_dict, target_list, ref_list)
        result_single = check_og_group(gene_count_dict, single_target_list, ref_single_target_list)

        og_result_dict[og]["result_single"] = result_single
        og_result_dict[og]["result_group"] = result_group
    return og_result_dict


og_count_path = "/Users/annanenarokova/work/myxo_local/Orthogroups.GeneCount.tsv"

outpath = "/Users/annanenarokova/work/myxo_local/ogs_duplicated_analysis.tsv"

target_species = 'Sphaerospora_molnari'
target_list = ["Ceratonova_shasta","Henneguya_salminicola","Kudoa_iwatai","Myxidium_liberkuehni","Myxobolus_squamalis","Polypodium_hydriforme","Sphaerospora_molnari","Tetracapsuloides_bryosalmonae","Thelohanellus_kitauei"]
ref_list = ["Acropora_millepora","Actinia_tenebrosa","Amphimedon_queenslandica", "Nematostella_vectensis","Orbicella_faveolata","Dendronephthya_gigantea","Exaiptasia_pallida","Hydra_vulgaris","Stylophora_pistillata","Pocillopora_damicornis"]

og_result_dict = analyse_ogs(og_count_path, target_list, ref_list, target_species)

write_dict_of_dicts(og_result_dict, outpath, key_name="Orthogroup")