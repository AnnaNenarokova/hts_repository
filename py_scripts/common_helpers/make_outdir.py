#!/usr/bin/python
from ntpath import split
from os.path import exists
from os import makedirs
def file_from_path(path, folder=False, endcut=0):
    head, tail = split(path)
    if folder: return head
    else: return tail[0:-endcut]

def name_outdir(f_path, workdir=False, endcut=6):
	name = file_from_path(f_path, endcut=endcut)
	if workdir: outdir = workdir + '/' + name + '/'
	else: outdir = file_from_path(f_path, folder=True) + '/' +name + '/'
	return outdir

def make_outdir(f_path, workdir=False, endcut=6):
	outdir = name_outdir(f_path, workdir, endcut=endcut)
	if not exists(outdir): makedirs(outdir)
	return outdir