#!/usr/bin/python
import csv
group = {
'Sasha': { 'test1': 3, 'test2': 3, 'test3': 3, 'test4': 3, 'test5': 2},
'Dasha': { 'test1': 3, 'test2': 5, 'test3': 4, 'test4': 3 },
'Masha': { 'test1': 5, 'test3': 4, 'test4': 5, 'test5': 4}
}
print group
f_out_name = '/home/anna/bioinformatics/ngs/test_out.csv'
with open(f_out_name , 'wb') as f_out_name:
	dict_writer = csv.DictWriter(hits_file, keys)
	dict_writer.writeheader()
	# dict_writer.writer.writerow(keys)
	dict_writer.writerows(hit_records)
f_out.close()