#!/usr/bin/python3
from collections import OrderedDict
from collections import defaultdict
from Bio import SeqIO

infile = SeqIO.parse('/home/kika/scripts/EC/outfile.fasta', 'fasta')
output1 = open('/home/kika/scripts/EC/outfile_dedupl_acc.fasta', 'w')
output2 = open('/home/kika/scripts/EC/outfile_dupl_names.txt', 'w')

multiplications = defaultdict(list)
seq_dict = OrderedDict()
for sequence in infile:
    multiplications[sequence.seq].append(sequence.name)
    if sequence.seq not in seq_dict:
    	#rename full header only with name (acc, till the first space)
        seq_dict[sequence.seq] = sequence.name 
        #keep full header			
        # seq_dict[sequence.seq] = sequence.description

for key, value in seq_dict.items():
    output1.write('>{}\n{}\n'.format(value, key))

for key, value in multiplications.items():
    if len(value) > 1:
        output2.write('{}\n'.format(str(value)))

output1.close()
output2.close()