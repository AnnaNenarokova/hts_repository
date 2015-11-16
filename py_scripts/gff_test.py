#!/usr/bin/python
from BCBio import GFF
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation

import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")

from blast.classes.blast_parser import BlastParser

bl_report = '/home/anna/bioinformatics/euglenozoa/tripanosoma/tr_proteins/bl_reports/mDNA_genes_bl_report.csv'
blparser = BlastParser(bl_report, 'csv')

print blparser.hits