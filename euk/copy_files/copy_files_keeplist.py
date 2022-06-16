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



ids_list = ["COG0022","COG0037","COG0050","COG0055","COG0056","COG0064","COG0074","COG0087","COG0088","COG0091","COG0206","COG0292","COG0354","COG0355","COG0356","COG0377","COG0443","COG0445","COG0459","COG0479","COG0486","COG0508","COG0532","COG0533","COG0567","COG0576","COG0843","COG1007","COG1008","COG1104","COG1220","COG1485","COG1622","COG1845","COG1894","COG1905","COG2857","COG3175","COG3346","COG5405"]
indir = "/Users/vl18625/work/euk/markers_euks/nina_markers/be/be_mono_results/alpha/euk_alpha_fastas/"
outdir = "/Users/vl18625/work/euk/markers_euks/nina_markers/be/be_mono_results/alpha/be_alpha_40/"
copy_files(ids_list, indir, outdir)