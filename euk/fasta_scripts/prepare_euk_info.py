#!python3
from os import listdir
from Bio import SeqIO

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

fasta_folder="/Users/anna/work/euk_local/eukprot_proteomes/original_fastas/"

annotation_dict = prepare_euk_info(fasta_folder)