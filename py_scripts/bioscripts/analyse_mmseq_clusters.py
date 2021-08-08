#!/usr/bin/python
import sys
def get_clusters_array(mmseq_fasta_txt):
    clusters_array = []
    with open(mmseq_fasta_txt, "r") as input_f:
        for row in input_f:
            name = row[1:-2]
            size = int(name.split(";")[-1].split("=")[-1])
            clusters_array.append({"name":name,"size":size})
    return clusters_array

def return_duplicated_indices(clusters_array):
    duplicated_indices = []
    current_name = None
    i = 0
    for item in clusters_array:
        if current_name:
            if item["name"] == current_name:
                duplicated_indices.append(i-1)
        current_name = item["name"]
        i+=1
    return duplicated_indices

def analyse_clusters_array(clusters_array):
    duplicated_indices = return_duplicated_indices(clusters_array)
    print (duplicated_indices[0:10])
    print (len(duplicated_indices))

    clusters = {}

    i = 0
    for item in clusters_array:
        name = item["name"]
        size = item["size"]
        if i in duplicated_indices:
            clusters[name] = 0
            current_name = name
        else:
            clusters[current_name] += size
        i+=1
        if i%10000 == 0:
            print (i)
    return clusters

def calc_mmseq_cluster_sizes(mmseq_fasta_txt):
    clusters_array = get_clusters_array(mmseq_fasta_txt)
    print(clusters_array[0])
    print(len(clusters_array))
    clusters = analyse_clusters_array(clusters_array)
    print(len(clusters))
    return 0



mmseq_fasta_txt = "/Users/annanenarokova/work/blasto_local/tRNAs/tRNAseq/clusterRes_all_seqs.fasta.txt"

calc_mmseq_cluster_sizes(mmseq_fasta_txt)