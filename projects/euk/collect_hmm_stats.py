#!/usr/bin/python3
import os
import re
import sys
sys.path.insert(0, "/Users/anna/work/code/ngs/")
sys.path.insert(0, "/user/home/vl18625/code/ngs")
sys.path.insert(0, "/Users/vl18625/work/code/ngs/")
from py_scripts.helpers.parse_csv import *

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

def prepare_hmm_dict(hmm_report_dir, proteome_ext, hmm_ext):
	hmm_dict = {}
	for hmm_report in listdir_nohidden(hmm_report_dir):
		hmm_report_name_split = hmm_report.split(proteome_ext)
		proteome_name = hmm_report_name_split[0]
		cog_name = hmm_report_name_split[1].split(hmm_ext)[0]
		if proteome_name not in hmm_dict:
			hmm_dict[proteome_name] = {}
		hmm_dict[proteome_name][cog_name] = 0
		hmm_report_path = hmm_report_dir + hmm_report
		hmm_results = parse_hmmreport(hmm_report_path)
		for hmm_result in hmm_results:
			hmm_dict[proteome_name][cog_name] += 1
	return hmm_dict


hmm_report_dir = "/Users/vl18625/work/euk/markers_euks/hmm_results_elife_eukrpot2/"
full_stats_path = "/Users/vl18625/work/euk/markers_euks/hmm_results_elife_eukrpot2.csv"
proteome_ext = ".fasta"
hmm_ext = ".faa"
hmm_dict = prepare_hmm_dict(hmm_report_dir, proteome_ext, hmm_ext)

write_dict_of_dicts(hmm_dict, full_stats_path, key_name="species")