#!/usr/bin/python

def read_list(list_path):
	result_list = []
	with open (list_path) as list_file:
		for line in list_file:
			result_list.append(line.rstrip())
	return result_list


ids_path = "/Users/vl18625/work/euk/134_euk_id_list.txt"

full_file_names_path = "/Users/vl18625/work/euk/euk_list.txt"

full_file_names_list = read_list(full_file_names_path)

ids_list = read_list(ids_path)

keep_files = []
for file_name in full_file_names_list:
	if file_name.split("_")[0] in ids_list:
		keep_files.append(file_name)

outfile_path = "/Users/vl18625/work/euk/get_132_proteomes.sh"
outdir = "/user/work/vl18625/euk/eukprot/132_euk_prots/"
with open(outfile_path, "w") as outfile:
	for file in keep_files:
		line = "cp " + file + " " + outdir + '\n'
		outfile.write(line)