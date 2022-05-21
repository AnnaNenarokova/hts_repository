#!/usr/bin/python3
from Bio import SeqIO
from os import listdir

def listdir_nohidden(path):
    for f in listdir(path):
        if not f.startswith('.'):
            yield f

def read_list(list_path):
    result_list = []
    with open (list_path) as list_file:
        for line in list_file:
            result_list.append(line.rstrip())
    return result_list

def rename_seq_eukprot3(old_name):
    old_name_split = old_name.split("_")
    new_name = old_name_split[0] + "_" + old_name_split[-1]
    return new_name

def prepare_euk_info_eukprot3(fasta_folder, keep_list_path, outpath, delimiter="\t"):
    keep_list = read_list(keep_list_path)
    with open (outpath, "w") as outfile:
        for fasta in listdir_nohidden(fasta_folder):
            fasta_id = fasta.split("_")[0]
            if fasta_id in keep_list:
                print (fasta)
                fasta_path = fasta_folder + fasta
                for record in SeqIO.parse(fasta_path, "fasta"):
                    old_id = record.id
                    new_id = rename_seq_eukprot3(record.id)
                    description = record.description
                    annotation = description.replace(old_id, "")
                    out_line = new_id + delimiter + annotation + "\n"
                    outfile.write(out_line)
    return outpath


fasta_folder="/Users/vl18625/work/euk/eukprot/eukprot3/proteins/"
keep_list_path="/Users/vl18625/work/euk/eukprot/anna_eukprot3_keeplist.txt"
outpath="/Users/vl18625/work/euk/eukprot/anna_set_prot_info.tsv"

prepare_euk_info_eukprot3(fasta_folder, keep_list_path, outpath, delimiter="\t")