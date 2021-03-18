#!/usr/bin/python
import sys
sys.path.insert(0, "/Users/annanenarokova/work/code/ngs/")
sys.path.insert(0, "/home/users/nenarokova/ngs/")
from Bio.SeqUtils import GC
from Bio import SeqIO
from py_scripts.helpers.parse_csv import *
from py_scripts.biohelpers.calculate_hit_coverage import *
from py_scripts.biohelpers.analyse_taxa import *

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
    contigs_hits = {}
    with open(blast_tsv) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter='\t')
        for blast_hit in reader:
            contig = blast_hit['qseqid']
            if contig not in contigs_hits.keys():
                contigs_hits[contig] = []
            contigs_hits[contig].append(blast_hit)
    cov_name = ref_species + "_bh_cov"
    print ("Counting hit coverage for " + ref_species)
    for contig in contigs_info:
        if contig in contigs_hits.keys():
            contig_coverage = calculate_hit_cov_query(contigs_hits[contig])
        else:
            contig_coverage = float(0)
        contigs_info[contig][cov_name] = contig_coverage
    return contigs_info

def add_best_species(contigs_info, blast_path_dict):
    for contig in contigs_info:
        max_cov = 0
        second_max_cov = 0
        best_species = ''
        for species in blast_path_dict:
            cov_name = species + "_bh_cov"
            coverage = float(contigs_info[contig][cov_name])
            if coverage > max_cov:
                second_max_cov = max_cov
                max_cov = coverage
                best_species = species
            elif coverage > second_max_cov:
                second_max_cov = coverage
        contigs_info[contig]["best_ref_sp"] = best_species
        significance = float(0)
        if max_cov > 0:
            if second_max_cov > 0:
                significance = max_cov/second_max_cov
            else:
                significance = 999999999
        contigs_info[contig]["significance"] = significance
    return contigs_info

def add_diamond_taxa(contigs_info, diamond_taxa_path):
    taxid_dict, seq_dict = get_taxid_dicts(diamond_taxa_path)
    for contig in contigs_info:
        taxid = seq_dict[contig]["taxid"]
        evalue = seq_dict[contig]["evalue"]
        if taxid in taxid_dict:
            cur_dict = taxid_dict[taxid]
            if "name" in cur_dict:
                ncbi_species = cur_dict["name"]
            else:
                name = ""
                print ("name is not in the keys", taxid)
            if "lineage" in cur_dict:
                lineage = cur_dict["lineage"]
            else:
                lineage = ""
                print ("lineage is not in the keys", taxid)
        else:
            print(taxid, "is not in the taxid_dict!")
            ncbi_species = ""
            lineage = ""

        contigs_info[contig]["taxid"] = taxid
        contigs_info[contig]["evalue"] = evalue
        contigs_info[contig]["ncbi_species"] = ncbi_species
        contigs_info[contig]["lineage"] = lineage
    return contigs_info

def analyse_metaspades_contigs(contigs_fasta, outpath, diamond_taxa_path, blast_path_dict, outfmt=False):
    if not outfmt:
        outfmt = "qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send"
    print ("Getting general contig reports")
    contigs_info = get_simple_report_contigs(contigs_fasta)
    print ("Getting custom db reports")
    for species in blast_path_dict:
        contigs_info = add_blast_results(contigs_info, blast_path_dict[species], species, outfmt)
    contigs_info = add_best_species(contigs_info, blast_path_dict)
    print ("Getting NCBI taxonomy report")
    contigs_info = add_diamond_taxa(contigs_info, diamond_taxa_path)
    print ("Writing down the results")
    write_dict_of_dicts(contigs_info, outpath, key_name="contig_id")
    return contigs_info


contigs_fasta = "/Users/annanenarokova/work/hypsa_local/K28_contigs.fasta"
outpath = "/Users/annanenarokova/work/hypsa_local/K28_contigs_info_test.csv"
diamond_taxa_path = "/Users/annanenarokova/work/hypsa_local/K28_Hippobosca_contigs_dmnd_tax.tsv"

outfmt = "qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send"
blast_path_dict = {
    "Wolbachia": "/Users/annanenarokova/work/hypsa_local/diamond_blast_results/K28_wolbachia_ncbi.faa.dmnd.tsv",
    "Arsenophonus": "/Users/annanenarokova/work/hypsa_local/diamond_blast_results/K28_arsenophonus_ncbi.faa.dmnd.tsv"
    }

contigs_info = analyse_metaspades_contigs(contigs_fasta, outpath, diamond_taxa_path, blast_path_dict)
