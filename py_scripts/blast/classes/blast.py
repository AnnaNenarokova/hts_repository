#!/usr/bin/python

import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from common_helpers.make_outdir import file_from_path, name_outdir, make_outdir
from seq_helpers.convert import fastq_fasta

class Blast(object):
	def __init__(self, ref_path=False, ref_type='fasta', db_type=False, db_path=False, query_path=False, outdir=False, threads=False):
		self.ref_path = ref_path
		self.ref_type = ref_type
		if self.ref_type=='fastq': self.ref = fastq_fasta(self.ref)
		self.db_type = db_type
		self.db_path = db_path
		self.query_path = query_path
		self.outdir = outdir
		return None

	def makeblastdb(self):
		if not ref: 
			print "Error: No reference"
			return 1
		if not self.outdir:
			self.outdir = make_outdir(self.ref)
		db_folder = self.outdir + 'db_folder/'
		db_path = db_folder + file_from_path(self.ref, endcut=6) + '.db'
		makeblastdb = ['makeblastdb', '-in', self.ref, '-parse_seqids', '-dbtype', self.db_type, '-out', db_path]
		call(makeblastdb)
		return db_path

	formats = { 
	'pairwise': {'№':'0', 'ext':''}, 
	'query_anchored_identities': {'№':'1', 'ext':''},
	'query_anchored_no_identities': {'№':'2', 'ext':''},
	'flat_query_anchored_identities': {'№':'3', 'ext':''},
	'flat_query_anchored_no_identities': {'№':'4', 'ext':''},
	'xml': {'№':'5', 'ext':'.xml'}, 
	'tabular': {'№':'6', 'ext':'.csv'},
	'tabular_comment_lines': {'№':'7', 'ext':'.csv'},
	'text_asn': {'№':'8', 'ext':''},
	'binary_asn': {'№':'9', 'ext':''},
	'comma_values': {'№':'10', 'ext':'.csv'},
	'blast_archive': {'№':'11', 'ext':''}
	}

	def blast(self, bltype='blastn', outfmt='comma_values', blastn_short=False, evalue=10, threads=8, outfile=False):
		if not self.query_path:
			print "Error: No query"
			return 1
		if not self.db_path: self.db_path = makeblastdb()
		else:
			if not outfile: self.outdir = make_outdir(self.ref)

		query_name = file_from_path(self.query_path, endcut=6)
		if not outfile: outfile = outdir + str(query_name + "_bl_report" + formats[outfmt]['ext'])

		blast_call = [bltype, '-query', self.query, '-db', self.db_path, '-out', outfile, '-outfmt', formats['outfmt'], '-num_threads', str(threads)]
		if blastn_short: blast_call.extend ['-task', 'blastn-short']
		return outfile

