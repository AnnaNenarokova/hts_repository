#!/usr/bin/python

import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from common_helpers.parse_csv import *
from common_helpers.make_outdir import *

numbers_csv_path = '/home/anna/bioinformatics/euglenozoa/mitocarta/mitocarta_numbers.csv'
info_csv_path  = '/home/anna/bioinformatics/euglenozoa/mitocarta/Human_MitoCarta2_0.csv'

id_dicts = csv_to_dict_list(numbers_csv_path)
main_key = 'HumanGeneID'
info_dict = csv_to_dict(info_csv_path, main_key=main_key)

for id_dict in id_dicts:
    info = info_dict[id_dict[main_key]]
    for key in info:
        id_dict[key] = info[key]

outfile = '/home/anna/bioinformatics/euglenozoa/mitocarta/Human.MitoCarta.2.0.csv'
write_dicts_list(id_dicts, outfile)