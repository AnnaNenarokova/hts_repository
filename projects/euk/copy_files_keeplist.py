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

def copy_files(ids_path, indir, outdir):
	ids_list = read_list(ids_path)
	for file_name in listdir_nohidden(indir):
		id = file_name.split("_")[0]
		if id in ids_list:
			print ("copying", file_name)
			file_path = indir + file_name
			outpath = outdir + file_name
			shutil.copyfile(file_path, outpath)
	return 0

ids_path = "/Users/anna/work/euk_local/eukprot/new_eukprot3_proteomes_list.txt"
indir = "/Users/anna/work/euk_local/eukprot/eukprot3/proteins/"
outdir = "/Users/anna/work/euk_local/eukprot/anna_eukprot3_proteome_dataset/"
copy_files(ids_path, indir, outdir)