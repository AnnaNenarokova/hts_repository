import os
from ntpath import split
from subprocess32 import call
from string import maketrans
from Bio import SeqIO
# from fuzzysearch import find_near_matches

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

def find_spacers_fuzzysearch(repeat_fw, seq, max_distance, spacers_array):
	spacers = []
	repeat_rv = reverse(repeat_fw)
	repeat_matches_fw = find_near_matches(repeat_fw, seq, max_l_dist = max_distance)
	repeat_matches_rv = find_near_matches(repeat_rv, seq, max_l_dist = max_distance)
	if not (len(repeat_matches_fw) <= 0 and len(repeat_matches_rv) <= 0): 
		if len(repeat_matches_fw) >= len(repeat_matches_rv):
			for i in range(len(repeat_matches_fw)-1):
				spacer_start = repeat_matches_fw[i].end + 1
				spacer_end = repeat_matches_fw[i+1].start
				spacer = seq[spacer_start : spacer_end]
		 		if len(spacer) in range (28, 31): 
		 			spacers.append(spacer)
		else:
			seq = reverse(seq)
			for i in range(len(repeat_matches_rv)-1):
				spacer_start = repeat_matches_rv[i].end + 1
				spacer_end = repeat_matches_rv[i+1].start
				spacer = seq[spacer_start : spacer_end]
		 		if len(spacer) in range (29, 31): 
		 			spacers.append(spacer)
		if len(spacers)>0 : spacers_array.append(spacers)
	return 0

def use_fuzznuc (reads, pattern, outdir, max_mismatch = 5, indels = False):
	fuzznuc_file = outdir + 'fuzznuc_report'
	fuzznuc = ['fuzznuc', '-sequence', reads, '-pattern', pattern, '-outfile', fuzznuc_file]
	fuzznuc_options = ['-pmismatch', str(max_mismatch), '-complement', '-snucleotide1', '-squick1', 
					   '-rformat2', 'excel']
	fuzznuc = fuzznuc + fuzznuc_options
	call(fuzznuc)
	return fuzznuc_file

def find_spacers_fuzznuc(reads, outdir, repeat = 'GAGTTCCCCGCGCCAGCGGGGATAAACCGC'):
	spacers = []
	fuzznuc_file = use_fuzznuc(reads, repeat, outdir)
	return spacers

def handle_HTS (file_fw, file_rv, outdir, only_find = False):

	if only_find == True: 
		flash_output = outdir + 'flash_out/'
	else: 
		flash_output = flash_merge(file_fw, file_rv, outdir)

	combined_reads = flash_output + 'out.extendedFrags.fastq'
	find_spacers_fuzznuc(combined_reads, outdir)
	return 0

def handle_files (workdir, file_fw = False, file_rv = False, HTS_dir = False, HTSes = False, only_find = False):
	if file_fw and file_rv:
		name_reads = file_from_path(file_fw)[0:-6]
		outdir = workdir + name_reads + '/'

		if not only_find: 
			handle_HTS (file_fw, file_rv, outdir)
		else: 
			handle_HTS (file_fw, file_rv, outdir, only_find = True)

	elif HTS_dir and HTSes:
		for fw, rv in HTSes:
			file_fw = HTS_dir + fw
			file_rv = HTS_dir + rv
			name_fw = file_from_path(file_fw)
			name_rv = file_from_path(file_rv)
			name_reads = name_fw[0:-6]
			outdir = workdir + name_reads + '/'
			print outdir
			if not os.path.exists(outdir): os.makedirs(outdir)
			if not only_find: 
				handle_HTS (file_fw, file_rv, outdir)
			else: 
				handle_HTS (file_fw, file_rv, outdir, only_find = True)

	else: print "Error: handle_HTSes haven't get needed values"

	return 0



workdir = '/home/anna/bioinformatics/HTS-all/HTS-programming/'

# file_fw = '/home/anna/bioinformatics/HTS-all/HTSes/CTG_CCGTCC_L001_1.fastq'
# file_rv = '/home/anna/bioinformatics/HTS-all/HTSes/CTG_CCGTCC_L001_2.fastq'

# handle_files(workdir, file_fw, file_rv, only_find = False)

HTS_dir = '/home/anna/bioinformatics/HTS-all/HTSes/'
HTSes = [('CTG_CCGTCC_L001_1.fastq', 'CTG_CCGTCC_L001_2.fastq'), ('Kan-frag_ATGTCA_L001_1.fastq', 'Kan-frag_ATGTCA_L001_2.fastq'),  
('T4ai_AGTTCC_L001_1.fastq', 'T4ai_AGTTCC_L001_2.fastq'), ('T4bi_1.fastq', 'T4bi_2.fastq'), ('T4C1T_TAGCTT_L001_1.fastq', 'T4C1T_TAGCTT_L001_2.fastq')]
handle_files(workdir, HTS_dir = HTS_dir, HTSes = HTSes)