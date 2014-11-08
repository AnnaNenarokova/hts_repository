#!/usr/bin/python
import os
import csv
from ntpath import split
import subprocess32
from string import maketrans
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

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

def use_fuzznuc (reads, pattern, max_mismatch = 0, indels = False, name = ''):
	fuzznuc = ['fuzznuc', '-sequence', reads, '-pattern', pattern]
	fuzznuc_options = ['-pmismatch', str(max_mismatch), '-complement', '-snucleotide1', '-squick1', 
					   '-rformat2', 'excel', '-stdout', '-auto']
	fuzznuc = fuzznuc + fuzznuc_options
	fuzznuc_out = subprocess32.Popen((fuzznuc), stdout=subprocess32.PIPE, bufsize=100)
	return fuzznuc_out

def find_spacers_fuzznuc(reads, outdir):
	output_pipe = use_fuzznuc(reads, REPEAT).stdout
	for line in iter(output_pipe.readline, ''):
		row = line.split('\t')
		repeat_matches = []
		i = 0
		if row[0] != 'SeqName':
			repeat_matches.append({ 'SeqName': row[0], 'Start': row[1], 'End': row[2], 'Strand': row[4], 'Mismatch': row[6] })
			i+=1
		if (repeat_matches[i]['SeqName'] == seq_record.id):
			if repeat_matches[i]['Strand'] == '+':
				seq = SeqRecord(seq_record.seq[spacer_start:spacer_end], id = repeat_matches[i]['SeqName']+' '+str(cur_sp_n), description = '')
			elif repeat_matches[i]['Strand'] == '-':
				seq = SeqRecord(seq_record.seq.reverse_complement()[spacer_start:spacer_end], id = repeat_matches[i]['SeqName']+' '+str(cur_sp_n), description = '')
			else: print("Error in find_spacers_fuzznuc")
			if len(spacer.seq) in range (29, 31): 
				spacers[-1].append(spacer)
				sp_fasta_out.append(spacer)
				spacers_number +=1
				sp_in = True
			else: cur_sp_n-=1
			spacer_start = int(repeat_matches[i]['End'])
			i+=1
		if not sp_in: spacers.pop()
		k+=1

	# sp_fasta_out = [f for f in sorted(sp_fasta_out, key=lambda x : str(x.seq))]
	# SeqIO.write(sp_fasta_out, spacers_fasta, "fasta")
	# return spacers

reads = '/home/anna/bioinformatics/htses/T4bi_1.fastq'
outdir = '/home/anna/bioinformatics/outdirs'
find_spacers_fuzznuc(reads, outdir)
