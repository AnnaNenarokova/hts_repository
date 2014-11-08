from Bio import SeqIO

def find_genes(record, outdir):
	seq = record.seq
	genes = []
	for feature in record.features:
		if feature.type == 'CDS':
				if 'gene' in feature.qualifiers:
					gene_name_gb = str(feature.qualifiers['gene']).translate(None, '!@#$[]\'\"')
					# if 'ins' in gene_name_gb:
					start = feature.location.start
					end = feature.location.end
					strand = feature.location.strand 
					description = 'start ' + str(start) + ' end ' + str(end)
					if 'product' in feature.qualifiers:
						product = str(feature.qualifiers['product']).translate(None, '!@#$[]\'\"')
						if "disrupted" in product:
							description = description + ' product ' + product
							if strand == 1: gene = SeqIO.SeqRecord(seq[start:end], id = gene_name_gb, description = description)
							elif strand == -1: gene = SeqIO.SeqRecord(seq[start:end].reverse_complement(), id = gene_name_gb, description = description)
							else: print 'Error'
							genes.append(gene)
	file_out = outdir + 'disrupted_BL21' + '.fasta'
	SeqIO.write(genes, file_out, "fasta")

file_gb = '/home/anna/bioinformatics/outdirs/BL21.gbk'
outdir = '/home/anna/bioinformatics/outdirs/'
record = SeqIO.read(file_gb, "genbank")
find_genes(record, outdir)