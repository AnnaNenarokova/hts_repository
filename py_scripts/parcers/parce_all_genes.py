#!/usr/bin/python
from Bio import SeqIO
def find_genes(record, outdir):
	seq = record.seq
	# rev_seq = seq.reverse_complement()
	for gene_name in ['pep', 'yej', 'omp', 'rim', 'pdf', 'sbm', 'asp', 'def']:
	# for gene_name in ['pep']:
		genes = []
		for feature in record.features:
			if feature.type == 'gene':
				if 'gene' in feature.qualifiers:
					gene_name_gb = str(feature.qualifiers['gene'])
					gene_name_gb = gene_name_gb.translate(None, '\'!@#$[]')
					if gene_name in gene_name_gb:
						print gene_name_gb,
						start = feature.location.start
						# print start
						end = feature.location.end
						# print end
						print end - start
						# if feature.location.strand == 1:
						# 	print feature.location.strand
						# 	gene = SeqIO.SeqRecord(seq[start:end], id = str(gene_name_gb), description= '')
						# elif feature.location.strand == -1:
						# 	print feature.location.strand
						# 	gene = SeqIO.SeqRecord(seq[start:end].reverse_complement(), id =  str(gene_name_gb), description= '')
						# else: print 'Error'
						# file_out = outdir + str(gene_name_gb)+ '.fasta'
						# SeqIO.write(gene, file_out, "fasta")

file_gb = '/home/anna/bioinformatics/outdirs/BL21.gbk'
outdir = '/home/anna/bioinformatics/outdirs/genes/genes_bl/all_genes/'
record = SeqIO.read(file_gb, "genbank")
find_genes(record, outdir)