#!/usr/bin/python
import os
from subprocess32 import call
from ntpath import split
global ONLY_TRIM; ONLY_TRIM = False
global ONLY_ASSEMBLE; ONLY_ASSEMBLE = True
global ONLY_ANNOTATE; ONLY_ANNOTATE = False
global THREADS; THREADS = 10


def spades_assemble(outdir, test=False, spades_dir=False, file_fw=False, file_rv=False, bbduk_out = False, trim_out=False, RAM=7):
	if not spades_dir: spades_dir = '/home/anna/bioinformatics/bioprograms/SPAdes-3.1.1-Linux/bin/'

	spades_out = outdir + 'spades_out/'
	spades = spades_dir + './spades.py'

	if test: spades_assemble= [spades, '--test'] # Test SPAdes

	else:

		if trim_out:
			files = {'PEfw' : 'paired_out_fw.fastq', 'PErv' : 'paired_out_rv.fastq', 
					 'UPfw': 'unpaired_out_fw.fastq', 'UPrv': 'unpaired_out_rv.fastq'}
			for key in files:
				files[key] = trim_out + files[key]
				spades_options = ['-1', files['PEfw'], '-2', files['PErv'], '-s', files['UPfw'], '-s', files['UPrv'], 
								  '-o', spades_out, '-m '+ str(RAM), '--careful']
				spades_assemble= [spades] + spades_options

		elif file_fw and file_rv:
			spades_options = ['-o', spades_out, '-m '+ str(RAM), '-t '+ str(THREADS), '--careful']
			spades_assemble = [spades, '-1', file_fw, '-2', file_rv] + spades_options

		else: print "Error: spades_assemble haven't get needed values"

		if not os.path.exists(spades_out): os.makedirs(spades_out)
		print(' '.join(spades_assemble))
		call(spades_assemble)
		
	return spades_out

outdir = '/home/anna/bioinformatics/hts/outdirs/'
file_fw = '/home/anna/bioinformatics/hts/htses/dasha/Ecoli-B_trimmed_paired_R1.fastq'
file_rv = '/home/anna/bioinformatics/hts/htses/dasha/Ecoli-B_trimmed_paired_R2.fastq'
spades_assemble(outdir, file_fw=file_fw, file_rv=file_rv)
