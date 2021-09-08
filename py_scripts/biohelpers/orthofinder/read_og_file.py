#!python
import sys
sys.path.insert(0, "/Users/annanenarokova/work/code/ngs/")
sys.path.insert(0, "/home/users/nenarokova/ngs/")
from py_scripts.helpers.parse_csv import *

def read_og_file(og_path):
    GENE_DELIMETER = ", "
    og_dict = csv_to_dict(og_path, "Orthogroup", delimiter='\t')
    for og in og_dict:
        for species in og_dict[og]:
            og_dict[og][species] = og_dict[og][species].split(GENE_DELIMETER)
    return og_dict
