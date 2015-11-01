#!/usr/bin/python
import sys
sys.path.append('/home/anna/bioinformatics/hts_repository')
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
global THREADS; THREADS = 8

def file_from_path(path):
    head, tail = split(path)
    return tail

def reverse(seq):
 	complement = maketrans('ATGC', 'TACG')
	reverse = seq.translate(complement)[::-1]
	return reverse

def flash_merge(file_fw, file_rv, outdir, flash_dir = None):
	if not flash_dir: flash_dir = '/home/anna/bioinformatics/bioprograms/FLASH/'
	flash_output = outdir + 'flash_out/'
	if not os.path.exists(flash_output):
	    os.makedirs(flash_output)

	options_flash = ['-d', flash_output, '-O', '-M 300', '-x 0.25']
	flash = flash_dir + './flash'
	flash_merge = [flash] + options_flash + [file_fw, file_rv]
	subprocess32.call(flash_merge)
	return flash_output

def use_fuzznuc (reads, pattern, outdir = None, max_mismatch = 5, stdout = None, indels = None, name = ''):
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

def find_spacers_fuzznuc(reads):
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
	return spacers

def use_bowtie2 (reference, outdir, unpaired=None, reads1=None, reads2=None, keep_unaligned=None, bowtie2_dir=None):
	if not bowtie2_dir: bowtie2_dir = '/home/anna/bioinformatics/bioprograms/bowtie2-2.2.3/'
	bowtie2_out = outdir + file_from_path(reference)[0:-6]
	if not os.path.exists(bowtie2_out): os.makedirs(bowtie2_out)
	bt2_base = bowtie2_out + 'bt2_base'
	bowtie2_build = [bowtie2_dir + './bowtie2-build', '-q', reference, bt2_base]
	subprocess32.call(bowtie2_build)
	sam_file = bowtie2_out + 'alignment.sam'
	bowtie2 = [bowtie2_dir + './bowtie2']
	if reads1 and reads2:
		options = ['-p', str(THREADS), '--reorder', '-x', bt2_base, '-1', reads1, '-2', reads2, '-S', sam_file]
	elif unpaired:
		options = ['-p', str(THREADS), '--reorder', '-x', bt2_base, '-f', '-U', unpaired, '-S', sam_file]
	else: print "Error. Function use_bowtie2: wrong set of arguments"
	if keep_unaligned: 
		unaligned = bowtie2_out + 'unaligned.fasta'
		# , '--no-mixed', '--no-discordant'
		options = ['--un', unaligned] + options
	call_bowtie2 = bowtie2 + options
	subprocess32.call(call_bowtie2)
	return bowtie2_out

def handle_hts (file_fw, file_rv, outdir, reference = None):
	spacers1 = find_spacers_fuzznuc(file_fw)
	spacers2 = find_spacers_fuzznuc(file_rv)
	spacers = spacers1 + spacers2
	spacers_file = outdir + 'spacers.fasta'
	SeqIO.write(spacers, spacers_file, "fasta")
	if USE_BOWTIE2 and reference:
		use_bowtie2 (reference, outdir, unpaired=spacers_file, keep_unaligned=True)
	return 0

def handle_files (workdir, file_fw = None, file_rv = None, hts_dir = None, htses = None, reference = None):
	if file_fw and file_rv:
		name_reads = file_from_path(file_fw)[0:-6]
		outdir = workdir + name_reads + '/'
		handle_hts (file_fw, file_rv, outdir, reference = reference)

	elif hts_dir and htses:
		process_count = 0
		for fw, rv in htses:
			file_fw = hts_dir + fw
			file_rv = hts_dir + rv
			name_fw = file_from_path(file_fw)
			name_rv = file_from_path(file_rv)
			name_reads = name_fw[0:-6]
			outdir = workdir + name_reads + '/'
			if not os.path.exists(outdir): os.makedirs(outdir)
			if not MULTIPROC:
				if not ONLY_FIND: handle_hts (file_fw, file_rv, outdir)
				else: handle_hts (file_fw, file_rv, outdir)
			else:
				pid = os.fork()
				time.sleep(0.1)
				if pid == 0:
					if not ONLY_FIND: handle_hts (file_fw, file_rv, outdir)
					else: handle_hts (file_fw, file_rv, outdir)
					os.abort()
				else:
					process_count += 1
					if process_count >= MAX_PROCESSES:
						os.wait()
						process_count -= 1
			
	else: print "Error: handle_htses haven't get needed values"
	return 0

file_fw = '/home/anna/bioinformatics/htses/T5adapt_ACTTGA_L001_R1_001.fastq'
file_rv = '/home/anna/bioinformatics/htses/T5adapt_ACTTGA_L001_R2_001.fastq'
# file_fw = '/home/anna/bioinformatics/htses/T4bi_1.fastq'
# file_rv = '/home/anna/bioinformatics/htses/T4bi_2.fastq'
# file_fw = '/home/anna/bioinformatics/htses/T4ai_AGTTCC_L001_1.fastq'
# file_rv = '/home/anna/bioinformatics/htses/T4ai_AGTTCC_L001_2.fastq'
workdir = '/home/anna/bioinformatics/outdirs/'
# reference = '/home/anna/bioinformatics/references/pt7blue-T4.fasta'
# reference = '/home/anna/bioinformatics/htses/pT7blue-G8esc_rev.fasta'
# reference = '/home/anna/bioinformatics/references/t5.fasta
# reference = '/home/anna/bioinformatics/references/first_10_kb_t5.fasta'
# reference = '/home/anna/bioinformatics/references/CRISPR_repeat.fasta'
reference = '/home/anna/bioinformatics/references/sasha/SS_39_CRISPR.fasta'

handle_files (workdir, file_fw=file_fw, file_rv=file_rv, reference=reference)
# use_fuzznuc (file_fw, pattern, outdir)


# reference = '/home/anna/bioinformatics/references/CRISPR_repeat.fasta'
# reference = '/home/anna/bioinformatics/outdirs/pBad.fasta'
# reference = '/home/anna/bioinformatics/outdirs/BL21.fasta'
# reference = '/home/anna/bioinformatics/references/BW25113.fasta'

# reference = '/home/anna/bioinformatics/pt7blue-T4.fasta'
# reference = '/home/anna/bioinformatics/references/sasha/SS_39_CRISPR.fasta'
# reference = '/home/anna/bioinformatics/references/t5.fasta'
reference = '/home/anna/bioinformatics/references/first_10_kb_t5.fasta'
# reference = '/home/anna/bioinformatics/htses/pT7blue-G8esc_rev.fasta'
# reference = '/home/anna/bioinformatics/outdirs/plasmid70_TGACCA_L001_R1_001/contigs_plasmid70.fasta'
# reference = '/home/anna/bioinformatics/outdirs/plasmid70_TGACCA_L001_R1_001/contig_87kb.fasta'
# unpaired = '/home/anna/bioinformatics/outdirs/T5adapt_ACTTGA_L001_R1_001/spacers.fasta'
# unpaired = '/home/anna/bioinformatics/outdirs/T5adapt_ACTTGA_L001_R1_001/bowtie2_out_t5/unaligned_on_t5.fasta'
unpaired = '/home/anna/bioinformatics/outdirs/T5adapt_ACTTGA_L001_R1_001/bowtie2_out_SS_39_CRISPR/unaligned.fasta'

outdir = '/home/anna/bioinformatics/outdirs/T5adapt_ACTTGA_L001_R1_001/'
# reads1 = '/home/anna/bioinformatics/htses/plasmid70_TGACCA_L001_R1_001.fastq'
# reads2 = '/home/anna/bioinformatics/htses/plasmid70_TGACCA_L001_R2_001.fastq'

# outdir = cr_outdir(reads1, reference, workdir)
# outdir = cr_outdir(unpaired, reference, workdir)

# use_bowtie2 (reference, outdir, reads1=reads1, reads2=reads2, keep_unaligned=True, bowtie2_dir=None)
use_bowtie2 (reference, outdir, unpaired=unpaired, keep_unaligned=None)