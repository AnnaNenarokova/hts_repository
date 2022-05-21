#!python3
import re
import os

def listdir_nohidden(path):
	for f in os.listdir(path):
		if not f.startswith('.'):
			yield f

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

def prepare_hmm_report(hmm_result_dir, report_outpath):
	with open(report_outpath, "w") as outfile:
		outline = "\t".join(["query", "sseqid", "genome_id", "evalue"])
		outfile.write(outline + "\n")
		for hmm_report in listdir_nohidden(hmm_result_dir):
			hmm_report_path = hmm_result_dir + hmm_report
			query_name = hmm_report.split(".faa")[0]
			hmm_results = parse_hmmreport(hmm_report_path)
			hmm_results = sorted(hmm_results, key=lambda result: result["evalue"])
			if hmm_results:
				best_hmm_hit = hmm_results[0]
				sseqid = best_hmm_hit["sseqid"]
				genome_id = sseqid.split("-")[0]
				evalue = str(best_hmm_hit["evalue"])
				outline= "\t".join([query_name, sseqid, genome_id, evalue])
			else:
				print (hmm_report, "no hits!")
				sseqid = "#N/A"
				genome_id = "#N/A"
				evalue = "#N/A"
			outfile.write(outline + "\n")
	return report_outpath

hmm_result_dir = "/Users/vl18625/work/euk/markers_euks/nina_markers/mono_euk_sets/set2/hmm_results/"
report_outpath = '/Users/vl18625/work/euk/markers_euks/nina_markers/mono_euk_sets/set2/summary_hmm_report.txt'

prepare_hmm_report(hmm_result_dir, report_outpath)