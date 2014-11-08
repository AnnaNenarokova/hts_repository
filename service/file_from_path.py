from ntpath import split
def file_from_path(path):
    head, tail = split(path)
    return tail
def cr_outdir(f, workdir):
	name = file_from_path(f)[0:-6]
	outdir = workdir + name + '/'
	if not os.path.exists(outdir): os.makedirs(outdir)
	return outdir