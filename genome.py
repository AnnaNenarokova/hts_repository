#!/usr/bin/python
import os
from subprocess32 import call
from ntpath import split
global ONLY_TRIM; ONLY_TRIM = False
global ONLY_ASSEMBLE; ONLY_ASSEMBLE = True
global ONLY_ANNOTATE; ONLY_ANNOTATE = False
global THREADS; THREADS = 8
global RAM; RAM = 8

def file_from_path (path):
    head, tail = split(path)
    return tail

def cr_outdir(file_fw, file_rv, workdir):
	name_fw = file_from_path(file_fw)
	name_reads = name_fw[0:-6]
	outdir = workdir + name_reads + '/'
	if not os.path.exists(outdir): os.makedirs(outdir)
	return outdir

def handle_hts (file_fw, file_rv, outdir):
	if not ONLY_ASSEMBLE: 
		trim_out = bbduk_trim(file_fw, file_rv, outdir)
		if not ONLY_TRIM:
			spades_out = spades_assemble(outdir, trim_out)
			contigs = spades_out + 'contigs.fasta'
			prokka_annotate (contigs, outdir)
			# use_quast (contigs, reference, outdir)
			# scaffold_abacas (abacas_dir, contigs, reference, outdir)
	else: 
		# trim_out = outdir + 'bbduk_out/'
		velvet_out = velvet_assemble(outdir, file_fw=file_fw, file_rv=file_rv)
		
	return 0

def handle_files (workdir, file_fw=False, file_rv=False, hts_dir=False, htses=False):
	if file_fw and file_rv:
		outdir = cr_outdir(file_fw, file_rv, workdir)
		handle_hts (file_fw, file_rv, outdir)

	elif hts_dir and htses:
		for fw, rv in htses:
			file_fw = hts_dir + fw
			file_rv = hts_dir + rv
			outdir = cr_outdir(file_fw, file_rv, workdir)
			handle_hts (file_fw, file_rv, outdir)

	else: print "Error: handle_htses haven't get needed values"

	return 0

workdir = '/home/anna/bioinformatics/outdirs/'
file_fw = '/home/anna/bioinformatics/hts/htses/dasha/Ecoli-B_trimmed_paired_R1.fastq'
file_rv = '/home/anna/bioinformatics/hts/htses/dasha/Ecoli-B_trimmed_paired_R2.fastq'
handle_files(workdir, file_fw, file_rv)

# htses =[('CTG_CCGTCC_L001_1.fastq', 'CTG_CCGTCC_L001_2.fastq'), ('Kan-frag_ATGTCA_L001_1.fastq', 'Kan-frag_ATGTCA_L001_2.fastq'),  
# # ('T4ai_AGTTCC_L001_1.fastq', 'T4ai_AGTTCC_L001_2.fastq'), ('T4bi_1.fastq', 'T4bi_2.fastq'), ('T4C1T_TAGCTT_L001_1.fastq', 'T4C1T_TAGCTT_L001_2.fastq')]

# # hts_dir = '/home/anna/bioinformatics/hts/htses/'

# # handle_files(workdir, hts_dir = hts_dir, htses = htses)


