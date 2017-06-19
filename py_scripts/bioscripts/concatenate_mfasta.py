#!/usr/bin/python
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

fasta_file = '/home/anna/bioinformatics/blastocrithidia/scaffolding/reference_genomes/leish/leptomonas.fasta'
outfile = '/home/anna/bioinformatics/blastocrithidia/scaffolding/reference_genomes/leish/leptomonas_concatenated.fasta'
id='leptomonas_H10_concatenated'
handle = open(fasta_file, 'r')

whole_seq=''

for record in SeqIO.parse(handle, 'fasta'):
    cur_seq = record.seq
    whole_seq += cur_seq

result_record = SeqRecord(whole_seq,
        id=id, name='',
        description='')
SeqIO.write(result_record, open(outfile, 'w'), 'fasta')
