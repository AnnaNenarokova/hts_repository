#!/usr/bin/python
import csv
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from common_helpers.make_outdir import file_from_path, make_outdir

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
		hits = self.parse_blast_csv()
		sorted_hits = sorted( hits, key = lambda hit: ( hit['query_id'], -hit['alignment_length'], hit['e-value']) ) 
		self.hits = sorted_hits
		return self.hits

	def count_hits(self):
		queries = []
		for hit in self.hits: queries.append(hit['query_id'])
		return [len(queries), len(set(queries))]

	def write_blast_csv(self, outfile_path, hits=False, header=False):
		with open(outfile_path, 'wb') as outfile:
			csv_writer = csv.writer(outfile, delimiter=',')
			if header:
				csv_writer.writerow(['query id', 'subject id', '% identity', 'alignment length', 
				 	'mismatches','gap opens', 'q start','q end','s start', 's end', 'e-value', 'bit score'])
			
			if not hits: hits = self.hits
			for hit in hits:
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
		self.sort_blast_csv()
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
		self.write_blast_csv(outfile_path=outfile_path, hits=results, header=True)
		return outfile_path