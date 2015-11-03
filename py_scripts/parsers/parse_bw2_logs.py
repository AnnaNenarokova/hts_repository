#!/usr/bin/python
def parse_bw2_log(bw2_log_file):
	with open(bw2_log_file, 'r') as log:
		log_list = log.readlines()
		log.closed
	splitted_log_list = []
	for row in log_list:
		splitted_row = row.split()
		splitted_log_list.append(splitted_row)

	log_data = []
	log_data.append(splitted_log_list[0][0])
	
	for i in range(1, 5):
		log_data.append(splitted_log_list[i][0])
		log_data.append(splitted_log_list[i][1])
	log_data.append(splitted_log_list[6][0])
	log_data.append(splitted_log_list[7][0])
	log_data.append(splitted_log_list[7][1])
	log_data.append(splitted_log_list[9][0])
	log_data.append(splitted_log_list[10][0])
	for i in range(11, 18):
		log_data.append(splitted_log_list[i][0])
		log_data.append(splitted_log_list[i][1])
	log_data.append(splitted_log_list[18][0])
	
	for x in log_data: print x
	

bw2_log_file = '/home/anna/bioinformatics/wheat/bw2_all.sh.e40498-1'
parse_bw2_log(bw2_log_file)