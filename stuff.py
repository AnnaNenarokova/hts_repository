# print spacers_array

# 	merge_by_flash(work_dir, file_fw, file_rv, outdir)

# for output_flash in ('.extendedFrags.fastq', '.notCombined_1.fastq', '.notCombined_2.fastq'):
#     file_fastq = outdir + 'FlashOutput/' + name_reads +  output_flash
#     file_fasta = file_fastq[0:-1] + 'a'
#     SeqIO.convert (file_fastq, "fastq", file_fasta, "fasta")

# for f in (name_fw, name_rv):
# 	file_fastq = work_dir + '/' + f
# 	file_fasta = outdir + '/' + f[0:-1] + 'a'
# 	SeqIO.convert (file_fastq, "fastq", file_fasta, "fasta")

# seqs = ('CGGCATCACCTTTGGCTTCGGCTGCGGTTTCTCCCCGCTGGCGCGGGGAACTCTGCGTAAGCGTATCGCCGCGCGTCTGCGAAAGCGGTTTATCCCCGCTGGCGCGGGGAACTCGCGGGATCGTCACCCTCAGCAGCGAAAGACAGTGGTTTATCCTCGCTGGTGCGGGGAACTCTCTAAAAGCTTACATTTGTTCTTAAAGCATTTTTTTCCATAAAAACAACCCATCAACCTTAGATCGGAAGAGCAC',
#  	'NAGGTTGGTGGGTTGTTTTTATGGGATAAAATGCTTTAAGAACAAATGTATACTTTTAGAGAGTTCCCCGCGCCAGCGGGGATAAACCGTTGTCTTTCGCTGCTGAGGGTGACGATCCCGCGAGTTCCCTGCGCCAGGGGGGATAAACCGCTTTCGCAGACGCGCGGCGATACGCTCACGCAGAGTTGCCCGCGCCAGCGGGGATCAACCGCAGCCGAAGGCAAAGGTGATGACGAGATTGGAAGAGCGG',
#  	'CCGTCCGCGCGCTTCCGATCTCGGCATCACCTTTGGCTTCGGCTGCGGTTTATCCCCGCTGGCGCGGGGAACTCTGCGTGAGCGTATCGCCGCGCGTCTGCGAAAGCGGTTTATCCCCGCTGGCGCGGGGAACTCGCGGGATCGTCACCCTCAGCAGCGAAAGACAGCGGTTTATCCCCGCTGGCGCGGGGAACTCTCTAAAAGTATACATTTGTTCTTAAAGCATTTTTTCCCATAAAAACAACCCACCAACCTTAGATCGGAAGAGCAC')

# for seq in seqs:
# 	for max_distance in range(3, 5):
#  		find_spacers(repeat_fw, seq, max_distance, spacers_array)

# file_fasta = outdir + '/' + name_reads + '.notCombined_2.fasta'

# SeqIO.write(records, rev_comp, "fasta")

# cd ~/BRIG-0.95-dist && java -jar /home/anna/BRIG-0.95-dist/BRIG.jar #open BRIG
