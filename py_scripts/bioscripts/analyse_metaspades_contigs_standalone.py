#!/usr/bin/python3
import csv
import os
import sys
from encoder import XML2Dict
from Bio.SeqUtils import GC
from Bio import SeqIO
from Bio import Entrez
Entrez.email = "vacatko@prf.jcu.cz"

def write_list_of_dicts(list_of_dicts, outpath, fieldnames=False):
    with open(outpath, 'w') as csvfile:
        if not fieldnames:
            fieldnames = list_of_dicts[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in list_of_dicts:
            writer.writerow(row)
        csvfile.close()
    return outpath

def write_dict_of_dicts(dict_of_dicts, outpath, key_name=False, fieldnames=False):
    list_of_dicts = []
    for key in dict_of_dicts:
        cur_dict = {}
        cur_dict[key_name] = key
        for k in dict_of_dicts[key]:
            cur_dict[k] = dict_of_dicts[key][k]
        list_of_dicts.append(cur_dict)
    write_list_of_dicts(list_of_dicts, outpath, fieldnames)
    return outpath

def csv_to_list_of_dicts(csv_path, delimiter=',', fieldnames=None):
    with open(csv_path) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter=delimiter)
        list_of_dicts = []
        for row in reader:
            list_of_dicts.append(row)
        csvfile.close
    return list_of_dicts

def merge_intervals(intervals):
    intervals.sort(key=lambda interval: interval[0])
    merged_intervals = [intervals[0]]
    for current in intervals:
        previous = merged_intervals[-1]
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged_intervals.append(current)
    return merged_intervals

def sum_interval_length(intervals):
    sum_int_length = 0
    for interval in intervals:
        length = interval[1] - interval[0]
        sum_int_length += length
    return sum_int_length

def calculate_hit_cov_query(blast_hits):
    if blast_hits == []:
        hit_coverage = float(0)
    else:
        total_length = int(blast_hits[0]['qlen'])

        intervals = []
        for blast_hit in blast_hits:
            new_interval = sorted( [ int(blast_hit['qstart']), int(blast_hit['qend']) ] )
            intervals.append(new_interval)
        intervals = merge_intervals(intervals)

        hit_sum_length = sum_interval_length(intervals)

        hit_coverage = float(hit_sum_length)/float(total_length)
    return hit_coverage

def get_contigs_hits(blast_csv_path):
    blast_hits = parse_csv(blast_csv_path, '\t')
    contigs_hits = {}
    for bh in blast_hits:
        qseqid = bh[qseqid_index]
        qlen = int(bh[qlen_index])
        qstart = int(bh[qstart_index])
        qend = int(bh[qend_index])
        if qseqid not in contigs_hits.keys():
            contigs_hits[qseqid] = []
        contigs_hits[qseqid].append([qstart, qend])
    return contigs_hits  

def read_diamond_result(diamond_taxa_result_path, outfmt_opts=False):
    if not outfmt_opts:
        outfmt_opts = "qseqid taxid evalue"
    outfmt_opt_list = outfmt_opts.split(" ")
    seq_dict = {}
    taxid_dict = {}
    with open(diamond_taxa_result_path) as diamond_f:
        for line in diamond_f:
            line_split = line.rstrip().split("\t")
            qseqid = line_split[outfmt_opt_list.index("qseqid")]
            taxid = line_split[outfmt_opt_list.index("taxid")]
            evalue = float(line_split[outfmt_opt_list.index("evalue")])
            seq_dict[qseqid] = {"taxid": taxid, "evalue": evalue}
            if taxid in taxid_dict:
                taxid_dict[taxid]["count"] += 1
            else:
                taxid_dict[taxid] = {}
                taxid_dict[taxid]["count"] = 1
    return taxid_dict, seq_dict

def add_lineages(taxid_dict):
    taxids = list(taxid_dict.keys())
    ncbi_xml_record = Entrez.efetch(db="taxonomy", id=taxids).read()
    ncbi_dict = XML2Dict().parse(ncbi_xml_record)
    taxa = ncbi_dict['TaxaSet']['Taxon']
    for taxon in taxa:
        taxid = taxon['TaxId'].decode("utf-8")
        name = taxon['ScientificName'].decode("utf-8")
        try:
            lineage = taxon['Lineage'].decode("utf-8")
        except:
            lineage = taxon['Lineage']
        if taxid in taxid_dict.keys():
            taxid_dict[taxid]["name"] = name
            taxid_dict[taxid]["lineage"] = lineage
        else:
            taxid_found = False
            if 'LineageEx' in taxon.keys():
                for ex_lineage in taxon['LineageEx']['Taxon']:
                    old_taxid = ex_lineage['TaxId'].decode("utf-8") 
                    if old_taxid in taxid_dict.keys():
                        taxid_found = True
                        taxid = old_taxid
                        taxid_dict[taxid]["name"] = name
                        taxid_dict[taxid]["lineage"] = lineage  
                        break
            if not taxid_found:
                print ("Taxid", taxid, "not found in taxid dict")
    taxid_dict['0']["name"] = "none"
    taxid_dict['0']["lineage"] = "none"
    return taxid_dict

def get_taxid_dicts(diamond_taxa_result_path, outfmt_opts=False):
    taxid_dict, seq_dict = read_diamond_result(diamond_taxa_result_path, outfmt_opts)
    taxid_dict = add_lineages(taxid_dict)
    return taxid_dict, seq_dict

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
                print ("name is not in the keys, taxid", taxid)
            if "lineage" in cur_dict:
                lineage = cur_dict["lineage"]
            else:
                lineage = ""
                print ("lineage is not in the keys, taxid", taxid)
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

contigs_fasta = sys.argv[1]
outpath = sys.argv[2]
diamond_taxa_path = sys.argv[3]
blast_folder = sys.argv[4]

outfmt = "qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send"

blast_files = os.listdir(blast_folder)

blast_path_dict = {}
for blast_file in blast_files:
    name = blast_file.split(".")[0]
    blast_path_dict[name] = blast_folder + blast_file

contigs_info = analyse_metaspades_contigs(contigs_fasta, outpath, diamond_taxa_path, blast_path_dict, outfmt=outfmt)
