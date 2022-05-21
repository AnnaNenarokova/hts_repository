#!/usr/bin/python3
from Bio import SeqIO
from os import listdir
import csv

species_path="/home/anna/bioinformatics/blasto_local/ciliates/ncbi_ciliate_assembly_ids_short.csv"
with open(species_path) as csvfile:
    reader = csv.DictReader(csvfile)
    seqdict = {}
    for row in reader:
        seqdict[row['id']] = row['species']

seqdir_path="/home/anna/bioinformatics/blasto_local/ciliates/ciliate_genomes/aragorn/trna_seqs/"
# outpath="/home/anna/bioinformatics/blasto_local/ciliates/ciliate_genomes/aragorn/trp_all_test.fna"
outpath="/home/anna/bioinformatics/blasto_local/ciliates/ciliate_genomes/aragorn/all_trnas.fna"

out_records = []
for seqfile in listdir(seqdir_path):
    splitname = seqfile.split("_")
    genome_id = splitname[0] + "_" + splitname[1]
    seqfile_path = seqdir_path + seqfile
    i = 0
    for record in SeqIO.parse(seqfile_path, "fasta"):
        if "t" in record.id:
        # if "Trp" in record.id:
            i += 1
            new_record = record
            new_id = seqdict[genome_id] + "_" + record.id + "_" + str(i)
            new_record.id = new_id
            out_records.append(new_record)
SeqIO.write(out_records, outpath, "fasta")


