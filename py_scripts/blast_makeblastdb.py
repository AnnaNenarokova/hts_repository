#!/usr/bin/python3
import os

db = ''
dbtype = nucl

os.system('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype))