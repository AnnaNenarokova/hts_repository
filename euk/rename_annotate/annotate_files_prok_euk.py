#!python
from ete3 import Tree
from Bio import SeqIO
import sys
sys.path.insert(0, "/Users/anna/work/code/ngs/")
sys.path.insert(0, "/user/home/vl18625/code/ngs")
sys.path.insert(0, "/Users/vl18625/work/code/ngs/")
import re

from py_scripts.helpers.parse_csv import *
from euk.fasta_scripts.get_prot_annotations_uniprot import *

def read_list(list_path):
    result_list = []
    with open (list_path) as list_file:
        for line in list_file:
            result_list.append(line.rstrip())
    return result_list

def prepare_euk_info_uniprot(fasta_folder):
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

def prepare_euk_info_eukprot_keeplist(fasta_folder, keep_list):
    annotation_dict = {}
    for filename in listdir_nohidden(fasta_folder):
        print (filename)
        proteome_id = filename.split("_")[0]
        if proteome_id in keep_list:
            fasta_path = fasta_folder + filename
            for record in SeqIO.parse(fasta_path, "fasta"):
                record_id = record.id
                annotation = record.description
                annotation_dict[record_id]= annotation
    return annotation_dict


def annotate_msa_elife(infasta_path, outfasta_path, prok_info_dict, euk_info_dict):
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

def annotate_msa_only_prok_elife(infasta_path, outfasta_path, prok_info_dict):
    with open(infasta_path) as infasta, open(outfasta_path, "w") as outfasta:
        lines = infasta.readlines()
        for line in lines:
            if line[0] == ">":
                id = line.rstrip()[1::]
                if id in prok_info_dict.keys():
                    id_dict = prok_info_dict[id]
                    description = '_'.join([id, id_dict['Domain'], id_dict['Phylum'], id_dict['Class'], id_dict['Order']])
                    new_line = ">" + id + " " + description + "\n"
                else:
                    new_line = line
            else:
                new_line = line
            outfasta.write(new_line)
    return outfasta_path

def annotate_msas(in_dir, out_dir, prok_info_path, euk_fasta_folder):
    prok_info_dict = csv_to_dict(prok_info_path, main_key="id", delimiter=',')
    euk_info_dict = prepare_euk_info(euk_fasta_folder)
    for fasta_file in listdir_nohidden(in_dir):
        infasta_path = in_dir + fasta_file
        outfasta_path = out_dir + fasta_file
        annotate_msa(infasta_path, outfasta_path, prok_info_dict, euk_info_dict)
    return 0

def annotate_msas_only_prok(in_dir, out_dir, prok_info_path):
    prok_info_dict = csv_to_dict(prok_info_path, main_key="id", delimiter=',')
    for fasta_file in listdir_nohidden(in_dir):
        infasta_path = in_dir + fasta_file
        outfasta_path = out_dir + fasta_file
        annotate_msa_only_prok(infasta_path, outfasta_path, prok_info_dict)
    return 0

def annotate_msas_keep_list(in_dir, out_dir, prok_info_path, euk_fasta_folder, keep_list_path):
    keep_list = read_list(keep_list_path)
    print("Reading prokaryote info")
    prok_info_dict = csv_to_dict(prok_info_path, main_key="id", delimiter=',')
    print("Reading eukaryote info")
    euk_info_dict = prepare_euk_info_eukprot_keeplist(fasta_folder, keep_list)
    print("Annotating sequences")
    for fasta_file in listdir_nohidden(in_dir):
        infasta_path = in_dir + fasta_file
        outfasta_path = out_dir + fasta_file
        annotate_msa(infasta_path, outfasta_path, prok_info_dict, euk_info_dict)
    return 0

def annotate_tree_euk_elife(tree, prok_info_dict, euk_info_dict):
    used_names = []
    for leaf in tree.iter_leaves():
        old_name = leaf.name
        id = old_name
        if id in prok_info_dict.keys():
            id_dict = prok_info_dict[id]
            new_name = '_'.join([id, id_dict['Domain'], id_dict['Phylum'], id_dict['Class'], id_dict['Order']])
        elif id in euk_info_dict.keys():
            description = euk_info_dict[id]
            new_name = id + "\t" + description

        else:
            print(id, "was not found in any dicts!")
            new_name = old_name
        if new_name in used_names:
            print (id, "is duplicated!")
            return (1)
        leaf.name = new_name
        used_names.append(new_name)
    return tree

def annotate_tree_nina(tree, prok_info_dict, euk_info_dict):
    used_names = []
    for leaf in tree.iter_leaves():
        old_name = leaf.name
        id = old_name
        genome_id = id.split("-")[0]
        if genome_id in prok_info_dict.keys():
            new_name = prok_info_dict[genome_id] + "_" + old_name
        elif id in euk_info_dict.keys():
            description = euk_info_dict[id]
            new_name = id + "\t" + description
        else:
            print(id, genome_id, "were not found in any dicts!")
            new_name = old_name
        if new_name in used_names:
            print (id, "is duplicated!")
        leaf.name = new_name
        used_names.append(new_name)
    return tree

def annotate_trees_fasta_files(in_treedir, out_treedir, prok_info_path, euk_fasta_folder):
    prok_info_dict = csv_to_dict(prok_info_path, main_key="id", delimiter=',')
    euk_info_dict = prepare_euk_info(euk_fasta_folder)
    for tree_file in listdir_nohidden(in_treedir):
        tree_path = in_treedir + tree_file
        tree = Tree(tree_path)
        new_tree = annotate_tree(tree, prok_info_dict, euk_info_dict)
        new_tree_path = out_treedir + tree_file
        tree.write(format=2, outfile=new_tree_path)
    return 0

def annotate_trees_elife(in_treedir, out_treedir, prok_info_path, euk_info_path):
    print("Reading prokaryote info")
    prok_info_dict = csv_to_dict(prok_info_path, main_key="id", delimiter=',')
    print("Reading eukaryote info")
    euk_info_dict = csv_to_dict_simple(euk_info_path, delimiter='\t')
    print("Annotating sequences")
    for tree_file in listdir_nohidden(in_treedir):
        tree_path = in_treedir + tree_file
        tree = Tree(tree_path)
        new_tree = annotate_tree(tree, prok_info_dict, euk_info_dict)
        new_tree_path = out_treedir + tree_file
        tree.write(format=2, outfile=new_tree_path)
    return 0


def annotate_trees_nina(in_treedir, out_treedir, prok_info_path, euk_info_path):
    print("Reading prokaryote info")
    prok_info_dict = csv_to_dict_simple(prok_info_path, delimiter='\t')
    print("Reading eukaryote info")
    euk_info_dict = csv_to_dict_simple(euk_info_path, delimiter='\t')
    print("Annotating trees")
    for tree_file in listdir_nohidden(in_treedir):
        print (tree_file)
        tree_path = in_treedir + tree_file 
        new_tree_path = out_treedir + tree_file + ".tree"
        try: 
            tree = Tree(tree_path)
            new_tree = annotate_tree_nina(tree, prok_info_dict, euk_info_dict)
            tree.write(format=2, outfile=new_tree_path)
        except:
            print ("Error", tree_path, new_tree_path)
    return 0

def annotate_tree_tax_info(tree, tax_info_dict,key_name="taxonomy"):
    used_names = []
    for leaf in tree.iter_leaves():
        old_name = leaf.name
        genome_id = old_name
        if genome_id in tax_info_dict.keys():
            new_name = genome_id + "_" + tax_info_dict[genome_id][key_name]
        else:
            print(id, genome_id, "was not found in the dict!")
            new_name = old_name
        if new_name in used_names:
            print (id, "is duplicated!")
        leaf.name = new_name
        used_names.append(new_name)
    return tree

def annotate_tree_tax_info_prot_ids(tree, tax_info_dict,key_name="taxonomy", delimiter="-", euk_delimiter=False, source_euk_delimiter=False):
    used_names = []
    euk_regex = "^EP\d+_P\d+"
    for leaf in tree.iter_leaves(): 
        old_name = leaf.name
        if euk_delimiter and re.match(euk_regex, old_name):
            current_delimiter = euk_delimiter
        else:
            current_delimiter = delimiter
        genome_id = old_name.split(current_delimiter)[0]
        if source_euk_delimiter:
            genome_id = genome_id.split[source_euk_delimiter][1]
        if genome_id in tax_info_dict.keys():
            new_name =  tax_info_dict[genome_id][key_name] + " " + old_name
        else:
            print(genome_id, "was not found in the dict!")
            new_name = old_name
        if new_name in used_names:
            print (genome_id, "is duplicated!")
        leaf.name = new_name
        used_names.append(new_name)
    return tree


def annotate_trees_tax_info(in_treedir, out_treedir, tax_info_path, protein_ids=False, euk_delimiter=False, source_euk_delimiter=False):
    print("Reading taxonomy info")
    tax_info_dict = csv_to_dict(tax_info_path, main_key="gid", delimiter='\t')
    print("Annotating trees")
    for tree_file in listdir_nohidden(in_treedir):
        tree_path = in_treedir + tree_file 
        new_tree_path = out_treedir + tree_file + "_annotated.tree"
        try: 
            tree = Tree(tree_path)
            if protein_ids:
                new_tree = annotate_tree_tax_info_prot_ids(tree, tax_info_dict,key_name="taxonomy", delimiter="-", euk_delimiter=euk_delimiter,source_euk_delimiter=source_euk_delimiter)
            else:
                new_tree = annotate_tree_tax_info(tree, tax_info_dict,key_name="taxonomy")
            new_tree.write(format=2, outfile=new_tree_path)
        except:
            print ("Error", tree_path, new_tree_path)
    return 0

def annotate_gene_tree(tree, tax_info_dict, annotation_dict, euk_delimiter="_"):
    euk_regex = "^EP\d+" + euk_delimiter + "P\d+"
    delimiter = "-"
    for leaf in tree.iter_leaves(): 
        old_name = leaf.name
        if re.match(euk_regex, old_name):
            current_delimiter = euk_delimiter
            prot_id = delimiter.join(old_name.split(current_delimiter))
            if prot_id in annotation_dict.keys():
                annotation = annotation_dict[prot_id]
            else:
                print(prot_id, "was not found in the annotation dict!")
                annotation = ""
        else:
            current_delimiter = delimiter
            annotation = ""

        genome_id = old_name.split(current_delimiter)[0]
        if genome_id in tax_info_dict.keys():
            taxonomy =  tax_info_dict[genome_id]["taxonomy"]
        else:
            print(genome_id, "was not found in the taxonomy dict!")
            taxonomy = old_name
        new_name = taxonomy + " " + annotation
        leaf.name = new_name
    return tree

def annotate_gene_trees(in_treedir, out_treedir, prot_dir, tax_info_path, euk_delimiter="_"):
    print("Reading taxonomy info")
    tax_info_dict = csv_to_dict(tax_info_path, main_key="gid", delimiter='\t')
    print("Reading annotations")
    annotation_dict = get_prot_annotations(prot_dir)
    print("Annotating trees")
    for tree_file in listdir_nohidden(in_treedir):
        print (tree_file)
        tree_path = in_treedir + tree_file 
        new_tree_path = out_treedir + tree_file + "_annotated.tree"
        tree = Tree(tree_path)
        new_tree = annotate_gene_tree(tree, tax_info_dict, annotation_dict, euk_delimiter=euk_delimiter)
        new_tree.write(format=2, outfile=new_tree_path)
    return out_treedir

tax_info_path="/Users/vl18625/work/euk/protein_sets/taxa_annotations.tsv"
prot_dir = "/Users/vl18625/work/euk/protein_sets/anna_dataset/anna_eukprot3_proteome_dataset/"
in_treedir="/Users/vl18625/work/euk/markers_euks/nina_markers/be/cyano/initial/trees/"
out_treedir="/Users/vl18625/work/euk/markers_euks/nina_markers/be/cyano/initial/trees_annotated/"

# annotate_trees_tax_info(in_treedir, out_treedir, tax_info_path, protein_ids=True, euk_delimiter="_")
annotate_gene_trees(in_treedir, out_treedir, prot_dir, tax_info_path, euk_delimiter="-")
