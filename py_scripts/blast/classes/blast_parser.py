#!/usr/bin/python
from BCBio import GFF
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
import csv
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from common_helpers.make_outdir import file_from_path, make_outdir, new_file
from common_helpers.lookahead import lookahead
from common_helpers.parse_csv import parse_csv
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

class HitsCollection(object):
	def __init__(self, hits=False, blreport_path=False, features_string=False, features=False, delimiter=','):
		if not features:
			if features_str: self.features = filter(None, features.split(' '))
			else: self.features = ['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore']
		
		if hits: self.hits = hits
		elif blreport_path: self.read_hits(blreport_path, delimiter=delimiter)
		else: return False

		return None

	def read_hits(self, blreport_path, delimiter=','):
		handle_file = open(self.blreport_path)
		handle_csv = csv.reader(handle_file, delimiter)
		for row in handle_csv:
			if row[0] in self.features: pass
			else:
				hit = {}
				for feature in self.features:
					if all_features[feature]['type'] == 'float':
						hit[feature] = float(row[i])
					elif all_features[feature]['type'] == 'int':
						hit[feature] = int(row[i])
					else:
						hit[feature] = row[i]
			self.hits.append(hit)
		return self.hits

	def count_hits(self, evalue=False, length=False, alen_qlen=False):
		hit_set= []
		for hit in self.hits: queries.append(hit['qseqid'])
			if alen_qlen:
				hit['allen/qlen'] = hit['length']/float(hit['qlen']):
				allen_index = self.features.index('length')
				self.features.insert(allen_index+1, 'allen/qlen')
		print 'All hits,', len_queries 
		print 'Set of queries:', len_q_set
		return [len_queries, len_q_set]

	def add_len_ratio(self):
		hits_with_ratio = HitsCollection(hits=self.hits, features=self.features)
		allen_index = hits_with_ratio.features.index('length')
		hits_with_ratio.features.insert(allen_index+1, 'allen/qlen')
		for hit in hits_with_ratio.hits:
			hit['allen/qlen'] = float(hit['length']/float(hit['qlen']))
		return hits_with_ratio

	def change_hits_ids(self, ids_csv_path, ids_csv_delimiter=','):
		ids_csv = parse_csv(ids_csv_path, delimiter=ids_csv_delimiter)
		ids_substitutes = {}
		for row in ids_csv: ids_substitute[row[0]] = row[1]
		new_ids_hits = HitsCollection(hits=self.hits, features=self.features)
		for hit in new_ids_hits.hits:
			hit['qseqid'] = ids_substitutes[hit['qseqid']]
		return new_ids_hits

	def write_blast_csv(self, outfile_path, hits=False, header=False):
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

	def __divide_hits_by_feature__(self, feature, hits=False, verbose=True):
		if not hits: hits = self.hits
		
		divided_hits = {}
		for hit in lookahead(hits):
			if hit[feature] in divided_hits.keys():
				divided_hits[hit[feature]].append(hit)
			else:
				divided_hits[hit[feature]] = []
				divided_hits[hit[feature]].append(hit)

		if verbose: print 'Set of ', feature, len(divided_hits)

		return divided_hits

	def extract_unique(self, query=False, subject=False):
		features = []
		if quer
		for query in queries:
			self.__divide_hits_by_feature__
		return outfile_path

	def extract_best(self, mindif_evalue=10, maxdif_length=1, sort_qseid=False, sort_sseid=False):
		features = []
		if sort_qseid: features.append('qseqid')
		if sort_sseid: features.append('sseqid')

		for feature in features:
			divided_hits = self.__divide_hits_by_feature__(feature, hits=hits)
			best_hits = []
			for subj in subj_hits:
				sorted_hits = sorted(subj_hits[subj], key = lambda hit: hit['evalue'])
				is_first = True
				for hit in sorted_hits:
					if is_first: 
						best_hits.append(hit)
						is_first = False
					else:
						if hit['evalue']== 0:
							best_hits.append(hit)
						elif (cur_hit['evalue'] == 0 or hit['evalue']/cur_hit['evalue'] >= mindif_evalue) \
								and \
							 (hit['length'] / cur_hit['length']) <= maxdif_length:
							break
						else:
							best_hits.append(hit)
					cur_hit = hit
			print 'Best hits', len(best_hits)
			self.hits = best_hits

		outfile_path = new_file(self.blreport_path, new_end='_best_hits.csv')
		self.blreport_path = outfile_path
		self.write_blast_csv(outfile_path=outfile_path, hits=best_hits, header=True)
		
				sorted_hits = sorted(subj_hits[subj], key = lambda hit: hit['evalue'])
				is_first = True
				for hit in sorted_hits:
					if is_first: 
						best_hits.append(hit)
						is_first = False
					else:
						if hit['evalue']== 0:
							best_hits.append(hit)
						elif (cur_hit['evalue'] == 0 or hit['evalue']/cur_hit['evalue'] >= mindif_evalue) \
								and \
							 (hit['length'] / cur_hit['length']) <= maxdif_length:
							break
						else:
							best_hits.append(hit)
					cur_hit = hit
			print 'Best hits', len(best_hits)
			self.hits = best_hits

		outfile_path = new_file(self.blreport_path, new_end='_best_hits.csv')
		self.blreport_path = outfile_path
		self.write_blast_csv(outfile_path=outfile_path, hits=best_hits, header=True)
		
		return outfile_path

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
					hit['s_GO_terms'] = row[2]

		qseqid_index = self.features.index('qseqid')						
		self.features.insert(qseqid_index+1, 'q_function')
		sseqid_index = self.features.index('sseqid')
		self.features.insert(sseqid_index+1, 's_GO_terms')
		self.features.insert(sseqid_index+1, 's_function')

		outfile_path = new_file(self.blreport_path, new_end='_with_functions.csv')
		self.write_blast_csv(outfile_path=outfile_path, hits=hits, header=True)
		return hits

