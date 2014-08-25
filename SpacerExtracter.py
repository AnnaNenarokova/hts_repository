import os
from subprocess import call
import ntpath
from string import maketrans
# from Bio.Seq import Seq
from Bio import SeqIO
import rpy2.robjects as robjects
import rpy2.robjects.packages
from rpy2.robjects.packages import importr


biostrings = importr("Biostrings")
iranges = importr("IRanges")

def file_from_path(path):
    head, tail = ntpath.split(path)
    dir_path = [head, tail]
    return tail

def reverse(seq):
 	complement = maketrans('ATGC', 'TACG')
	reverse = seq.translate(complement)[::-1]
	return reverse

def merge_by_flash(flash, file_fw, file_rv, output_dir):
	
	name_reads = file_from_path(file_fw)[0:-6]

	flash_output = output_dir + 'FlashOutput/'
	print flash_output

	if not os.path.exists(flash_output):
	    os.makedirs(flash_output)

	options_flash = ['-d', flash_output, '-o', name_reads, '-O', '-M 250', '-x 0.25']
	merge_by_flash = [flash] + options_flash + [file_fw, file_rv]
	# print merge_by_flash
	print ' '.join(merge_by_flash)
	call(merge_by_flash)
	return 0

def find_spacers(repeat_fw, seq, maxmismatch, spacers_array):
	repeat_rv = reverse(repeat_fw)
	seq = biostrings.DNAString(seq)
	positions_fw = biostrings.matchPattern(repeat_fw, seq, max_mismatch = maxmismatch, min_mismatch = 0, with_indels = True, fixed = True, algorithm = "auto")
	positions_rv = biostrings.matchPattern(repeat_rv, seq, max_mismatch = maxmismatch, min_mismatch = 0, with_indels = True, fixed = True, algorithm = "auto")

	matrix = iranges.as_matrix(positions_fw)
	print "FORWARD"
	print positions_fw
	print "REVERSE"
	print positions_rv
	print ('as matrix')
	print matrix
	return 0

# file_fw = '/home/anna/HTS-all/HTS-programming/CTG_CCGTCC_L001_1.fastq'
# file_rv = '/home/anna/HTS-all/HTS-programming/CTG_CCGTCC_L001_2.fastq'

file_fw = '/home/anna/BISS2014/EcoliProject/Stuff/1.fastq'
file_rv = '/home/anna/BISS2014/EcoliProject/Stuff/2.fastq'

work_dir = '/home/anna/HTS-all/HTS-programming/'

name_fw = file_from_path(file_fw)
name_rv = file_from_path(file_rv)

name_reads = name_fw[0:-6]

output_dir = work_dir + name_reads + '/'

input_dir = '/home/anna/HTS-all/HTSes/'
HTSes = [('CTG_CCGTCC_L001_1.fastq', 'CTG_CCGTCC_L001_2.fastq'), ('Kan-frag_ATGTCA_L001_1.fastq', 'Kan-frag_ATGTCA_L001_2.fastq'),  
('T4ai_AGTTCC_L001_1.fastq', 'T4ai_AGTTCC_L001_2.fastq'), ('T4bi_1.fastq', 'T4bi_2.fastq'), ('T4C1T_TAGCTT_L001_1.fastq', 'T4C1T_TAGCTT_L001_2.fastq')]

for fw, rv in HTSes:
	file_fw = input_dir + fw
	file_rv = input_dir + rv
	name_fw = file_from_path(file_fw)
	name_rv = file_from_path(file_rv)
	name_reads = name_fw[0:-6]
	output_dir = work_dir + name_reads + '/'
	print output_dir
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)

	flash = work_dir + './flash'

	merge_by_flash(flash, file_fw, file_rv, output_dir)
	#trimmomate (trimc_dir, file_fw, file_rv, output_dir)

# for output_flash in ('.extendedFrags.fastq', '.notCombined_1.fastq', '.notCombined_2.fastq'):
#     file_fastq = output_dir + '/' + name_reads + output_flash
#     file_fasta = file_fastq[0:-1] + 'a'
#     SeqIO.convert (file_fastq, "fastq", file_fasta, "fasta")

# for f in (name_fw, name_rv):
# 	file_fastq = work_dir + '/' + f
# 	file_fasta = output_dir + '/' + f[0:-1] + 'a'
# 	SeqIO.convert (file_fastq, "fastq", file_fasta, "fasta")

# seqs = ('CGGCATCACCTTTGGCTTCGGCTGCGGTTTCTCCCCGCTGGCGCGGGGAACTCTGCGTAAGCGTATCGCCGCGCGTCTGCGAAAGCGGTTTATCCCCGCTGGCGCGGGGAACTCGCGGGATCGTCACCCTCAGCAGCGAAAGACAGTGGTTTATCCTCGCTGGTGCGGGGAACTCTCTAAAAGCTTACATTTGTTCTTAAAGCATTTTTTTCCATAAAAACAACCCATCAACCTTAGATCGGAAGAGCAC',
# 	'NAGGTTGGTGGGTTGTTTTTATGGGATAAAATGCTTTAAGAACAAATGTATACTTTTAGAGAGTTCCCCGCGCCAGCGGGGATAAACCGTTGTCTTTCGCTGCTGAGGGTGACGATCCCGCGAGTTCCCTGCGCCAGGGGGGATAAACCGCTTTCGCAGACGCGCGGCGATACGCTCACGCAGAGTTGCCCGCGCCAGCGGGGATCAACCGCAGCCGAAGGCAAAGGTGATGACGAGATTGGAAGAGCGG',
# 	'CCGTCCGCGCGCTTCCGATCTCGGCATCACCTTTGGCTTCGGCTGCGGTTTATCCCCGCTGGCGCGGGGAACTCTGCGTGAGCGTATCGCCGCGCGTCTGCGAAAGCGGTTTATCCCCGCTGGCGCGGGGAACTCGCGGGATCGTCACCCTCAGCAGCGAAAGACAGCGGTTTATCCCCGCTGGCGCGGGGAACTCTCTAAAAGTATACATTTGTTCTTAAAGCATTTTTTCCCATAAAAACAACCCACCAACCTTAGATCGGAAGAGCAC')

# repeat_fw = 'GAGTTCCCCGCGCCAGCGGGGATAAACCGC'
# max_mismatch = 3
# spacers_array = 0

# for string in seqs:
# 	seq = biostrings.DNAString(string)
# 	find_spacers(repeat_fw, seq, max_mismatch, spacers_array)

# adapters_fw_file = output_dir  + name_reads + '-adapters_fw.fastq'
# adapters_rv_file = output_dir  + name_reads + '-adapters_rv.fastq'

# file_fasta = output_dir + '/' + name_reads + '.notCombined_2.fasta'
# rev_comp = file_fasta[0:-6] + 'revcomp' + '.fasta' 
# records = (rec.reverse_complement(id = "rc_"+rec.id, description = "reverse complement") \
# 			for rec in SeqIO.parse(file_fasta, "fasta") )
# SeqIO.write(records, rev_comp, "fasta")
