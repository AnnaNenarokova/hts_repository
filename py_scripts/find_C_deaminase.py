#!/usr/bin/python3
import os
import re
import subprocess
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/blasto_project/reference_tryps_proteoms/')
proteins = SeqIO.parse('TriTrypDB-35_TbruceiTREU927_AnnotatedProteins.fasta', 'fasta')
pseudogenes = open('pseudogenes.fa', 'w')
candidates = open('candidates.fa', 'w')
others = open('others.fa', 'w')

print('Searching for cytidine deaminase pattern')
for contig in proteins:
	if '*' in contig.seq:
		pseudogenes.write('>{}\n{}\n'.format(contig.description, contig.seq))
	else:
		if re.search(r'(H|C)\wE\w+PC\w{2}C', str(contig.seq)):
			candidates.write('>{}\n{}\n'.format(contig.description, contig.seq))
		else:
			others.write('>{}\n{}\n'.format(contig.description, contig.seq))
pseudogenes.close()
candidates.close()
others.close()

fasta = 'candidates.fa'
origin = 'animal'
ml_res = 'multiloc2_prediction.txt'

print('Running MultiLoc2')
subprocess.call('/usr/bin/python2.7 /home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py \
	-fasta={} -predictor=LowRes -origin={} -result={} -output=simple'.format(fasta, origin, ml_res), shell=True)
print('MultiLoc2 predictions done')