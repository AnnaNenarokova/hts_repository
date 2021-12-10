#!/usr/bin/python
from Bio import SeqIO
from os import listdir

def listdir_nohidden(path):
    for f in listdir(path):
        if not f.startswith('.'):
            yield f

def rename_seqs_numbers(fasta_path, seq_name):
    out_tsv_path = fasta_path[:-6] + ".tsv"
    out_fasta = fasta_path[:-6] + "_renamed.fasta"
    results = []
    i = 0
    with open(out_tsv_path, "w") as out_tsv:
        for record in SeqIO.parse(fasta_path, "fasta"):
            i+=1
            old_id = record.id
            new_id = seq_name + str(i)
            record.id = new_id
            results.append(record)
            out_tsv.write('{}\t{}\n'.format(old_id,new_id))
    SeqIO.write(results, out_fasta, "fasta")
    return 0

def rename_seqs_uniprot(fasta_path, out_tsv_path=False):
    if not out_tsv_path:
        out_tsv_path= fasta_path[:-6] + ".tsv"
    out_fasta = fasta_path[:-6] + "_renamed.fasta"
    results = []
    i = 0
    with open(out_tsv_path, "a") as out_tsv:
        for record in SeqIO.parse(fasta_path, "fasta"):
            i+=1
            old_id = record.id
            description = record.description
            new_id = old_id.split("|")[1]
            record.id = new_id
            record.description = ""
            results.append(record)
            out_tsv.write('{}\t{}\t{}\n'.format(old_id,new_id, description))
    SeqIO.write(results, out_fasta, "fasta")
    return 0

def rename_many_seqs(fasta_dir, out_tsv_path):
    for fasta_file in listdir_nohidden(fasta_dir):
        print(fasta_file)
        fasta_path = fasta_dir + fasta_file
        rename_seqs_uniprot(fasta_path, out_tsv_path)
    return 0

fasta_dir="/Users/anna/work/euk_local/uniprot_proteomes/original_fastas/"
out_tsv_path="/Users/anna/work/euk_local/uniprot_proteomes/proteome_id_info.tsv"
rename_many_seqs(fasta_dir,out_tsv_path)