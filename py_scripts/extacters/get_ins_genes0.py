from Bio import SeqIO

def find_genes(record, outdir):
	seq = record.seq
	genes = []
	for feature in record.features:
		if feature.type == 'CDS':
				if 'gene' in feature.qualifiers:
					gene_name_gb = str(feature.qualifiers['gene'])
					if 'ins' in gene_name_gb:
						start = feature.location.start
						end = feature.location.end
						strand = feature.location.strand 
						seq_name = gene_name_gb.translate(None, '!@#$[]\'\"')
						description = 'start ' + str(start) + ' end ' + str(end)
						if 'product' in feature.qualifiers: 
							description = description + ' product ' + str(feature.qualifiers['product']).translate(None, '!@#$[]\'\"')
						if strand == 1: gene = SeqIO.SeqRecord(seq[start:end], id = seq_name, description = description)
						elif strand == -1: gene = SeqIO.SeqRecord(seq[start:end].reverse_complement(), id = seq_name, description = description)
						else: print 'Error'
						genes.append(gene)
	file_out = outdir + 'disruptedy_BL21' + '.fasta'
	SeqIO.write(genes, file_out, "fasta")

file_gb = '/home/anna/bioinformatics/outdirs/BL21.gbk'
outdir = '/home/anna/bioinformatics/outdirs/'
record = SeqIO.read(file_gb, "genbank")
find_genes(record, outdir)