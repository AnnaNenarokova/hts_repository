#!/usr/bin/python3
import random
import ete3

def make_random_subset(species_list, subset_size):
    random_sp_subset = random.sample(species_list, subset_size)
    return random_sp_subset

def read_list(list_path):
    result_list = []
    with open (list_path) as list_file:
        for line in list_file:
            result_list.append(line.rstrip())
    return result_list

def create_random_subtree(subset_size, species_list_path, output_tree_path):
    species_list = read_list(species_list_path)
    random_tree = ete3.Tree()
    random_tree.populate(subset_size, species_list)
    random_tree.write(format=9, outfile=output_tree_path)
    return random_tree

species_list_path = "/Users/vl18625/work/euk/markers_euks/nina_markers/old_data/abe/old_data/COG0085.txt"
output_tree_path = "/Users/vl18625/work/euk/random_tree_for_haicai.tree"
subset_size = 100

random_tree = create_random_subtree(subset_size, species_list_path, output_tree_path)

print ("The tree is written in " + output_tree_path)