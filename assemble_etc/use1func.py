#!/usr/bin/python
import os
from subprocess32 import call
from ntpath import split
global ONLY_TRIM; ONLY_TRIM = False
global ONLY_ASSEMBLE; ONLY_ASSEMBLE = True
global ONLY_ANNOTATE; ONLY_ANNOTATE = False
global THREADS; THREADS = 8
global RAM; RAM = 8
import trim
import assemble
from genome_fun import use_quast
from genome_fun import prokka_annotate

def file_from_path (path):
    head, tail = split(path)
    return tail

def cr_outdir(file_fw, workdir):
	name_fw = file_from_path(file_fw)
	name_reads = name_fw[0:-6]
	outdir = workdir + name_reads + '/'
	if not os.path.exists(outdir): os.makedirs(outdir)
	return outdir

workdir = '/home/anna/bioinformatics/outdirs/'
# scaffold = '/home/anna/bioinformatics/outdirs/TB1_ex-wt/scaffolds.fasta'
# scaffold = '/home/anna/bioinformatics/outdirs/mut9/contigs_mut9.fasta_BL21.fasta.fasta'
# contigs = '/home/anna/bioinformatics/outdirs/plasmid70_TGACCA_L001_R1_001/pUM146.fasta'
# reference = '/home/anna/bioinformatics/outdirs/BL21.fasta'
f = '/home/anna/bioinformatics/htses/pt7blue-T4.fasta'

outdir = cr_outdir(f, workdir)
# use_quast (contigs, reference, outdir)

# # reference = '/home/anna/bioinformatics/hts/stuff/pt7blue-T4.fasta'
# reference = '/home/anna/bioinformatics/output_from_server/contigs.fasta'

# outdir = '/home/anna/bioinformatics/hts/outdirs/'
prokka_annotate (f, outdir)

