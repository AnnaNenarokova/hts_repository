#!python3
import os
import sys
sys.path.insert(0, "/Users/annanenarokova/work/code/ngs/")
from py_scripts.helpers.parse_csv import *

treedir_path="/Users/annanenarokova/work/dpapi_local/results/trees2/"
info_path="/Users/annanenarokova/work/dpapi_local/dpapi_refdataset_info.csv"
main_key = "old_id"
info_dict = csv_to_dict(info_path, main_key, delimiter=',')

os.chdir(treedir_path)
for file in os.listdir(treedir_path):
    old_name = file.split(".faa")[0]
    new_name = info_dict[old_name]['new_id']
    new_filename = new_name + ".tree"
    os.rename(file, new_filename)