from Bio import SeqIO

# for output_flash in ('.extendedFrags.fastq', '.notCombined_1.fastq', '.notCombined_2.fastq'):
#     file_fastq = outdir + 'FlashOutput/' + name_reads +  output_flash
#     file_fasta = file_fastq[0:-1] + 'a'
#     SeqIO.convert (file_fastq, "fastq", file_fasta, "fasta")

# for f in (name_fw, name_rv):
# 	file_fastq = work_dir + '/' + f
# 	file_fasta = outdir + '/' + f[0:-1] + 'a'
# 	SeqIO.convert (file_fastq, "fastq", file_fasta, "fasta")
work_dir = '/media/anna/biodata/htses/dasha/'
f = 'Ecoli-mut6_trimmed_paired_R1.fastq'
file_fastq = work_dir +  f
file_fasta = work_dir +  f[0:-1] + 'a'
SeqIO.convert (file_fastq, "fastq", file_fasta, "fasta")