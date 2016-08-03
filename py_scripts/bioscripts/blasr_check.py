#!/usr/bin/python
lpyr_alignment = '/home/anna/Dropbox/phd/bioinformatics/genomes/hinxton/novymonas/Lpyr_aligned_PacBio_reads.txt'
pand_alignment = '/home/anna/Dropbox/phd/bioinformatics/genomes/hinxton/novymonas/p_apista_blasr_only_reads'
movie_prefix = None
pand = []
for line in open(pand_alignment):
    pand.append(line.rstrip())

for i, line in enumerate(open(lpyr_alignment)):
    if i % 10000 == 0:
        print 'line', i

    alignment_id = line.split()[0]
    if alignment_id in pand:
        print alignment_id
