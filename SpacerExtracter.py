import os
from subprocess import call
from string import maketrans
# from Bio.Seq import Seq
from Bio import SeqIO
import rpy2.robjects as robjects
import rpy2.robjects.packages
from rpy2.robjects.packages import importr

biostrings = importr("Biostrings")
iranges = importr("IRanges")

def reverse(seq):
 	complement = maketrans('ATGC', 'TACG')
	reverse = seq.translate(complement)[::-1]
	return reverse

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

work_dir = '/home/anna/HTS_programming/HTS_spacers/'

name_fw = 'CTG_CCGTCC_L001_1.fastq'
name_rv = 'CTG_CCGTCC_L001_2.fastq'

file_fw = work_dir + name_fw
file_rv = work_dir + name_rv

name_reads = name_fw[0:-6]

output_dir = work_dir + name_reads

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

options_flash = ['-d' + output_dir, '-o' + name_reads, '-O', '-M 250', '-x 0.25']
merge_by_flash = ['./flash'] + options_flash + [file_fw, file_rv]

print
# call('cd '+ work_dir, shell = True)
# call(merge_by_flash)

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

# cutadapt_conf = ' -m 100 -a ACACTCTTTCCCTACACGACGCTCTTCCGATCT -a GATCGGAAGAGCGGTTCAGCAGGAATGCCGAG -a AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCT -a CAAGCAGAAGACGGCATACGAGATCGGTCTCGGCATTCCTGCTGAACCGCTCTTCCGATCT -a ACACTCTTTCCCTACACGACGCTCTTCCGATCT -a CGGTCTCGGCATTCCTGCTGAACCGCTCTTCCGATCT -a AGATCGGAAGAG '

# cutadapt_cmd_fw = 'cutadapt' +  cutadapt_conf + work_dir + name_fw + ' > ' + adapters_fw_file
# cutadapt_cmd_rv = 'cutadapt' +  cutadapt_conf + work_dir + name_rv + ' > ' + adapters_rv_file

# os.system(cutadapt_cmd_fw)
# os.system(cutadapt_cmd_rv)
