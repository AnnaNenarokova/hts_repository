#!/usr/bin/python3
from collections import OrderedDict
from collections import defaultdict
from Bio import SeqIO

infile = SeqIO.parse('/home/kika/Dropbox/blastocrithidia/genes/PABP/PABP1+2_PASTA/PABP_euk.fa', 'fasta')
output1 = open('/home/kika/Dropbox/blastocrithidia/genes/PABP/PABP1+2_PASTA/PABP_euk_dedupl.fa', 'w')
output2 = open('/home/kika/Dropbox/blastocrithidia/genes/PABP/PABP1+2_PASTA/PABP_euk_dupl_names.fa', 'w')

multiplications = defaultdict(list)
seq_dict = OrderedDict()
for sequence in infile:
    multiplications[sequence.seq].append(sequence.name)
    if sequence.seq not in seq_dict:
        seq_dict[sequence.seq] = sequence.name 				#rename full header only with name (acc number till the first space)
        													#no need to rename sequences then
        # seq_dict[sequence.seq] = sequence.description		#keep the full header


for key, value in seq_dict.items():
    output1.write('>{}\n{}\n'.format(value, key))

for key, value in multiplications.items():
    if len(value) > 1:
        output2.write('{}\n'.format(str(value)))

output1.close()
output2.close()