from Bio import SeqIO
import os
from ntpath import split
from subprocess32 import call

def file_from_path (path):
    head, tail = split(path)
    return tail

file_mut6 = '/home/anna/bioinformatics/outdirs/mut6/contigs_mut6.fasta'
file_mut9 = '/home/anna/bioinformatics/outdirs/mut9/contigs_mut9.fasta'
for file_mut in [file_mut6, file_mut9]:
	name_mut = file_from_path(file_mut)[0:-6]
	workdir = '/home/anna/bioinformatics/outdirs/genes_bl21/new_genes/'
	gene_files = os.listdir(workdir)
	for gene_name in gene_files:
		gene_file = workdir + gene_name
		blastdir = '/home/anna/bioinformatics/bioprograms/ncbi-blast-2.2.29+/bin/'
		blast = blastdir + 'blastn'
		outdir = '/home/anna/bioinformatics/outdirs/alignments/new_genes/' + name_mut + '/'
		if not os.path.exists(outdir): os.makedirs(outdir)
		outfile = outdir + str(gene_name)
		call_blast = [blast, '-query', gene_file, '-subject', file_mut, '-out', outfile, '-outfmt', '6']
		call(call_blast)
		outfile = outfile + '.html'
		call_blast = [blast, '-query', gene_file, '-subject', file_mut, '-out', outfile, '-html']
		call(call_blast)

# blastdir = '/home/anna/bioinformatics/bioprograms/ncbi-blast-2.2.29+/bin/'
# blast = blastdir + 'blastn'
# gene_file = "/home/anna/bioinformatics/outdirs/genes_bl/all_genes/aspA.fasta"
# outfile = '/home/anna/bioinformatics/outdirs/alignments/' + 'aspA'
# call_blast = [blast, '-query', gene_file, '-subject', file_mut6, '-out', outfile]
# call(call_blast)