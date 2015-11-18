#!/usr/bin/python
from BCBio import GFF
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation

import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")

from blast.classes.blast_parser import BlastParser
from common_helpers.make_outdir import new_file_same_dir

def blast_to_gff(blresult_path, reference, outfile_path=False):
	blparser = BlastParser(blresult_path, 'csv')
	hits = blparser.hits
	if not outfile_path: outfile_path = new_file_same_dir(blresult_path, new_ext='.gff')
	print hits
	pass

bl_result_path = '/home/anna/bioinformatics/euglenozoa/tripanosoma/tr_proteins/bl_reports/mDNA_genes_bl_report.csv'
reference = '/home/anna/bioinformatics/euglenozoa/tripanosoma/tr_proteins.fasta'

blast_to_gff(bl_result_path, reference)
