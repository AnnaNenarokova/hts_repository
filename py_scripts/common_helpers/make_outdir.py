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

def name_outdir(f_path, workdir=False, subfolder='/', endcut=6):
	name = file_from_path(f_path, endcut=endcut) + '/'
	if workdir: outdir = workdir + subfolder + name
	else: outdir = file_from_path(f_path, folder=True) + subfolder + name
	return outdir

def make_outdir(f_path, workdir=False, subfolder='/', endcut=6):
	outdir = name_outdir(f_path, workdir, subfolder, endcut=endcut)
	if not exists(outdir): makedirs(outdir)
	return outdir