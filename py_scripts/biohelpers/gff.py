#!/usr/bin/python

infile = "/home/anna/bioinformatics/euglenozoa/euglena/sequences/augustus.abinitio.prediction.gbrowse.gff3"
outfile = '/home/anna/bioinformatics/euglenozoa/euglena/sequences/augustus_100_scaffolds.gff3'
handle = open(infile)
outfile = open(outfile, "w")
out=[]
i=0
for line in handle:
	if line[0] != '#': 
		scaffold_number = int(line.split('\t')[0].split('_')[4])
		if scaffold_number<=100:
			out.append(line)
handle.close()
outfile.writelines(out)
outfile.close()