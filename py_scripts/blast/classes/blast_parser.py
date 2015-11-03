#!/usr/bin/python
import csv
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from common_helpers.make_outdir import file_from_path, make_outdir

class BlastParser(object):
	def __init__(self, bl_report_path, bl_report_type):
		self.bl_report_path = bl_report_path
		self.bl_report_type = bl_report_type

	def parse_blast_csv(self):
		handle_file = open(self.bl_report_path)
		handle_csv = csv.reader(handle_file, delimiter=',')
		results = []
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
			results.append(hit)
		return results
	
	def sort_blast_csv(self):
		hits = self.parse_blast_csv()
		sorted_hits = sorted( hits, key = lambda hit: ( hit['query_id'], -hit['alignment_length'], hit['e-value']) ) 
		return sorted_hits

	def write_blast_csv(self, hits, outfile_path, header=False):
		with open(outfile_path, 'wb') as outfile:
			csv_writer = csv.writer(outfile, delimiter=',')
			if header:
				csv_writer.writerow(['query id', 'subject id', '% identity', 'alignment length', 
				 	'mismatches','gap opens', 'q start','q end','s start', 's end', 'e-value', 'bit score'])
			for hit in hits:
				row = [
					hit['query_id'], hit['subject_id'], hit['%_identity'], hit['alignment_length'],
					hit['mismatches'], hit['gap_opens'], hit['q_start'], hit['q_end'], 
					hit['s_start'], hit['s_end'], hit['e-value'], hit['bit_score']
					  ]
				csv_writer.writerow(row)
			outfile.close()
		return outfile_path


# blreport = '/home/anna/bioinformatics/euglena/223_mitogenes/223_mitogenes_b2go/m_genes_bl_report.csv'
blreport = '/home/anna/bioinformatics/euglena/Tripanosoma_Verner/Tr_proteins/blast_db/bl_reports/Tr_prote/223_mitogenes_b2go_bl_report.csv'

out_path = '/home/anna/bioinformatics/euglena/out.csv' 
new_bp = BlastParser(blreport, 'csv')
sorted_hits = new_bp.sort_blast_csv()
new_bp.write_blast_csv(hits=sorted_hits, outfile_path=out_path, header=True)