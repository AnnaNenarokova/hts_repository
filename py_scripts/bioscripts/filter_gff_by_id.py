#!/usr/bin/python3

inpath = "/home/anna/bioinformatics/novymonas/novymonas_wt_stringtie.gff"
outpath = "/home/anna/bioinformatics/novymonas/novymonas_no_pand_stringtie.gff"
infile = open(inpath, 'r')
outfile = open(outpath, 'w')

l = [
"NODE_2_length_844906_cov_870.704",
"NODE_822_length_1318_cov_1863.76",
"NODE_346_length_5920_cov_1555.3",
"NODE_121_length_88224_cov_845.318",
"NODE_106_length_108046_cov_858.69",
"NODE_104_length_108845_cov_889.343"
]

for row in infile:
	name = row.split('\t')[0]
	if name not in l:
		outfile.write(row)
infile.close()
outfile.close()
