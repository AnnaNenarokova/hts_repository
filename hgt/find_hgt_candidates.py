#!python3
from ete3 import NCBITaxa
from Bio import SeqIO

ncbi_taxa = NCBITaxa()

diamond_result_path = "/home/vl18625/bioinformatics/diplonema/dpapi_genome_diamond_taxid.out"
infasta_path = "/home/vl18625/bioinformatics/diplonema/Dp_PB-MI_190104_dedup_cut_l100.faa"
outfasta_path = "/home/vl18625/bioinformatics/diplonema/dpapi_hgt_candidates.faa"

evalue_cutoff = 1
bacteria_taxid = 2


all_records = {}
for record in SeqIO.parse(infasta_path, "fasta"):
    all_records[record.id] = record

diamond_f = open(diamond_result_path, "r")

candidates = []

with open diamond_result_path as diamond_f:
    for line in diamond_f:
        line_split = line.rstrip().split("\t")
        id = line_split[0]
        taxid = line_split[1]
        evalue = float(line_split[2])
        if taxid == "0":
            is_bacteria = False
        else:
            is_bacteria = True if bacteria_taxid in ncbi_taxa.get_lineage(taxid) else False
        if is_bacteria and evalue < evalue_cutoff:
            candidates.append(all_records[id])
            
SeqIO.write(candidates, outfasta_path, "fasta")
 


