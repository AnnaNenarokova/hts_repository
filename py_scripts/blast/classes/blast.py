#!/usr/bin/python
# db_types: 'nucl', 'prot'
# bl_types: 'blastn', 'blastp', 'psiblast'
from subprocess import call
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from common_helpers.make_outdir import file_from_path, name_outdir, make_outdir
from seq_helpers.convert import fastq_fasta

class Blast(object):
	def __init__(self, ref_path=False, ref_type='fasta', db_type=False, db_path=False, query_path=False, outdir=False, threads=8):
		self.ref_path = ref_path
		self.ref_type = ref_type
		if self.ref_type=='fastq': self.ref_path = fastq_fasta(self.ref_path)
		self.db_type = db_type
		self.db_path = db_path
		self.query_path = query_path
		self.outdir = outdir
		return None

	def makeblastdb(self):
		if not self.ref_path: 
			print "Error: No reference"
			return 1
		if not self.outdir:
			self.outdir = make_outdir(self.ref_path)
		db_folder = self.outdir + 'blast_db/'
		db_path = db_folder + file_from_path(self.ref_path, endcut=6) + '.db'
		makeblastdb = ['makeblastdb', '-in', self.ref_path, '-parse_seqids', '-dbtype', self.db_type, '-out', db_path]
		call(makeblastdb)
		return db_path

	formats = { 
	'pairwise': {'':'0', 'ext':''}, 
	'query_anchored_identities': {'#':'1', 'ext':''},
	'query_anchored_no_identities': {'#':'2', 'ext':''},
	'flat_query_anchored_identities': {'#':'3', 'ext':''},
	'flat_query_anchored_no_identities': {'#':'4', 'ext':''},
	'xml': {'#':'5', 'ext':'.xml'}, 
	'tabular': {'#':'6', 'ext':'.csv'},
	'tabular_comment_lines': {'#':'7', 'ext':'.txt'},
	'text_asn': {'#':'8', 'ext':''},
	'binary_asn': {'#':'9', 'ext':''},
	'comma_values': {'#':'10', 'ext':'.csv'},
	'blast_archive': {'#':'11', 'ext':''}
	}

	def blast(self, bl_type='blastn', outfmt='comma_values', blastn_short=False, evalue=10, threads=8, outfile=False):
		if not self.query_path:
			print "Error: No query"
			return 'Error'
		if not self.db_path: self.db_path = self.makeblastdb()
		else:
			if not outfile: self.outdir = make_outdir(self.ref_path)

		query_name = file_from_path(self.query_path, endcut=6)
		if not outfile: outfile = self.outdir + str(query_name + "_bl_report" + self.formats[outfmt]['ext'])

		blast_call = [bl_type, '-query', self.query_path, '-db', self.db_path, '-out', outfile, '-outfmt', self.formats[outfmt]['#'], '-num_threads', str(threads), '-evalue', str(evalue)]
		
		if not ((bl_type=='blastn' and self.db_type=='nucl') or ((bl_type!='blastp' or bl_type!='psiblast') and self.db_type=='prot')): 
			print 'Error: Incompatible options'
			return 'Error'

		if blastn_short:
			if not (bl_type=='blastn' and self.db_type=='nucl'): 
				print 'Error: Incompatible options'
				return 'Error'
			else: blast_call.extend ['-task', 'blastn-short']

		print blast_call
		call(blast_call)
		return outfile


ref_path = '/home/anna/bioinformatics/euglena/Tripanosoma_Verner/Tr_proteins.fasta'
query_path ='/home/anna/bioinformatics/euglena/223_mitogenes/223_mitogenes_b2go.fasta'
new_blast = Blast(ref_path=ref_path, query_path=query_path, db_type='prot')
new_blast.blast(bl_type='psiblast', evalue=1, outfmt='tabular')