#!/usr/bin/python3
from collections import OrderedDict
from collections import defaultdict
from Bio import SeqIO

infile = SeqIO.parse('/home/kika/MEGAsync/blasto_project/genes/tRNAs/iqtree/trna_phylogeny_dataset2.fna', 'fasta')
out_fasta = open('/home/kika/MEGAsync/blasto_project/genes/tRNAs/iqtree/trna_phylogeny_deduplicated2.fasta', 'w')
out_dedupl = open('/home/kika/MEGAsync/blasto_project/genes/tRNAs/iqtree/duplicated_names2.txt', 'w')

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
    out_fasta.write('>{}\n{}\n'.format(value, key))

for key, value in multiplications.items():
    if len(value) > 1:
        out_dedupl.write('{}\n'.format(str(value)))

out_fasta.close()
out_dedupl.close()