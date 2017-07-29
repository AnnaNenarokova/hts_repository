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
					if strand == "+":
						if feature_type == feature:
							if gene_end <= gene_start:
								print "Gene end <= gene start error"
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
		if "N" not in str(seq):
			sequences.append(seq)
	motif = motifs.create(sequences)
	motif.weblogo(logo_path)
	print "Logo is available in " + logo_path
	return 0

left_border = -300
right_border = 300

in_fasta="/home/anna/bioinformatics/blasto/utr_analysis/P57/p57_DNA_scaffolds.fa"
gff_path="/home/anna/bioinformatics/blasto/utr_analysis/P57/annotation_only_TAA.gff"
gff_path="/home/anna/bioinformatics/blasto/utr_analysis/P57/annotation_only_TAA_distance_10.gff"
codon_environs, bed_path = get_codon_environs(gff_path, left_border=left_border, right_border=right_border, spades_ids=True, feature="gene", stops_included=False)

# in_fasta="/home/anna/bioinformatics/blasto/utr_analysis/LpyrH10/GCF_001293395.1_ASM129339v1_genomic.fna"
# gff_path="/home/anna/bioinformatics/blasto/utr_analysis/LpyrH10/GCF_001293395.1_ASM129339v1_genomic.gff"
# codon_environs, bed_path = get_codon_environs(gff_path, left_border=left_border, right_border=right_border, spades_ids=False, feature="CDS", stops_included=True)

# in_fasta="/home/anna/bioinformatics/blasto/utr_analysis/novymonas/nesm_pseudochr.fasta"
# gff_path="/home/anna/bioinformatics/blasto/utr_analysis/novymonas/nesm_pseudo.out.gff3"
# codon_environs, bed_path = get_codon_environs(gff_path, left_border=left_border, right_border=right_border, spades_ids=False, feature="CDS", stops_included=True)

# in_fasta="/home/anna/bioinformatics/blasto/utr_analysis/blechomonas/TriTrypDB-33_BayalaiB08-376_Genome.fasta"
# gff_path="/home/anna/bioinformatics/blasto/utr_analysis/blechomonas/TriTrypDB-33_BayalaiB08-376.gff"
# codon_environs, bed_path = get_codon_environs(gff_path, left_border=left_border, right_border=right_border, spades_ids=False, feature="CDS", stops_included=True)

# in_fasta="/home/anna/bioinformatics/blasto/utr_analysis/lseymouri/TriTrypDB-33_LseymouriATCC30220_Genome.fasta"
# gff_path="/home/anna/bioinformatics/blasto/utr_analysis/lseymouri/TriTrypDB-33_LseymouriATCC30220.gff"
# codon_environs, bed_path = get_codon_environs(gff_path, left_border=left_border, right_border=right_border, spades_ids=False, feature="CDS", stops_included=True)

# in_fasta="/home/anna/bioinformatics/blasto/utr_analysis/LpyrH10/old/Leptomonas_pyrrhocoris.fa"
# gff_path="/home/anna/bioinformatics/blasto/utr_analysis/LpyrH10/old/Leptomonas_pyrrhocoris_with_UTRs_all_genes_stops_corrected.gff"
# codon_environs, bed_path = get_codon_environs(gff_path, left_border=left_border, right_border=right_border, spades_ids=False, feature="CDS", stops_included=False)


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
	new_plot = plt.plot(x,coverage,label=interest_codon)

plt.legend()

plt.show()

# gc_usage = gc_per_position(fasta_path)

# nts = {"A": [], "C": [], "G": [], "T": []}

# for pos in gc_usage:
#	 for nt in nts:
#		 nts[nt].append(pos[nt])


# plots = []

# x = range(left_border, right_border)

# for nt in nts:
#	 print nt
#	 coverage = nts[nt]
#	 print len(coverage)
#	 new_plot = plt.plot(x,coverage,label=nt)

# plt.legend()

# plt.show()

