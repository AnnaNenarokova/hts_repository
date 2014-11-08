from Bio import SeqIO
f = '/home/anna/bioinformatics/outdirs/contigs_mut6.fasta'
file_out = '/home/anna/bioinformatics/outdirs/contig_41_mut6.fasta'
for record in SeqIO.parse(f, "fasta"):
	if record.id == 'contig_41':
		SeqIO.write(record, file_out, "fasta")
