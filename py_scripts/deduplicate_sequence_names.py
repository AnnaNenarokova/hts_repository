#!/usr/bin/python3
from Bio import SeqIO
from collections import OrderedDict
from collections import defaultdict

infile = SeqIO.parse('/home/kika/Dropbox/test.fa', 'fasta')
output1 = open('/home/kika/Dropbox/test_dedupl.fa', 'w')
output2 = open('/home/kika/Dropbox/test_dupl_names.fa', 'w')

multiplications = defaultdict(list)
seq_dict = OrderedDict()
for sequence in infile:
	multiplications[sequence.name].append(sequence.seq)
	if sequence.name not in seq_dict:
		seq_dict[sequence.description] = sequence.seq

for key, value in seq_dict.items():
	output1.write('>{}\n{}\n'.format(key, value))

for key, value in multiplications.items():
    if len(value) > 1:
        output2.write('{}\n'.format(str(key)))

output1.close()
output2.close()