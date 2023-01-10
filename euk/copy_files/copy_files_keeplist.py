#!/usr/bin/python
import shutil
import os

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

def copy_files(ids_list, indir, outdir, delimiter="."):
	for file_name in listdir_nohidden(indir):
		id = file_name.split(delimiter)[0]
		if id in ids_list:
			print ("copying", file_name)
			file_path = indir + file_name
			outpath = outdir + file_name
			shutil.copyfile(file_path, outpath)
	return 0

keep_list = ["COG0074","COG0459","COG2857","COG0567","COG1894","COG1485","COG0443","COG0087","COG0022","COG0479","COG2609","COG1612","COG3175","COG0355","COG0277","COG1220","COG0114","COG0532","COG0216","COG0292","COG0100","COG0091","COG0445","COG0016","COG0377","COG0064","COG0090","COG0224","COG0143","COG1217","COG0030","COG0576","COG4799","COG3346","COG0508","COG0050","COG0055","COG0636","COG1562","COG0843","COG1104","COG1622","COG2009","COG0197","COG0103","COG1290","COG0635","COG0354","COG1905","COG0356","COG0740","COG0088","COG0056","COG1845","COG0304","COG0820","COG1008","COG0713","COG1034"]
indir = "/Users/vl18625/work/euk/markers_euks/nina_markers/be/be_c20/after_filtering/linsi_bmge/"
outdir = "/Users/vl18625/work/euk/markers_euks/nina_markers/be/be_c20/after_filtering/for_be_concat/"

keep_list = ["arCOG00410","arCOG00412","arCOG00780","arCOG00781","arCOG00809","arCOG00987","arCOG01001","arCOG01179","arCOG01183","arCOG01227","arCOG01344","arCOG01563","arCOG01722","arCOG01758","arCOG01946","arCOG04050","arCOG04067","arCOG04071","arCOG04088","arCOG04089","arCOG04090","arCOG04091","arCOG04092","arCOG04093","arCOG04095","arCOG04098","arCOG04099","arCOG04126","arCOG04154","arCOG04208","arCOG04245","arCOG04254","arCOG04277","arCOG04289"]
indir="/Users/vl18625/work/euk/markers_euks/nina_markers/ae/68_final_ae_markers/linsi_bmge/"
outdir="/Users/vl18625/work/euk/markers_euks/nina_markers/ae/non_asgard_only/linsi_bmge/"
copy_files(keep_list, indir, outdir)