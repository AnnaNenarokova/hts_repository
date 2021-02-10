#!/usr/bin/python
import sys
sys.path.insert(0, "/Users/annanenarokova/work/code/ngs/")
sys.path.insert(0, "/home/users/nenarokova/ngs/")
from Bio.SeqUtils import GC
from Bio import SeqIO
from py_scripts.helpers.parse_csv import *
from py_scripts.biohelpers.calculate_hit_coverage import *

def get_simple_report_contigs(contigs_fasta):
    contigs_info = {}
    for record in SeqIO.parse(contigs_fasta, "fasta"):
        name = record.id
        length = int(name.split("_")[3])
        coverage = float(name.split("_")[-1])
        gc = float(GC(record.seq))
        contigs_info[name] = {"gc":gc, "coverage": coverage, "length": length}
    return contigs_info

def add_blast_results(contigs_info, blast_tsv, ref_species, outfmt):
    fieldnames = outfmt.split(" ")
    blast_results = csv_to_list_of_dicts(blast_tsv, delimiter='\t', fieldnames=fieldnames)
    cov_name = ref_species + "_bh_cov"
    contigs_hits = {}
    for contig in contigs_info:
        contigs_hits[contig] = []
        for blast_hit in blast_results:
            if contig == blast_hit['qseqid']:
                contigs_hits[contig].append(blast_hit)
    for contig in contigs_hits:
        contig_coverage = calculate_hit_cov_query(contigs_hits[contig])
        contigs_info[contig][cov_name] = contig_coverage
    return contigs_info

def analyse_metaspades_contigs(contigs_fasta, blast_path_dict, outpath, outfmt=False):
    if not outfmt:
        outfmt = "qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send"
    contigs_info = get_simple_report_contigs(contigs_fasta)
    for species in blast_path_dict:
        contigs_info = add_blast_results(contigs_info, blast_path_dict[species], species, outfmt)
    write_dict_of_dicts(contigs_info, outpath, key_name="contig_id")
    return contigs_info




contigs_fasta = "/mnt/data/metagenomic_data/spades_runs/K26/contigs.fasta"
outpath = "/mnt/data/metagenomic_data/ref_blast/K26_contigs_info.csv"
outfmt = "qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send"

blast_path_dict = {
    "Wolbachia": "/mnt/data/metagenomic_data/ref_blast/diamond_blast_results/K26_wolbachia_ncbi.faa.dmnd.tsv",
    "Arsenophonus": "/mnt/data/metagenomic_data/ref_blast/diamond_blast_results/K26_arsenophonus_ncbi.faa.dmnd.tsv",
    "Bartonella": "/mnt/data/metagenomic_data/ref_blast/diamond_blast_results/K26_bartonella_ncbi.faa.dmnd.tsv",
    "D_rerio": "/mnt/data/metagenomic_data/ref_blast/diamond_blast_results/K26_danio_rerio_uniprot.faa.dmnd.tsv",
    "Hippoboscidae": "/mnt/data/metagenomic_data/ref_blast/diamond_blast_results/K26_hipoboscoidea_ncbi.faa.dmnd.tsv",
    "Spiroplasma": "/mnt/data/metagenomic_data/ref_blast/diamond_blast_results/K26_spiroplasma_ncbi.faa.dmnd.tsv",
    "D_melanogaster": "/mnt/data/metagenomic_data/ref_blast/diamond_blast_results/K26_uniprot_drosophila_melanogaster.faa.dmnd.tsv",
    "H_sapiens": "/mnt/data/metagenomic_data/ref_blast/diamond_blast_results/K26_uniprot_homo_sapiens.faa.dmnd.tsv",
    "M_musculus": "/mnt/data/metagenomic_data/ref_blast/diamond_blast_results/K26_uniprot_mus_musculus.faa.dmnd.tsv"
    }

contigs_info = analyse_metaspades_contigs(contigs_fasta, blast_path_dict, outpath, outfmt=outfmt)
