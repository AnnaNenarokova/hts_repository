import os
from subprocess import call
import ntpath
from string import maketrans
# from Bio.Seq import Seq
from Bio import SeqIO
from fuzzysearch import find_near_matches

def file_from_path(path):
    head, tail = ntpath.split(path)
    dir_path = [head, tail]
    return tail

def reverse(seq):
 	complement = maketrans('ATGC', 'TACG')
	reverse = seq.translate(complement)[::-1]
	return reverse

def merge_by_flash(flash_dir, file_fw, file_rv, output_dir):

	name_reads = file_from_path(file_fw)[0:-6]

	flash_output = output_dir + 'FlashOutput/'
	print flash_output

	if not os.path.exists(flash_output):
	    os.makedirs(flash_output)

	options_flash = ['-d', flash_output, '-o', name_reads, '-O', '-M 250', '-x 0.25']
	flash = flash_dir + './flash'
	merge_by_flash = [flash] + options_flash + [file_fw, file_rv]
	# print merge_by_flash
	print ' '.join(merge_by_flash)
	call(merge_by_flash)
	return flash_output

def find_spacers(repeat_fw, seq, max_distance, spacers_array):
	spacers = []
	repeat_rv = reverse(repeat_fw)
	matches_fw = find_near_matches(repeat_fw, seq, max_l_dist = max_distance)
	matches_rv = find_near_matches(repeat_rv, seq, max_l_dist = max_distance)
	# print "FORWARD", matches_fw, "REVERSE", matches_rv
	if not (len(matches_fw) <= 0 and len(matches_rv) <= 0): 
		if len(matches_fw) >= len(matches_rv):
			for i in range(len(matches_fw)-1):
				spacer_start = matches_fw[i].end + 1
				spacer_end = matches_fw[i+1].start
				spacer = seq[spacer_start : spacer_end]
		 		if len(spacer) in range (28, 31): 
		 			spacers.append(spacer)
		else:
			seq = reverse(seq)
			for i in range(len(matches_rv)-1):
				spacer_start = matches_rv[i].end + 1
				spacer_end = matches_rv[i+1].start
				spacer = seq[spacer_start : spacer_end]
		 		if len(spacer) in range (29, 31): 
		 			spacers.append(spacer)
		print len(spacers),
		if len(spacers)>0 : spacers_array.append(spacers)
	return 0

work_dir = '/home/anna/HTS-all/HTS-programming/'
# file_fw = '/home/anna/HTS-all/HTSes/CTG_CCGTCC_L001_1.fastq'
# file_rv = '/home/anna/HTS-all/HTSes/CTG_CCGTCC_L001_2.fastq'

file_fw = '/home/anna/HTS-all/HTS-programming/100_CTG_CCGTCC_L001_1.fastq'
file_rv = '/home/anna/HTS-all/HTS-programming/100_CTG_CCGTCC_L001_2.fastq'
# file_fw = '/home/anna/HTS-all/HTS-programming/1000_Kan-frag_ATGTCA_L001_1.fastq'
# file_rv = '/home/anna/HTS-all/HTS-programming/1000_Kan-frag_ATGTCA_L001_2.fastq'

name_fw = file_from_path(file_fw)
name_rv = file_from_path(file_rv)
name_reads = name_fw[0:-6]
output_dir = work_dir + name_reads + '/'

input_dir = '/home/anna/HTS-all/HTSes/'
HTSes = [('CTG_CCGTCC_L001_1.fastq', 'CTG_CCGTCC_L001_2.fastq'), ('Kan-frag_ATGTCA_L001_1.fastq', 'Kan-frag_ATGTCA_L001_2.fastq'),  
('T4ai_AGTTCC_L001_1.fastq', 'T4ai_AGTTCC_L001_2.fastq'), ('T4bi_1.fastq', 'T4bi_2.fastq'), ('T4C1T_TAGCTT_L001_1.fastq', 'T4C1T_TAGCTT_L001_2.fastq')]

# flash_output = merge_by_flash(work_dir, file_fw, file_rv, output_dir)
flash_output = '/home/anna/HTS-all/HTS-programming/100_CTG_CCGTCC_L001_1/FlashOutput/'
# print flash_output
combined_reads = flash_output + name_reads + '.extendedFrags.fastq'

reads = SeqIO.parse(combined_reads, "fastq")
repeat_fw = 'GAGTTCCCCGCGCCAGCGGGGATAAACCGC'
spacers_array= []
max_distance = 2

for read in reads:
	seq = str(read.seq)
	find_spacers(repeat_fw, seq, max_distance, spacers_array)

print len(spacers_array)
print spacers_array
# for fw, rv in HTSes:
# 	file_fw = input_dir + fw
# 	file_rv = input_dir + rv
# 	name_fw = file_from_path(file_fw)
# 	name_rv = file_from_path(file_rv)
# 	name_reads = name_fw[0:-6]
# 	output_dir = work_dir + name_reads + '/'
# 	print output_dir
# 	if not os.path.exists(output_dir):
# 		os.makedirs(output_dir)

# 	merge_by_flash(work_dir, file_fw, file_rv, output_dir)

# for output_flash in ('.extendedFrags.fastq', '.notCombined_1.fastq', '.notCombined_2.fastq'):
#     file_fastq = output_dir + 'FlashOutput/' + name_reads +  output_flash
#     file_fasta = file_fastq[0:-1] + 'a'
#     SeqIO.convert (file_fastq, "fastq", file_fasta, "fasta")

# for f in (name_fw, name_rv):
# 	file_fastq = work_dir + '/' + f
# 	file_fasta = output_dir + '/' + f[0:-1] + 'a'
# 	SeqIO.convert (file_fastq, "fastq", file_fasta, "fasta")

# seqs = ('CGGCATCACCTTTGGCTTCGGCTGCGGTTTCTCCCCGCTGGCGCGGGGAACTCTGCGTAAGCGTATCGCCGCGCGTCTGCGAAAGCGGTTTATCCCCGCTGGCGCGGGGAACTCGCGGGATCGTCACCCTCAGCAGCGAAAGACAGTGGTTTATCCTCGCTGGTGCGGGGAACTCTCTAAAAGCTTACATTTGTTCTTAAAGCATTTTTTTCCATAAAAACAACCCATCAACCTTAGATCGGAAGAGCAC',
#  	'NAGGTTGGTGGGTTGTTTTTATGGGATAAAATGCTTTAAGAACAAATGTATACTTTTAGAGAGTTCCCCGCGCCAGCGGGGATAAACCGTTGTCTTTCGCTGCTGAGGGTGACGATCCCGCGAGTTCCCTGCGCCAGGGGGGATAAACCGCTTTCGCAGACGCGCGGCGATACGCTCACGCAGAGTTGCCCGCGCCAGCGGGGATCAACCGCAGCCGAAGGCAAAGGTGATGACGAGATTGGAAGAGCGG',
#  	'CCGTCCGCGCGCTTCCGATCTCGGCATCACCTTTGGCTTCGGCTGCGGTTTATCCCCGCTGGCGCGGGGAACTCTGCGTGAGCGTATCGCCGCGCGTCTGCGAAAGCGGTTTATCCCCGCTGGCGCGGGGAACTCGCGGGATCGTCACCCTCAGCAGCGAAAGACAGCGGTTTATCCCCGCTGGCGCGGGGAACTCTCTAAAAGTATACATTTGTTCTTAAAGCATTTTTTCCCATAAAAACAACCCACCAACCTTAGATCGGAAGAGCAC')

# for seq in seqs:
# 	for max_distance in range(3, 5):
#  		find_spacers(repeat_fw, seq, max_distance, spacers_array)

# file_fasta = output_dir + '/' + name_reads + '.notCombined_2.fasta'
# rev_comp = file_fasta[0:-6] + 'revcomp' + '.fasta' 
# records = (rec.reverse_complement(id = "rc_"+rec.id, description = "reverse complement") \
# 			for rec in SeqIO.parse(file_fasta, "fasta") )
# SeqIO.write(records, rev_comp, "fasta")
