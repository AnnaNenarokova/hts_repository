#!/usr/bin/python
from Bio import SeqIO
from Bio import Seq

fasta = '/home/anna/Dropbox/PhD/bioinformatics/trypanosomatids/blasto/blastocrithidia/genes/tRNAs/trna_phylogeny_dataset.fna'
results = {}

for record in SeqIO.parse(fasta, "fasta"):
    seq = record.seq
    if seq in results:
        results[seq].append(record.id)
    else:
        results[seq] = [record.id]

outpath = '/home/anna/Dropbox/PhD/bioinformatics/trypanosomatids/blasto/blastocrithidia/genes/tRNAs/trna_phylogeny_deduplicated.fna'
result_records = []
i = 0
with open(outpath, 'w') as outfile:
    for key in results:
        i += 1
        print i
        ref_sp = results[key][0]
        for sp in results[key]:
            try:
                val = int(sp[-1])
                print "Bad name", sp
            except ValueError:
                ref_sp = sp
                print "Good name",sp
                break
        outfile.write('>{}\n{}\n'.format(ref_sp,key))
    outfile.close()

