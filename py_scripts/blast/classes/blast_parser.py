#!/usr/bin/python
from BCBio import GFF
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
import csv
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from common_helpers.make_outdir import file_from_path, make_outdir
from parsers.parse_csv import parse_csv

class BlastParser(object):
	def parse_blast_csv(self):
		handle_file = open(self.bl_report_path)
		handle_csv = csv.reader(handle_file, delimiter=',')
		self.hits = []
		for row in handle_csv:
			hit = {
			'query_id': str(row[0]),
			'subject_id': str(row[1]),
			'%_identity': float(row[2]),
			'alignment_length': int(row[3]),
			'mismatches': int(row[4]),
			'gap_opens': int(row[5]),
			'q_start': int(row[6]),
			'q_end': int(row[7]),
			's_start': int(row[8]),
			's_end': int(row[9]),
			'e-value': float(row[10]),
			'bit_score': float(row[11]),
					}
			self.hits.append(hit)
		return self.hits

	def __init__(self, bl_report_path, bl_report_type):
		self.bl_report_path = bl_report_path
		self.bl_report_type = bl_report_type
		self.parse_blast_csv()
		return None

	def sort_blast_csv(self):
		sorted_hits = sorted( hits, key = lambda hit: ( hit['query_id'], -hit['alignment_length'], hit['e-value']) ) 
		self.hits = sorted_hits
		return self.hits

	def count_hits(self):
		queries = []
		for hit in self.hits: queries.append(hit['query_id'])
		return [len(queries), len(set(queries))]

	def write_blast_csv(self, outfile_path, functions='False', hits=False, header=False):
		with open(outfile_path, 'wb') as outfile:
			csv_writer = csv.writer(outfile, delimiter=',')
			if header:
				if functions:
					header_row = ['query id', 'q. function', 'subject id', 's. function', 's. GO terms', '% identity', 'alignment length', 
				 		'mismatches','gap opens', 'q. start','q. end','s start', 's. end', 'e-value', 'bit score']
				else:
				 	header_row = ['query id', 'subject id', '% identity', 'alignment length', 
				 		'mismatches','gap opens', 'q. start','q. end','s. start', 's. end', 'e-value', 'bit score']
				csv_writer.writerow(header_row)

			if not hits: hits = self.hits
			for hit in hits:
				if functions:
					if not 'q_function' in hit.keys(): hit['q_function']=''
					row = [
						hit['query_id'], hit['q_function'], hit['subject_id'], hit['s_function'], hit['s_go_terms'], hit['%_identity'], hit['alignment_length'],
						hit['mismatches'], hit['gap_opens'], hit['q_start'], hit['q_end'], 
						hit['s_start'], hit['s_end'], hit['e-value'], hit['bit_score']
						  ]
				else:
					row = [
						hit['query_id'], hit['subject_id'], hit['%_identity'], hit['alignment_length'],
						hit['mismatches'], hit['gap_opens'], hit['q_start'], hit['q_end'], 
						hit['s_start'], hit['s_end'], hit['e-value'], hit['bit_score']
						  ]

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
				query = hit['query_id']
				results.append(hit)
				i = 1
			else:
				if hit['query_id'] == query:
					i += 1
					if i <= max_hits:
						results.append(hit)
				else:
					i = 1
					query = hit['query_id']
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
				query = hit['query_id']
				result = hit
				i = 1
			else:
				if hit['query_id'] == query:
					i += 1
				else:
					if i == 1: results.append(result)
					i = 1
					query = hit['query_id']
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
				if hit['query_id'] == row[0]:
					hit['q_function'] = row[1]
			for row in s_info:
				if hit['subject_id'] == row[0]:
					hit['s_function'] = row[1]
					hit['s_go_terms'] = row[2]
		outfile_path = file_from_path(self.bl_report_path, folder=True) + 'hits_functions.csv'
		self.write_blast_csv(outfile_path=outfile_path, hits=hits, functions='True', header=True)
		return hits