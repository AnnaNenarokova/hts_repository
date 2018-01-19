#!/usr/bin/python3
import subprocess

db = '/home/kika/tara/andalucia_mtProteins_test_set.fa'
dbtype = 'prot'

subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype), shell=True)