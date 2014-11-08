from subprocess32 import call
from file_from_path import file_from_path
file1 = '/home/anna/bioinformatics/outdirs/BL21.fasta'
file2 = '/home/anna/bioinformatics/outdirs/IS10L.fasta'
outdir = '/home/anna/bioinformatics/outdirs/'
name1 = file_from_path(file1)[0:-6]
name2 = file_from_path(file2)[0:-6]
outfile = outdir + str(name1 + '_' +  name2) 
blastdir = '/home/anna/bioinformatics/bioprograms/ncbi-blast-2.2.29+/bin/'
blast = blastdir + 'blastn'
call_blast = [blast, '-query', file1, '-subject', file2, '-out', outfile, '-outfmt', '5']
call(call_blast)