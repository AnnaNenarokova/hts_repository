#!/usr/bin/python

f='/home/anna/Dropbox/PhD/bioinformatics/blasto/blastocrithidia/proteomics/all_peptides_triat.txt'
out=open("/home/anna/Dropbox/PhD/bioinformatics/blasto/blastocrithidia/proteomics/all_peptides_triat.faa", "w")
with open(f) as f:
    i=0
    for s in f:
        out.write('>{}\n{}\n'.format(i, s))
        i=i+1
    f.close()
    print i

out.close

