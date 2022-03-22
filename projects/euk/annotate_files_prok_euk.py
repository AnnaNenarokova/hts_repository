#!/usr/bin/python3
from ete3 import Tree
from Bio import SeqIO
import csv
from os import listdir
import sys
sys.path.insert(0, "/Users/anna/work/code/ngs/")
from py_scripts.helpers.parse_csv import *

def listdir_nohidden(path):
    for f in listdir(path):
        if not f.startswith('.'):
            yield f

def prepare_euk_info(fasta_folder):
    annotation_dict = {}
    for filename in listdir_nohidden(fasta_folder):
        print (filename)
        fasta_path = fasta_folder + filename
        for record in SeqIO.parse(fasta_path, "fasta"):
            record_id = record.id
            prot_id = record_id.split("|")[1]
            annotation = record.description
            annotation_dict[prot_id]= annotation
    return annotation_dict

def annotate_tree(tree, prok_info_dict, euk_info_dict):
    used_names = []
    for leaf in tree.iter_leaves():
        old_name = leaf.name
        id = old_name
        if id in prok_info_dict.keys():
            id_dict = prok_info_dict[id]
            new_name = '_'.join([id, id_dict['Domain'], id_dict['Phylum'], id_dict['Class'], id_dict['Order']])
        elif id in euk_info_dict.keys():
            new_name = euk_info_dict[id]
        else:
            print(id, "was not found in any dicts!")
            new_name = old_name
        if new_name in used_names:
            print (id, "is duplicated!")
            return (1)
        leaf.name = new_name
        used_names.append(new_name)
    return tree

def annotate_msa(infasta_path, outfasta_path, prok_info_dict, euk_info_dict):
    with open(infasta_path) as infasta, open(outfasta_path, "w") as outfasta:
        lines = infasta.readlines()
        for line in lines:
            if line[0] == ">":
                id = line.rstrip()[1::]
                if id in prok_info_dict.keys():
                    id_dict = prok_info_dict[id]
                    description = '_'.join([id, id_dict['Domain'], id_dict['Phylum'], id_dict['Class'], id_dict['Order']])
                elif id in euk_info_dict.keys():
                    description = euk_info_dict[id]
                else:
                    print(id, "was not found in any dicts!")
                    description = ""
                new_line = ">" + id + " " + description + "\n"
            else:
                new_line = line
            outfasta.write(new_line)
    return outfasta_path

def annotate_trees(in_treedir, out_treedir, prok_info_path, euk_fasta_folder):
    prok_info_dict = csv_to_dict(prok_info_path, main_key="id", delimiter=',')
    euk_info_dict = prepare_euk_info(euk_fasta_folder)
    for tree_file in listdir_nohidden(in_treedir):
        tree_path = in_treedir + tree_file
        tree = Tree(tree_path)
        new_tree = annotate_tree(tree, prok_info_dict, euk_info_dict)
        new_tree_path = out_treedir + tree_file
        tree.write(format=2, outfile=new_tree_path)
    return 0

def annotate_msas(in_dir, out_dir, prok_info_path, euk_fasta_folder):
    prok_info_dict = csv_to_dict(prok_info_path, main_key="id", delimiter=',')
    euk_info_dict = prepare_euk_info(euk_fasta_folder)
    for fasta_file in listdir_nohidden(in_dir):
        infasta_path = in_dir + fasta_file
        outfasta_path = out_dir + fasta_file
        annotate_msa(infasta_path, outfasta_path, prok_info_dict, euk_info_dict)
    return 0


in_treedir="/Users/anna/work/euk_local/elife_markers/trees/alphabac_tests/constrained_trees/"
out_treedir="/Users/anna/work/euk_local/elife_markers/trees/alphabac_tests/annotated_constrained_trees/"

prok_info_path="/Users/anna/work/euk_local/elife_markers/S3_700ArcBac_species_list.csv"
euk_fasta_folder="/Users/anna/work/euk_local/uniprot_proteomes/original_fastas/"

annotate_trees(in_treedir, out_treedir, prok_info_path, euk_fasta_folder)

# infasta_dir="/Users/anna/work/euk_local/elife_markers/fasta_with_euks/aligned_trimmed/"
# outfasta_dir="/Users/anna/work/euk_local/elife_markers/fasta_with_euks/al_trimmed_annotated/"
# annotate_msas(infasta_dir, outfasta_dir, prok_info_path, euk_fasta_folder)