#!/usr/bin/python
from BCBio import GFF
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
import csv
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from common_helpers.make_outdir import file_from_path, make_outdir, new_file_same_dir
from parsers.parse_csv import parse_csv
global bl_features;
all_features = {
'qseqid': {'description': 'Query Seq-id', 'type': 'str'},
'qgi': {'description': 'Query GI', 'type': 'str'},
'qacc': {'description': 'Query accesion', 'type': 'str'},
'qaccver': {'description': 'Query accession.version', 'type': 'str'},
'qlen': {'description': 'Query sequence length', 'type': 'int'},
'sseqid': {'description': 'Subject Seq-id', 'type': 'str'},
'sallseqid': {'description': 'All subject Seq-id(s)', 'type': 'str'},
'sgi': {'description': 'Subject GI', 'type': 'str'},
'sallgi': {'description': 'All subject GIs', 'type': 'str'},
'sacc': {'description': 'Subject accession', 'type': 'str'},
'saccver': {'description': 'Subject accession.version', 'type': 'str'},
'sallacc': {'description': 'All subject accessions', 'type': 'str'},
'slen': {'description': 'Subject sequence length', 'type': 'int'},
'qstart': {'description': 'Start of alignment in query', 'type': 'int'},
'qend': {'description': 'End of alignment in query', 'type': 'int'},
'sstart': {'description': 'Start of alignment in subject', 'type': 'int'},
'send': {'description': 'End of alignment in subject', 'type': 'int'},
'qseq': {'description': 'Aligned part of query sequence', 'type': 'str'},
'sseq': {'description': 'Aligned part of subject sequence', 'type': 'str'},
'evalue': {'description': 'Expect value', 'type': 'float'},
'bitscore': {'description': 'Bit score', 'type': 'float'},
'score': {'description': 'Raw score', 'type': 'float'},
'length': {'description': 'Alignment length', 'type': 'int'},
'pident': {'description': 'Percentage of identical matches', 'type': 'float'},
'nident': {'description': 'Number of identical matches', 'type': 'int'},
'mismatch': {'description': 'Number of mismatches', 'type': 'int'},
'positive': {'description': 'Number of positive-scoring matches', 'type': 'int'},
'gapopen': {'description': 'Number of gap openings', 'type': 'int'},
'gaps': {'description': 'Total number of gaps', 'type': 'int'},
'ppos': {'description': 'Percentage of positive-scoring matches', 'type': 'float'},
'frames': {'description': 'Query and subject frames', 'type': 'str'},
'qframe': {'description': 'Query frame', 'type': 'str'},
'sframe': {'description': 'Subject frame', 'type': 'str'},
'btop': {'description': 'Blast traceback operations (BTOP)', 'type': 'str'},
'staxids': {'description': 'Subject Taxonomy ID(s)', 'type': 'str'},
'sscinames': {'description': 'Subject Scientific Name(s)', 'type': 'str'},
'scomnames': {'description': 'Subject Common Name(s)', 'type': 'str'},
'sblastnames': {'description': 'Subject Blast Name(s)', 'type': 'str'},
'sskingdoms': {'description': 'Subject Super Kingdom(s)', 'type': 'str'},
'stitle': {'description': 'Subject Title', 'type': 'str'},
'salltitles': {'description': 'All Subject Title(s)', 'type': 'str'},
'sstrand': {'description': 'Subject Strand', 'type': 'str'},
'qcovs': {'description': 'Query Coverage Per Subject', 'type': 'float'},
'qcovhsp': {'description': 'Query Coverage Per HSP', 'type': 'float'},
}

class BlastParser(object):
	def parse_blast_csv(self):
		handle_file = open(self.bl_report_path)
		handle_csv = csv.reader(handle_file, delimiter=self.delimiter)

		if not self.custom_features: features = self.default_features
		else: features = self.custom_features
		self.features = filter(None, features.split(' '))

		self.hits = []

		for row in handle_csv:
			hit = {}
			i = 0
			for feature in self.features:
				if all_features[feature]['type'] == 'float':
					hit[feature] = float(row[i])
				elif all_features[feature]['type'] == 'int':
					hit[feature] = int(row[i])
				else:
					hit[feature] = row[i]
				i+=1

			self.hits.append(hit)
			
		return self.hits

	def __init__(self, bl_report_path, custom_features=False, delimiter=','):
		self.bl_report_path = bl_report_path
		self.custom_features = custom_features
		if not custom_features:
			self.default_features = ' qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore '
		self.delimiter = delimiter
		self.parse_blast_csv()
		return None

	def sort_blast_csv(self):
		sorted_hits = sorted( hits, key = lambda hit: ( hit['qseqid'], -hit['alignment_length'], hit['e-value']) ) 
		self.hits = sorted_hits
		return self.hits

	def count_hits(self):
		queries = []
		for hit in self.hits: queries.append(hit['qseqid'])
		return [len(queries), len(set(queries))]

	def write_blast_csv(self, outfile_path, functions='False', hits=False, header=False):
		if not hits: hits = self.hits
		with open(outfile_path, 'wb') as outfile:
			csv_writer = csv.writer(outfile, delimiter=self.delimiter)
			if header:
				csv_writer.writerow(self.features)

			for hit in hits:
				row = []
				for feature in self.features:
					row.append(hit[feature])
				csv_writer.writerow(row)
			outfile.close()

		return outfile_path

	def extract_credible_hits(self, max_hits=2):
		self.sort_blast_csv()
		print self.count_hits()
		query = False
		results = []
		for hit in self.hits:
			if not query: 
				query = hit['qseqid']
				results.append(hit)
				i = 1
			else:
				if hit['qseqid'] == query:
					i += 1
					if i <= max_hits:
						results.append(hit)
				else:
					i = 1
					query = hit['qseqid']
					results.append(hit)
		outfile_path = file_from_path(self.bl_report_path, folder=True) + 'credible_hits.csv'
		self.write_blast_csv(outfile_path=outfile_path, hits=results, header=True)
		return outfile_path

	def extract_unique_hits(self):
		print self.count_hits()
		query = False
		results = []
		for hit in self.hits:
			if not query: 
				query = hit['qseqid']
				result = hit
				i = 1
			else:
				if hit['qseqid'] == query:
					i += 1
				else:
					if i == 1: results.append(result)
					i = 1
					query = hit['qseqid']
					result = hit

		outfile_path = file_from_path(self.bl_report_path, folder=True) + 'unique_hits.csv'
		print len(results), 'unique hits'
		return results

	def add_functions(self, q_path,  q_delimiter, s_path, s_delimiter, hits=False):
		q_info = parse_csv(q_path, delimiter=q_delimiter)
		s_info = parse_csv(s_path, delimiter=s_delimiter)
		if not hits: hits = self.hits
		for hit in hits:
			for row in q_info:
				if hit['qseqid'] == row[0]:
					hit['q_function'] = row[1]
			for row in s_info:
				if hit['sseqid'] == row[0]:
					hit['s_function'] = row[1]
					hit['s_go_terms'] = row[2]
		self.features.extend(['q_function', 's_function', 's_go_terms'])
		outfile_path = new_file_same_dir(self.bl_report_path, new_ext='_with_functions.csv')
		self.write_blast_csv(outfile_path=outfile_path, hits=hits, header=True)
		return hits