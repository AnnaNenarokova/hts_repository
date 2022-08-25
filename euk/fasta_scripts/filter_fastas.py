#!/usr/bin/python3
from os import listdir
from Bio import SeqIO

def listdir_nohidden(path):
    for f in listdir(path):
        if not f.startswith('.'):
            yield f

def filter_fastas_exclude_sp(exclude_list, indir, outdir, species_id_delimiter="_"):
	for file_name in listdir_nohidden(indir):
		infile = indir + file_name
		out_records = []
		for record in SeqIO.parse(infile, "fasta"):
			species_id = record.id.split(species_id_delimiter)[0]
			if species_id not in exclude_list:
				out_records.append(record)
		outfile = outdir + file_name
		SeqIO.write(out_records, outfile, "fasta")
	return 0

def filter_fasta_keep_sp(keep_list, infasta, outfasta, species_id_delimiter="-", euk=False):
	out_records = []
	euk_regex = "^EP\d+-P\d+"
	for record in SeqIO.parse(infasta, "fasta"):
		species_id = record.id.split(species_id_delimiter)[0]
		if euk:
			if re.match(euk_regex, record.id):
				if species_id in keep_list:
					out_records.append(record)
			else:
				out_records.append(record)
		else:
			if species_id in keep_list:
				out_records.append(record)
	SeqIO.write(out_records, outfasta, "fasta")
	return 0

def filter_fastas_keep_sp(keep_list, indir, outdir, species_id_delimiter="-", euk=False):
	for fasta in listdir_nohidden(indir):
		infasta = indir + fasta
		outfasta = outdir + fasta
		filter_fasta_keep_sp(keep_list, infasta, outfasta, species_id_delimiter=species_id_delimiter,euk=euk)
	return 0 

alpha_proteo_list=["GCA_002422845.1","GCA_009780035.1","GCA_006738645.1","GCA_002117145.1","GCA_000144605.1","GCA_000013025.1","GCA_000152825.2","GCA_007197755.1","GCA_002717245.1","GCA_002722055.1","GCA_002746255.1","GCA_000427665.1","GCA_002937855.1","GCA_001898075.1","GCA_000742475.1","GCA_000469665.2","GCA_000515255.1","GCA_000226315.1","GCA_004210305.1","GCA_000293845.2","GCA_000012345.1","GCA_000163555.2","GCA_900167455.1","GCA_902799835.1","GCA_000021745.1","GCA_000143145.1","GCA_000192745.1","GCA_000155675.2","GCA_003324715.1","GCA_003970735.1","GCA_002938315.1","GCA_000013085.1","GCA_003403095.1","GCA_000746585.2","GCA_000166935.1","GCA_002787635.1","GCA_002291925.1","GCA_009784235.1","GCA_000616095.1","GCA_002722885.1","GCA_000375545.1","GCA_000186705.2","GCA_009768975.1","GCA_000299935.1","GCA_000264455.2","GCA_002937655.1","GCA_002937675.1","GCA_002937625.1","GCA_002691145.1","GCA_002937495.1","GCA_002422365.1","GCA_002436405.1","GCA_001767855.1","GCA_002728255.1","GCA_011523425.1"]
cyano_list=["GCA_000464785.1","GCA_003503675.1","GCA_000155555.1","GCA_000019485.1","GCA_000346485.2","GCA_000204075.1","GCA_000484535.1","GCA_001870225.1","GCA_000353285.1","GCA_000015645.1","GCA_000195975.1","GCA_000013225.1","GCA_002075285.3","GCA_000317065.1","GCA_000010065.1","GCA_000018105.1","GCA_003149375.1"]
euk_keeplist=["EP00002","EP00003","EP00004","EP01087","EP00006","EP01091","EP01094","EP01104","EP00727","EP01109","EP00023","EP00026","EP01113","EP01114","EP01117","EP00029","EP01125","EP01127","EP01130","EP00031","EP01086","EP00033","EP00039","EP01147","EP00046","EP00794","EP00795","EP00057","EP00058","EP00059","EP00067","EP00072","EP00080","EP00081","EP00083","EP00098","EP00103","EP00104","EP00106","EP00107","EP00109","EP00110","EP00112","EP00113","EP00115","EP00117","EP00119","EP00120","EP01134","EP00123","EP01135","EP00127","EP00857","EP00865","EP00129","EP00131","EP00134","EP00145","EP00150","EP00157","EP00158","EP00162","EP00163","EP00164","EP00736","EP00167","EP00169","EP00176","EP00185","EP00852","EP00202","EP00206","EP00210","EP00738","EP00229","EP00895","EP00247","EP00248","EP00260","EP00269","EP00271","EP00741","EP00279","EP00298","EP00300","EP00314","EP00900","EP00810","EP00333","EP00348","EP00742","EP00820","EP00927","EP00931","EP00379","EP00390","EP00397","EP00454","EP00455","EP00808","EP00457","EP00466","EP00473","EP01084","EP01083","EP00797","EP01082","EP00903","EP00813","EP01138","EP01029","EP00924","EP00749","EP00750","EP00503","EP00513","EP00530","EP00609","EP00611","EP00625","EP00645","EP00654","EP00753","EP00656","EP01062","EP00667","EP00671","EP00681","EP00759","EP01027","EP00761","EP00686","EP01080","EP00762","EP01028","EP00696","EP00697","EP00698","EP00802","EP00792","EP01146","EP00705","EP00770"]

# filter_fastas_keep_sp(euk_keeplist, indir, outdir, species_id_delimiter="-", euk=True)

exclude_list =["EP00480", "EP01006"] # remove Ploetia (misidentified) and Reticulomyxa (long branched) 

indir="/Users/vl18625/work/euk/markers_euks/nina_markers/be/euk_c20_monobranch_sets_fastas/"
outdir="/Users/vl18625/work/euk/markers_euks/nina_markers/be/euk_c20_monobranch_sets_filtered_fastas/"

filter_fastas_exclude_sp(exclude_list, indir, outdir, species_id_delimiter="-")