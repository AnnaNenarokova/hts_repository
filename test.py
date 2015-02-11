#!/usr/bin/python
import json
json_file = '/home/anna/bioinformatics/htses/katya/indexes_result_json'
json_data=open(json_file, 'r')
a = json.load(json_data)
print a