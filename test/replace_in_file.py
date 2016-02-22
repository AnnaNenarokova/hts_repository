#!/usr/bin/python

file_path = '/home/anna/Dropbox/phd/db/proteomes/parsed_ortho_groups.csv'
outpath = '/home/anna/Dropbox/phd/db/proteomes/parsed_ortho_groups_f.csv'

with open(file_path, 'r') as f:
    data = f.read()
    f.closed

data = data.replace(';', '|').replace(',', ';').replace('|', ',')

with open(outpath, 'w') as f:
    f.write(data)
    f.closed