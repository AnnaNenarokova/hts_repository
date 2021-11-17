#!/usr/bin/python
import re

def parse_hmmresults(hmm_result_path, columns_str=False):
	if not columns_str:
		columns_str = "sseqid s_accession qseqid q_accession evalue score bias 1_domain_evalue 1_domain_score 1_domain_bias exp reg clu ov env dom rep inc"
		columns_list = columns_str.split(" ")
	with open(hmm_result_path) as hmmfile:
		for line in hmmfile:
			if line[0] != "#":
				line_edited = re.sub(' +', ' ', line)
				line_split = line_edited.rstrip().split(" ")
				qseqid = line_split[columns_list.index("qseqid")]
				sseqid = line_split[columns_list.index("sseqid")]
				evalue = float(line_split[columns_list.index("evalue")])
				bitscore = float(line_split[columns_list.index("score")])
	return 0

hmm_result_path = "/Users/anna/work/euk_local/hmm_results_ed_cogs/UP000444721_5763.fasta95_COG5257.faa.hmm.txt"

parse_hmmresults(hmm_result_path)