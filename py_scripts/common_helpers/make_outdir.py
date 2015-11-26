#!/usr/bin/python
from ntpath import split
from os.path import exists
from os.path import basename
from os import makedirs
def file_from_path(path, endcut=0):
    tail = basename(path)
    if endcut == 0: return tail
    else: return tail[0:-endcut]

def dir_from_path(path, lift=0):
	upper_dir = path
	for i in range(lift + 1):
		upper_dir = split(upper_dir)[0]
	return upper_dir + '/'

def name_outdir(f_path, workdir=False, subfolder='', endcut=6):
	name = file_from_path(f_path, endcut=endcut) + '/'
	if workdir: outdir = workdir + subfolder + name
	else: outdir = dir_from_path(f_path) + subfolder + name
	return outdir

def make_outdir(f_path, workdir=False, subfolder='', endcut=6):
	outdir = name_outdir(f_path, workdir, subfolder, endcut=endcut)
	if not exists(outdir): makedirs(outdir)
	return outdir

def new_file_same_dir(oldfile_path, newfile_name=False, new_ext=False):
	cur_dir = dir_from_path(oldfile_path)
	if (newfile_name and not new_ext): 
		newfile_path = cur_dir + newfile_name
	elif (new_ext and not newfile_name):
		f_name = file_from_path(oldfile_path)
		without_ext = f_name.split('.')[0]
		newfile_path = cur_dir + without_ext + new_ext
	else:
		print "Error: Incomparible options"
		return "Error"
	return newfile_path