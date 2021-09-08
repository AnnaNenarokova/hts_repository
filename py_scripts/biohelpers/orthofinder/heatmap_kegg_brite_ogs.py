#!/usr/bin/python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.insert(0, "/Users/annanenarokova/work/code/ngs/")
sys.path.insert(0, "/home/users/nenarokova/ngs/")
from py_scripts.helpers.parse_csv import *

def make_heatmap_df_ogs_kegg(ogs_kegg_path, desired_kos_path, kegg_key="ko_BRITE", index_order=False):
    ogs_kegg_dict = csv_to_dict(ogs_kegg_path, "Orthogroup", delimiter='\t')
    for og in ogs_kegg_dict:
        ko_brite_split = (ogs_kegg_dict[og][kegg_key]).split(",")
        ogs_kegg_dict[og][kegg_key] = ko_brite_split
    ko_dict = csv_to_dict_simple(desired_kos_path, delimiter="\t")
    species_list = list(list(ogs_kegg_dict.values())[0].keys())
    species_list.remove(kegg_key)
    ko_heatmap_dict = {}
    for ko in ko_dict:
        ko_function = ko_dict[ko]
        ko_heatmap_dict[ko_function] = {}
        for species in species_list:
            ko_heatmap_dict[ko_function][species] = 0

    for og in ogs_kegg_dict:
        og_dict = ogs_kegg_dict[og]
        for ko in og_dict[kegg_key]:
            if ko in ko_dict:
                for species in species_list:
                    ko_function = ko_dict[ko]
                    ko_heatmap_dict[ko_function][species] += int(og_dict[species])

    heatmap_df = pd.DataFrame(ko_heatmap_dict)
    if index_order:
        heatmap_df = heatmap_df.reindex(index_order)
    heatmap_df = heatmap_df.transpose()
    return heatmap_df

ogs_kegg_path = "/Users/annanenarokova/work/myxo_local/orthofinder/old_orthofinder/Orthogroups.GeneCount.Brite.Removed.txt"
desired_kos_path = "/Users/annanenarokova/work/myxo_local/kegg_ko_brite.tsv"

#index_order = ["Sphaerospora_molnari","Myxidium_liberkuehni","Thelohanellus_kitauei","Henneguya_salminicola","Myxobolus_squamalis","Ceratonova_shasta","Kudoa_iwatai","Tetracapsuloides_bryosalmonae","Polypodium_hydriforme","Hydra_vulgaris","Actinia_tenebrosa","Exaiptasia_pallida","Nematostella_vectensis","Orbicella_faveolata","Pocillopora_damicornis","Stylophora_pistillata","Acropora_millepora", "Dendronephthya_gigantea", "Amphimedon_queenslandica"]
#index_order = ["Sphaerospora_molnari","Thelohanellus_kitauei","Henneguya_salminicola","Myxobolus_squamalis","Ceratonova_shasta","Kudoa_iwatai","Tetracapsuloides_bryosalmonae","Polypodium_hydriforme","Hydra_vulgaris","Actinia_tenebrosa","Exaiptasia_pallida","Nematostella_vectensis","Orbicella_faveolata","Pocillopora_damicornis","Stylophora_pistillata","Acropora_millepora", "Dendronephthya_gigantea", "Amphimedon_queenslandica"]
   
heatmap_df = make_heatmap_df_ogs_kegg(ogs_kegg_path, desired_kos_path, index_order=False)

fig = plt.figure(figsize=(12,12))
r = sns.heatmap(heatmap_df, cmap='BuPu')
r.set_title("Heatmap of KEGG BRITE functions")

plt.show()
