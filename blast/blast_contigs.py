import os
from ntpath import split
from subprocess32 import call
def file_from_path (path):
    head, tail = split(path)
    return tail

file_mut6 = '/home/anna/bioinformatics/outdirs/mut6/contigs_mut6.fasta'
file_mut9 = '/home/anna/bioinformatics/outdirs/mut9/contigs_mut9.fasta'
file_mut6_ends = '/home/anna/bioinformatics/outdirs/mut6/contigs_mut6_ends.fasta'
file_mut9_ends = '/home/anna/bioinformatics/outdirs/mut9/contigs_mut9_ends.fasta'
contigs6 = '/home/anna/bioinformatics/outdirs/mut6/contigs_mut6.fasta'
file_bl21 = '/home/anna/bioinformatics/outdirs/BL21.fasta'

blastdir = '/home/anna/bioinformatics/bioprograms/ncbi-blast-2.2.29+/bin/'
blast = blastdir + 'blastn'
outdir = '/home/anna/bioinformatics/outdirs/alignments/contigs/'

file1 = '/home/anna/bioinformatics/outdirs/pBad.fasta'
# file1 = '/home/anna/bioinformatics/outdirs/BL21.fasta'
# for file2 in (file_mut6_ends, file_mut9_ends):
# 	name1 = file_from_path(file1)[0:-6]
# 	name2 = file_from_path(file2)[0:-6]
# 	outfile = outdir + str(name1 + '_' +  name2 + '.xml') 
# 	call_blast = [blast, '-query', file1, '-subject', file2, '-out', outfile, '-outfmt', '5']
# 	call(call_blast)

file2 = file_bl21
name1 = file_from_path(file1)[0:-6]
name2 = file_from_path(file2)[0:-6]
outfile = outdir + str(name1 + '_' +  name2) 
call_blast = [blast, '-query', file1, '-subject', file2, '-out', outfile, '-outfmt', '6']
call(call_blast)