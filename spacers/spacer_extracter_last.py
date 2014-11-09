#!/usr/bin/python
import os
import csv
from ntpath import split
import subprocess32
from string import maketrans
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from natsort import natsorted

global ONLY_FIND; ONLY_FIND = False
global ONLY_SPACERS; ONLY_SPACERS = False
global MAX_PROCESSES; MAX_PROCESSES = 8
global REPEAT; REPEAT = 'GAGTTCCCCGCGCCAGCGGGGATAAACCGC'
global USE_BOWTIE2; USE_BOWTIE2 = True
global MULTIPROC; MULTIPROC = False 

def file_from_path(path):
    head, tail = split(path)
    return tail

def reverse(seq):
 	complement = maketrans('ATGC', 'TACG')
	reverse = seq.translate(complement)[::-1]
	return reverse

def flash_merge(file_fw, file_rv, outdir, flash_dir = False):
	if not flash_dir: flash_dir = '/home/anna/bioinformatics/bioprograms/FLASH/'
	flash_output = outdir + 'flash_out/'
	if not os.path.exists(flash_output):
	    os.makedirs(flash_output)

	options_flash = ['-d', flash_output, '-O', '-M 250', '-x 0.25']
	flash = flash_dir + './flash'
	flash_merge = [flash] + options_flash + [file_fw, file_rv]
	call(flash_merge)
	return flash_output

def use_fuzznuc (reads, pattern, outdir = False, max_mismatch = 5, stdout = False, indels = False, name = ''):
	if stdout:
		fuzznuc = ['fuzznuc', '-sequence', reads, '-pattern', pattern]
		fuzznuc_options = ['-pmismatch', str(max_mismatch), '-complement', '-snucleotide1', '-squick1', 
						   '-rformat2', 'excel', '-stdout', '-auto']
		fuzznuc = fuzznuc + fuzznuc_options
		fuzznuc_out = subprocess32.Popen((fuzznuc), stdout=subprocess32.PIPE, bufsize=100)
	else:
		fuzznuc_out = outdir + 'fuzznuc_report' + name
		fuzznuc = ['fuzznuc', '-sequence', reads, '-pattern', pattern, '-outfile', fuzznuc_out]
		fuzznuc_options = ['-pmismatch', str(max_mismatch), '-complement', '-snucleotide1', '-squick1', 
						   '-rformat2', 'excel']
		fuzznuc = fuzznuc + fuzznuc_options
		subprocess32.call(fuzznuc)

	return fuzznuc_out

def find_spacers_fuzznuc(reads, outdir):
	output_pipe = use_fuzznuc(reads, REPEAT, stdout = True).stdout
	spacers = []
	spacers_number = 0
	reads_iter = SeqIO.parse(reads, "fastq")
	read = next(reads_iter)
	last_repeat = None
	for line in iter(output_pipe.readline, ''):
		row = line.split('\t')
		if row[0] != 'SeqName':
			repeat = {'seq_id': row[0], 'start': row[1], 'end': row[2], 'strand': row[4]}
			if last_repeat:
				if repeat['seq_id'] == last_repeat['seq_id']:
					spacer_start = int(last_repeat['end'])
					spacer_end = int(repeat['start'])-1	
					while repeat['seq_id'] != read.id: 
						read = next(reads_iter)
					if repeat['strand'] == '+':
						spacer_seq = read.seq[spacer_start:spacer_end]
					elif repeat['strand'] == '-':
						spacer_seq = read.seq.reverse_complement()[spacer_start:spacer_end]
					else: print("Error in find_spacers_fuzznuc")
					if len(spacer_seq) in range (28, 33): 
						spacers_number +=1
						cur_spacer_n += 1
						description = 'CRISPR cassette ' + read.id[-11: len(read.id)]
						spacer = SeqRecord(spacer_seq, id = read.id + ' spacer ' + str(cur_spacer_n), description = description)
						spacers.append(spacer)
			last_repeat = repeat
		else: cur_spacer_n = 0
	print str(spacers_number) + ' spacers founded'
	spacers_file = outdir + 'spacers.fasta'
	SeqIO.write(spacers, spacers_file, "fasta")
	return spacers_file

reads = '/home/anna/bioinformatics/htses/T4bi_1.fastq'
outdir = '/home/anna/bioinformatics/outdirs/T4bi_1/'
find_spacers_fuzznuc(reads, outdir)
# use_fuzznuc (reads, REPEAT, outdir = outdir)