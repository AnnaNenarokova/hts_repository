#!/usr/bin/python3
from subprocess import call
import matplotlib.pyplot as plt
from Bio import SeqIO
from Bio import motifs

def get_codon_environs(gff_path, bed_out_path=False, left_border=-200, right_border=200, spades_ids=False, feature="gene", stops_included="False", starts=False):
	if not bed_out_path:
		if starts:
			bed_out_path='{}_{}_{}_start_environs.bed'.format(gff_path[:-4],left_border, right_border)
		else:
			bed_out_path='{}_{}_{}_stop_environs.bed'.format(gff_path[:-4],left_border, right_border)
	if stops_included:
		left_border -= 3
		right_border -= 3
	codon_environs = {}
	with open(gff_path, 'r') as gff_file:
		len_contigs={}
		with open(bed_out_path, 'w') as output:
			for row in gff_file:
				if row[0] != "#":
					split_row = row.split('\t')
					contig_id = split_row[0]
					feature_type = split_row[2]
					gene_start = int(split_row[3])
					gene_end = int(split_row[4])
					score = split_row[5]
					strand = split_row[6][0]
					if feature_type == feature:
						if gene_end < gene_start:
							print "Gene end < gene start error"
							print gene_start, gene_end
						else:
							if starts:
								if strand == "+":
									current_borders = [gene_start+left_border, gene_start+right_border]
								elif strand == "-":
									current_borders = [gene_end-right_border-1, gene_end-left_border-1]
								else:
									print "GFF strand error"
							else:
								if strand == "+":
									current_borders = [gene_end+left_border, gene_end+right_border]
								elif strand == "-":
									current_borders = [gene_start-right_border-1, gene_start-left_border-1]
								else:
									print "GFF strand error"
									exit(1)
								if contig_id not in codon_environs.keys():
									codon_environs[contig_id]=[]
								if current_borders[0] > 0:
									codon_environs[contig_id].append( {"strand":strand, "borders": current_borders} )
							new_row = '{}\t{}\t{}\t{}\t{}\t{}\n'.format(contig_id, current_borders[0], current_borders[1], 'name', score, strand)
							print new_row
							output.write(new_row)
		output.close()
	gff_file.close()
	return codon_environs, bed_out_path

def codon_usage_per_position(fasta_path):
	codon_usage = False
	for record in SeqIO.parse(fasta_path, "fasta"):
		seq = record.seq.upper()
		seq_length = len(seq)
		if not codon_usage:
			codon_usage = [{} for x in range(seq_length/3)]
		for i, k in enumerate(range(0, seq_length, 3)):
			codon = str(seq[k:k+3])
			if codon in codon_usage[i].keys():
				codon_usage[i][codon]+= 1
			else:
				codon_usage[i][codon] = 1
	return codon_usage

def gc_per_position(fasta_path):
	gc_usage = False
	for record in SeqIO.parse(fasta_path, "fasta"):
		seq = record.seq.upper()
		seq_length = len(seq)
		if not gc_usage:
			gc_usage = [{"A": 0, "C": 0, "G": 0, "T": 0} for x in range(seq_length)]
		for i, k in enumerate(range(0, seq_length)):
			codon = str(seq[k])
			if codon in gc_usage[i].keys():
				gc_usage[i][codon]+= 1
	return gc_usage


def create_logo_from_fasta(fasta_path, logo_path):
	sequences=[]
	for record in SeqIO.parse(fasta_path, "fasta"):
		seq = record.seq.upper()
		if "N" not in str(seq) and "Y" not in str(seq):
			sequences.append(seq)
	motif = motifs.create(sequences)
	motif.weblogo(logo_path)
	print "Logo is available in " + logo_path
	return 0

left_border = -300
right_border = 0

in_fasta="/home/anna/bioinformatics/all_tryp_references/TriTrypDB-34_TbruceiTREU927_Genome.fasta"
gff_path="/home/anna/bioinformatics/all_tryp_references/TriTrypDB-34_TbruceiTREU927_cleaned.gff"

codon_environs, bed_path = get_codon_environs(gff_path, left_border=left_border, right_border=right_border, spades_ids=False, feature="gene", stops_included=True)


logo_path='{}_{}_{}_stop_environs_logo.png'.format(gff_path[:-4],left_border, right_border)

out_fasta=bed_path[:-3]+"fna"

bedtools_call = ['bedtools', 'getfasta', '-fi', in_fasta, '-bed', bed_path, '-fo', out_fasta, '-s']
call(bedtools_call)

fasta_path=out_fasta

print fasta_path

create_logo_from_fasta(fasta_path, logo_path)

codon_usage = codon_usage_per_position(fasta_path)

interest_codons = {
	"TAA"  : [],
	# "GAA"  : [],
	"TAG"  : [],
	# "GAG"  : [],
	"TGA"  : []
	# "TGG"  : []
}
# interest_codons = {
#	 "AAA"  : [],
#	 "TAA"  : [],
#	 "ATA"  : [],
#	 "AAT"  : [],
#	 "ATT"  : [],
#	 "TAT"  : [],
#	 "TTA"  : [],
#	 "TTT"  : []
# }
for pos in codon_usage:
	for interest_codon in interest_codons:
		if interest_codon in pos.keys():
			interest_codons[interest_codon].append(pos[interest_codon])
		else:
			interest_codons[interest_codon].append(0)


plots = []

codon_left_border = left_border/3
codon_right_border = right_border/3

x = range(codon_left_border, codon_right_border)

for interest_codon in interest_codons:
	print interest_codon
	coverage = interest_codons[interest_codon]
	print len(coverage)
	if interest_codon == "TAA":
		new_plot = plt.plot(x,coverage,label=interest_codon, linewidth=1.0)
	else:
		new_plot = plt.plot(x,coverage,label=interest_codon, linewidth=1.0)


# gc_usage = gc_per_position(fasta_path)

# nts = {"A": [], "C": [], "G": [], "T": []}

# for pos in gc_usage:
# 	 for nt in nts:
# 		 nts[nt].append(pos[nt])


# plots = []

# x = range(left_border, right_border)

# for nt in nts:
# 	 print nt
# 	 coverage = nts[nt]
# 	 print len(coverage)
# 	 new_plot = plt.plot(x,coverage,label=nt)

plt.legend()

plt.show()

