from Bio import SeqIO
import os
from ntpath import split
from subprocess32 import call
global MAX_PROCESSES; MAX_PROCESSES = 8
def file_from_path (path):
    head, tail = split(path)
    return tail

file_mut6 = '//home/anna/bioinformatics/outdirs/mut6_contigs_ends.fasta'
file_mut9 = '/home/anna/bioinformatics/outdirs/mut9_contigs_ends.fasta'
file_bl21 = '/home/anna/bioinformatics/outdirs/BL21.gbk'

blastdir = '/home/anna/bioinformatics/bioprograms/ncbi-blast-2.2.29+/bin/'
blast = blastdir + 'blastn'
outdir = '/home/anna/bioinformatics/outdirs/alignments/contigs/'
if not os.path.exists(outdir): os.makedirs(outdir)
# files = [(file_mut6, file_mut9), (file_mut9, file_mut6), (file_mut6, file_bl21), (file_mut9, file_mbl21)]
# process_count = 0
# for file1, file2 in files:
# 	outfile = outdir + str(file1 + file2) 
# 	call_blast1 = [blast, '-query', file1, '-subject', file2, '-out', outfile, '-outfmt', '6']
# 	call_blast2
# 	for call_blast in [call_blast1, call_blast2]:
# 		pid = os.fork()
# 		time.sleep(0.1)
# 		if pid == 0:
# 			if (call_blast == call_blast2): 
# 				outfile = outfile + '.html'
# 				call_blast = [blast, '-query', file1, '-subject', file2, '-out', outfile, '-html']
# 			call(call_blast)
# 			os.abort()
# 		else:
# 			process_count += 1
# 			if process_count >= MAX_PROCESSES:
# 				os.wait()
# 				process_count -= 1
name1 = file_from_path(file_mut6)[0:-6]
name2 = file_from_path(file_mut9)[0:-6]
outfile = outdir + str(name1 + '_' +  name2) 
call_blast = [blast, '-query', file_mut6, '-subject', file_mut9, '-out', outfile, '-outfmt', '6']
call(call_blast)