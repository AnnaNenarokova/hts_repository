#!/usr/bin/python
import sys
import os.path

# sys.path.insert(0, "/home/anna/bioinformatics/ngs")
# from helpers.test import test as test

# test()

import os
import time
from subprocess import call
from Bio import SeqIO
from ntpath import split
global THREADS
global CLUSTER; CLUSTER = False
if CLUSTER: THREADS = 24
else: THREADS = 8
global FASTQ; FASTQ = False

global FORMATS; 
FORMATS = { 
	'pairwise': ['0'], 
	'query_anchored_identities': ['1', ''],
	'query_anchored_no_identities': ['2', ''],
	'flat_query_anchored_identities': ['3', ''],
	'flat_query_anchored_no_identities': ['4', ''],
	'xml': ['5', '.xml'], 
	'tabular': ['6', '.csv'],
	'tabular_comment_lines': ['7', '.csv'],
	'text_asn': ['8', ''],
	'binary_asn': ['9', ''],
	'comma_values': ['10', '.csv'],
	'blast_archive': ['11', '']
}

def file_from_path(path, folder=False):
    head, tail = split(path)
    if folder: return head
    else: return tail

def cr_outdir(f, workdir=False):
	name = file_from_path(f)[0:-6]
	if workdir: outdir = workdir + name + '/'
	else: outdir = file_from_path(f, folder=True) + '/' + name + '/'
	if not os.path.exists(outdir): os.makedirs(outdir)
	return outdir

def convert(fastq_file):
	fasta_file = fastq_file[0:-1] + 'a'
	SeqIO.convert(fastq_file, "fastq", fasta_file, "fasta")
	return fasta_file

def makeblastdb(fasta_file, type, outdir=False):
	if not outdir:
		outdir = cr_outdir(fasta_file)
	db_folder = outdir + 'db_folder/'
	if not os.path.exists(db_folder):
	    os.makedirs(db_folder)
	blast_db = db_folder + file_from_path(fasta_file)[0:-6] + '.db'
	makeblastdb = ['makeblastdb', '-in', fasta_file, '-parse_seqids', '-dbtype', type, '-out', blast_db]
	call(makeblastdb)
	return blast_db


def blast_mkdb(query, reference, bl_type, fmt, outdir=False):
	if not outdir:
		outdir = cr_outdir(reference)
	if FASTQ: ref_file = convert(reference)
	else: ref_file = reference
	blast_db = makeblastdb(ref_file, outdir)
	name1 = file_from_path(query)[0:-6]
	name2 = file_from_path(reference)[0:-6]

	# if fmt == FORMATS['comma_values']:

	outfile = outdir + str(name1 + '_' +  name2 + "_bl_report" + '')


	if FASTQ: 
		blastn = ['blastn', '-query', query, '-db', blast_db, '-out', outfile, '-outfmt', FORMATS['comma_values'], '-task', 'blastn-short', '-num_threads', str(THREADS)]
	else:
		blast = ['psiblast', '-query', query, '-db', blast_db, '-out', outfile, '-outfmt', FORMATS['comma_values'], '-num_threads', str(THREADS), '-evalue', '5']
	print blast
	call(blast)
	return 0

# if FASTQ:
# 	if not CLUSTER:
# 		fastq_file = '/home/anna/bioinformatics/wheat/H7_1.fastq'
# 		adapters = '/home/anna/bioinformatics/wheat/adapters.fa'
# 		trim_out = '/home/anna/bioinformatics/wheat/H7_1/trim_out/'
# 	else:
# 		fastq_file = '/mnt/lustre/nenarokova/wheat/R1.fasta'
# 		adapters = '/mnt/lustre/nenarokova/wheat/universal_adapter.fasta'
# 	blast_mkdb(adapters, fastq_file)
# 	many_files = False
# 	if many_files:
# 		files = os.listdir(trim_out)
# 		files = filter(lambda x: x.endswith('.fastq'), files) 

# 		process_count = 0

# 		for f in files:
# 			fastq_file = trim_out + f
# 			pid = os.fork()
# 			time.sleep(0.1)
# 			if pid == 0:
# 				print "Process started"
# 				blast_fastq(adapters, fastq_file)
# 				print "Process ended"
# 				os._exit(0)

# 			else:
# 				process_count += 1
# 				if process_count >= THREADS:
# 					os.wait()
# 					process_count -= 1

# 		for i in range(process_count):
# 			os.wait()
# else:
# 	query = '/home/anna/bioinformatics/euglena/Tr_proteins.fasta'
# 	# reference = '/home/anna/bioinformatics/euglena/Euglena_gracilis_genome_V1.fasta'
# 	# reference = '/home/anna/bioinformatics/euglena/E_gracilis_transcriptome_cds.fasta'
# 	reference = '/home/anna/bioinformatics/euglena/E_gracilis_transcriptome_final.PROTEINS.fasta'
# 	bl_type = 'nucl'
# 	fmt = FORMATS['comma_values']
# 	blast_mkdb(query, reference, bl_type, fmt)