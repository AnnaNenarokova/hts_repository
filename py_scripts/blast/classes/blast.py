#!/usr/bin/python

import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from common_helpers.make_outdir import file_from_path, name_outdir, make_outdir
from seq_helpers.convert import fastq_fasta

global FORMATS; 
FORMATS = { 
	'pairwise': '0', 
	'query_anchored_identities': '1',
	'query_anchored_no_identities': '2',
	'flat_query_anchored_identities': '3',
	'flat_query_anchored_no_identities': '4',
	'xml': '5', 
	'tabular': '6',
	'tabular_comment_lines': '7',
	'text_asn': '8',
	'binary_asn': '9',
	'comma_values': '10',
	'blast_archive': '11'
}

class Blast(object):
	def __init__(self, ref=False, ref_type='fasta', db_type=False, db=False, query=False, outdir=False):
		self.ref = ref
		self.ref_type = ref_type
		if self.ref_type=='fastq': self.ref = fastq_fasta(self.ref)
		self.db_type = db_type
		self.db = db
		self.query = query
		self.outdir = outdir
		return None

	def makeblastdb(self):
		if not self.outdir:
			self.outdir = make_outdir(self.ref)
		db_folder = self.outdir + 'db_folder/'
		db_path = db_folder + file_from_path(self.ref, endcut=6) + '.db'
		makeblastdb = ['makeblastdb', '-in', self.ref, '-parse_seqids', '-dbtype', self.db_type, '-out', db_path]
		call(makeblastdb)
		return db_path

	def blast(self, fmt=6):
		if not self.db: self.db = makeblastdb()
		
		return None

