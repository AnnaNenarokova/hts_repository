#!/usr/bin/python3
import re
import os
from Bio import SeqIO
import sys
sys.path.insert(0, "/Users/vl18625/work/code/ngs/")
sys.path.insert(0, "/scratch/nenarokova/code/ngs/")
from py_scripts.helpers.parse_csv import *

def listdir_nohidden(path):
	for f in os.listdir(path):
		if not f.startswith('.'):
			yield f

def read_list(list_path):
	result_list = []
	with open (list_path) as list_file:
		for line in list_file:
			result_list.append(line.rstrip())
	return result_list

def parse_hmmreport(hmm_report_path, columns_str=False):
	results = []
	if not columns_str:
		columns_str = "sseqid s_accession qseqid q_accession evalue score bias 1_domain_evalue 1_domain_score 1_domain_bias exp reg clu ov env dom rep inc"
		columns_list = columns_str.split(" ")
	with open(hmm_report_path) as hmmfile:
		for line in hmmfile:
			if line[0] != "#":
				line_edited = re.sub(' +', ' ', line)
				line_split = line_edited.rstrip().split(" ")
				qseqid = line_split[columns_list.index("qseqid")]
				sseqid = line_split[columns_list.index("sseqid")]
				evalue = float(line_split[columns_list.index("evalue")])
				bitscore = float(line_split[columns_list.index("score")])
				result_dict = {"qseqid": qseqid, "sseqid": sseqid, "evalue": evalue, "bitscore": bitscore}
				results.append(result_dict)
	return results

def prepare_hmm_dict(hmm_report_dir, hmm_ext=".txt", proteome_ext=".fasta", max_evalue=0.0000001, n_best=100, monobranch=False):
	hmm_dict = {}
	for hmm_report in listdir_nohidden(hmm_report_dir):
		hmm_report_name_split = hmm_report.split(proteome_ext)
		proteome_file = hmm_report_name_split[0] + proteome_ext
		hmm_file = hmm_report_name_split[1].split(hmm_ext)[0]
		if monobranch:
			hmm_file_split = hmm_file.split("_")
			cog_file = hmm_file_split[0] + ("_") + hmm_file_split[1] + ".faa"
		else:
			cog_file = hmm_file
		if proteome_file not in hmm_dict:
			hmm_dict[proteome_file] = {}
		if cog_file not in hmm_dict[proteome_file].keys():
			hmm_dict[proteome_file][cog_file] = {}
		hmm_report_path = hmm_report_dir + hmm_report
		hmm_results = parse_hmmreport(hmm_report_path)
		hmm_results = list(filter(lambda result: (result["evalue"] <= max_evalue), hmm_results))
		if len(hmm_results) > n_best:
			hmm_results = sorted(hmm_results, key=lambda result: result["evalue"])
			hmm_results = hmm_results[:n_best]
		for hmm_result in hmm_results:
			hmm_dict[proteome_file][cog_file][hmm_result["sseqid"]] = ""
	return hmm_dict

def prepare_fastas(hmm_report_dir, proteomes_dir, cog_dir, result_dir, hmm_ext=".hmm", proteome_ext=".fasta", n_best=100, max_evalue=0.0000001):
	print("Parcing hmm_reports")
	hmm_dict = prepare_hmm_dict(hmm_report_dir, n_best=n_best, max_evalue=max_evalue)
	print("Parcing proteomes sequences")
	for proteome in listdir_nohidden(proteomes_dir):
		proteome_dict = hmm_dict[proteome]
		proteome_path = proteomes_dir + proteome
		for record in SeqIO.parse(proteome_path, "fasta"):
			sseqid = record.id
			for cog in proteome_dict:
				if record.id in proteome_dict[cog]:
					hmm_dict[proteome][cog][sseqid] = record
	print("Writing down sequences")
	for cog_file in listdir_nohidden(cog_dir):
		cog = cog_file
		out_records = []
		cog_path = cog_dir + cog_file
		outpath = result_dir + cog_file
		for record in SeqIO.parse(cog_path, "fasta"):
			out_records.append(record)
		for proteome in hmm_dict:
			if cog in hmm_dict[proteome].keys():
				proteome_cog_dict = hmm_dict[proteome][cog]
			else:
				print (cog + " not in hmm_dict[" + proteome + "]")
			for sseqid in proteome_cog_dict:
				out_records.append(proteome_cog_dict[sseqid])
		SeqIO.write(out_records, outpath, "fasta")
	return 0

def prepare_fastas_keep_list(hmm_report_dir, proteomes_dir, cog_dir, result_dir, monobranch=False, keep_list_path=False, hmm_ext=".txt", proteome_ext=".fasta", n_best=1, max_evalue=0.00001):
	if keep_list_path: keep_list = read_list(keep_list_path)
	print("Parcing hmm_reports")
	hmm_dict = prepare_hmm_dict(hmm_report_dir, hmm_ext, proteome_ext, n_best, max_evalue, monobranch=monobranch)
	print("Parcing proteome sequences")
	proteome_set = set()
	for proteome in listdir_nohidden(proteomes_dir):
		proteome_id = proteome.split("-")[0]
		if not keep_list_path or (proteome_id in keep_list):
			proteome_set.add(proteome)
			proteome_dict = hmm_dict[proteome]
			proteome_path = proteomes_dir + proteome
			for record in SeqIO.parse(proteome_path, "fasta"):
				sseqid = record.id
				for cog_file in proteome_dict:
					if record.id in proteome_dict[cog_file]:
						hmm_dict[proteome][cog_file][sseqid] = record
	print("Writing down sequences")
	for cog_file in listdir_nohidden(cog_dir):
		out_set = set()
		out_records = []
		cog_path = cog_dir + cog_file
		outpath = result_dir + cog_file
		for record in SeqIO.parse(cog_path, "fasta"):
			seqid = record.id
			if seqid not in out_set:
				out_records.append(record)
				out_set.update(seqid)
		for proteome in proteome_set:
			if cog_file in hmm_dict[proteome]:
				proteome_cog_dict = hmm_dict[proteome][cog_file]
				for sseqid in proteome_cog_dict:
					record = proteome_cog_dict[sseqid]
					seqid = record.id
					if seqid not in out_set:
						out_records.append(record)
						out_set.update(seqid)
		SeqIO.write(out_records, outpath, "fasta")
	return 0

def parse_euk_hmm_dict(hmm_report_dir, source_name, hmm_dict, hmm_ext=".txt", proteome_ext=".fasta"):
	for hmm_report in listdir_nohidden(hmm_report_dir):
		hmm_report_name_split = hmm_report.split(proteome_ext)
		euk_id = hmm_report_name_split[0]
		if euk_id not in hmm_dict:
			hmm_dict[euk_id] = {}
		
		hmm_report_path = hmm_report_dir + hmm_report
		hmm_results = parse_hmmreport(hmm_report_path)

		for hmm_result in hmm_results:
			sseqid = hmm_result["sseqid"]
			if sseqid not in hmm_dict[euk_id]:
				hmm_dict[euk_id][sseqid] = {source_name:[]}
			elif source_name not in hmm_dict[euk_id][sseqid]:
				hmm_dict[euk_id][sseqid][source_name] = []
			hmm_dict[euk_id][sseqid][source_name].append(hmm_result)

	return hmm_dict

def prepare_ABC_hmm_dict(a_dir, b_dir, c_dir):
	hmm_dict = {}
	print ("Parcing A")
	source_name="archaea"
	hmm_dict = parse_euk_hmm_dict(a_dir, source_name, hmm_dict)
	print ("Parcing B")
	source_name="alpha"
	hmm_dict = parse_euk_hmm_dict(b_dir, source_name, hmm_dict)
	print ("Parcing C")
	source_name="cyano"
	hmm_dict = parse_euk_hmm_dict(c_dir, source_name, hmm_dict)
	return hmm_dict

def find_best_hit_ABC(prot_id_dict):
	best_bitscore = 0
	best_source_name = None
	for source_name in prot_id_dict:
		for hit in prot_id_dict[source_name]:
			hit_bitscore =  hit['bitscore']
			if hit_bitscore > best_bitscore:
				best_bitscore = hit_bitscore
				best_source_name = source_name
	return best_source_name

def make_euk_statistics(ABC_hmm_dict):
	euk_stats = {}
	for euk_id in ABC_hmm_dict:
		euk_dict = ABC_hmm_dict[euk_id]
		euk_stats[euk_id] = {"archaea":0, "alpha":0, "cyano":0, "total_hits":0}
		for prot_id in euk_dict:
			euk_stats[euk_id]["total_hits"] += 1
			source_name = find_best_hit_ABC(euk_dict[prot_id])
			if source_name:
				euk_stats[euk_id][source_name] += 1
	return euk_stats

def write_euk_stats(a_dir, b_dir, c_dir, outpath):
	ABC_hmm_dict = prepare_ABC_hmm_dict(a_dir, b_dir, c_dir)
	euk_stats = make_euk_statistics(ABC_hmm_dict)
	write_dict_of_dicts(euk_stats, outpath, key_name="species")
	return outpath

def prepare_best_ABC_hmm_dict(ABC_hmm_dict):
	best_ABC_hmm_dict = {}
	for species in ABC_hmm_dict:
		best_ABC_hmm_dict[species] = {}
		species_dict = ABC_hmm_dict[species]
		for prot_id in species_dict:
			best_bitscore = 0
			best_hit = None
			best_source = None
			best_ABC_hmm_dict[species][prot_id] = {}
			prot_dict = species_dict[prot_id]
			for source in prot_dict:
				for hit in prot_dict[source]:
					bitscore = hit['bitscore']
					if bitscore > best_bitscore:
						best_bitscore = bitscore
						best_hit = hit
						best_source = source
			best_ABC_hmm_dict[species][prot_id]['best_hit'] = best_hit
			best_ABC_hmm_dict[species][prot_id]['source'] = best_source
	return best_ABC_hmm_dict

def prepare_euk_marker_dict(best_ABC_hmm_dict, arcog_to_cog):
	euk_marker_dict = {}
	for species in best_ABC_hmm_dict:
		species_dict = best_ABC_hmm_dict[species]
		for prot_id in species_dict:
			prot_dict = species_dict[prot_id]
			hit = prot_dict['best_hit']
			source = prot_dict['source']
			qseqid = hit['qseqid']
			if qseqid in arcog_to_cog:
				marker_id = arcog_to_cog[qseqid]
			else:
				marker_id = qseqid
			if marker_id not in euk_marker_dict:
				euk_marker_dict[marker_id] = {}
				euk_marker_dict[marker_id][species] = {'alpha':[],'archaea':[],'cyano':[]}
			elif species not in euk_marker_dict[marker_id]:
				euk_marker_dict[marker_id][species] = {'alpha':[],'archaea':[],'cyano':[]}
			euk_marker_dict[marker_id][species][source].append(hit)
	return euk_marker_dict

def prepare_best_euk_marker_dict(euk_marker_dict):
	best_euk_marker_dict= {}
	for cog in euk_marker_dict:
		best_euk_marker_dict[cog] = {}
		for species in euk_marker_dict[cog]:
			best_euk_marker_dict[cog][species] = {'alpha': None,'archaea': None,'cyano': None}
			for source in euk_marker_dict[cog][species]:
				best_bitscore = 0
				best_hit = None
				for hit in euk_marker_dict[cog][species][source]:
					if hit['bitscore'] > best_bitscore:
						best_hit = hit
				best_euk_marker_dict[cog][species][source] = best_hit
	return best_euk_marker_dict

def prepare_seqid_dict(best_euk_marker_dict):
	used_seqs = []
	seqid_dict = {}
	for cog in best_euk_marker_dict:
		seqid_dict[cog] = {}
		for species in best_euk_marker_dict[cog]:
			seqid_dict[cog][species] = []
			for source in best_euk_marker_dict[cog][species]:
				hit = best_euk_marker_dict[cog][species][source]
				if hit:
					sseqid = hit['sseqid']
					if sseqid not in used_seqs:
						used_seqs.append(sseqid)
						seqid_dict[cog][species].append(sseqid)
					else:
						print(f"ERROR! {sseqid} is duplicated")
	return seqid_dict

def filter_fonticula(seqid_dict):
	for cog in seqid_dict:
		new_prot_list = []
		fonticula_id = "EP00159_Fonticula_alba"
		if fonticula_id in seqid_dict[cog].keys():
			for prot_id in seqid_dict[cog]["EP00159_Fonticula_alba"]:
				prot_id_splitted = prot_id.split("-")
				new_prot_id = prot_id_splitted[0] + "-" + prot_id_splitted[-1]
				new_prot_list.append(new_prot_id)
			seqid_dict[cog]["EP00159_Fonticula_alba"] = new_prot_list
	return seqid_dict

def prepare_euk_seq_dict(seqid_dict,exclude_euk_list,proteomes_dir,include_markers_list=None, proteome_ext=".fasta"):
	print ("Analysing euk_marker_dict")
	if include_markers_list:
		markers = include_markers_list
	else:
		markers = euk_marker_dict
	
	euk_seq_dict = {}
	species_dict = {}
	for marker_id in markers:
		euk_seq_dict[marker_id] = {}
		for species in seqid_dict[marker_id]:
			if species not in exclude_euk_list:
				if species not in euk_seq_dict[marker_id]:
					euk_seq_dict[marker_id][species] = {}
				if species not in species_dict:
					species_dict[species] = {}
				for prot_id in seqid_dict[marker_id][species]:
					euk_seq_dict[marker_id][species][prot_id] = ""
					species_dict[species][prot_id] = marker_id
	print ("Collecting euk fasta seqs")
	for species in species_dict:
		print (species)
		proteome_path = proteomes_dir + species + proteome_ext
		for record in SeqIO.parse(proteome_path, "fasta"):
			prot_id = record.id 
			if prot_id in species_dict[species]:
				marker_id = species_dict[species][prot_id]
				euk_seq_dict[marker_id][species][prot_id] = record
	return euk_seq_dict

def prepare_markers_seq_dict(euk_seq_dict,AB_markers_dir,cog_ext=".faa"):
	markers_seq_dict = {}
	for marker_id in euk_seq_dict:
		markers_seq_dict[marker_id] = []
		AB_path = AB_markers_dir + marker_id + cog_ext
		for record in SeqIO.parse(AB_path, "fasta"):
			markers_seq_dict[marker_id].append(record)
		for species in euk_seq_dict[marker_id]:
			for prot_id in euk_seq_dict[marker_id][species]:
				markers_seq_dict[marker_id].append(euk_seq_dict[marker_id][species][prot_id])
	return markers_seq_dict

def write_fastas(markers_seq_dict, outdir,marker_ext=".faa"):
	for marker_id in markers_seq_dict:
		records = []
		outfasta = outdir + marker_id + marker_ext
		for record in markers_seq_dict[marker_id]:
			records.append(record)
		SeqIO.write(records, outfasta, "fasta")
	return outdir

def prepare_ABE_fastas():
	workdir = "/Users/vl18625/work/euk/markers_euks/hmm_results/"
	a_dir = workdir + "ae_hmm_results/"
	b_dir = workdir + "alpha_hmm_results/"
	c_dir = workdir + "cyano_hmm_results/"

	AB_markers_dir="/Users/vl18625/work/euk/protein_sets/AB_manually_filtered_Nina/"

	proteomes_dir="/Users/vl18625/work/euk/protein_sets/anna_dataset/anna_eukprot3_proteome_dataset/"

	exclude_euk_list = ["EP01146_Carpediemonas_membranifera","EP00033_Pygsuia_biforma","EP00727_Mastigamoeba_balamuthi","EP00480_Reticulomyxa_filosa","EP00157_Rozella_allomycis","EP00771_Trimastix_marina"]
	outpath = "/Users/vl18625/work/euk/markers_euks/hmm_results/euk_stats.csv"
	arcog_cog_path = "/Users/vl18625/work/euk/markers_euks/nina_markers/arCOG_COG.csv"
	include_markers_list = ["COG0016","COG0049","COG0051","COG0052","COG0064","COG0081","COG0085","COG0086","COG0087","COG0088","COG0090","COG0091","COG0092","COG0093","COG0094","COG0096","COG0098","COG0099","COG0100","COG0103","COG0201","COG0202","COG0532","COG0533","COG0541","COG0552"]

	outdir="/Users/vl18625/work/euk/markers_euks/nina_markers/abe/ABE_26_markers_fastas/"

	arcog_to_cog = csv_to_dict_simple(arcog_cog_path)

	ABC_hmm_dict = prepare_ABC_hmm_dict(a_dir, b_dir, c_dir)

	print("preparing best_ABC_hmm_dict")
	best_ABC_hmm_dict = prepare_best_ABC_hmm_dict(ABC_hmm_dict)

	print("preparing euk_marker_dict")
	euk_marker_dict = prepare_euk_marker_dict(best_ABC_hmm_dict, arcog_to_cog)

	print("preparing best_euk_marker_dict")
	best_euk_marker_dict = prepare_best_euk_marker_dict(euk_marker_dict)

	seqid_dict = prepare_seqid_dict(best_euk_marker_dict)

	seqid_dict = filter_fonticula(seqid_dict)

	euk_seq_dict = prepare_euk_seq_dict(seqid_dict,exclude_euk_list,proteomes_dir,include_markers_list=include_markers_list, proteome_ext=".fasta")

	markers_seq_dict = prepare_markers_seq_dict(euk_seq_dict,AB_markers_dir,cog_ext=".faa")

	outdir = write_fastas(markers_seq_dict, outdir,marker_ext=".faa")
	return outdir

hmm_report_dir = "/scratch/nenarokova/euk/markers/hmm_results/alpha/"
cog_dir = "/scratch/nenarokova/euk/markers/bacteria/alphaproteo_markers/faa/"
proteomes_dir = "/scratch/nenarokova/euk/proteomes/anna_eukprot3_set_v2_21_03_23/"
result_dir = "/scratch/nenarokova/euk/markers/be/many_hits/alpha/faa/"
prepare_fastas(hmm_report_dir, proteomes_dir, cog_dir, result_dir)
