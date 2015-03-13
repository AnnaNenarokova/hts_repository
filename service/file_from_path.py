#!/usr/bin/python
from ntpath import split
def file_from_path(path, folder=False):
    head, tail = split(path)
    if folder: return head
    else: return tail

def cr_outdir(f, workdir=False):
	name = file_from_path(f)[0:-6]
	if workdir: outdir = workdir + name + '/'
	else: outdir = file_from_path(f, folder=True) + name + '/'
	if not os.path.exists(outdir): os.makedirs(outdir)
	return outdir