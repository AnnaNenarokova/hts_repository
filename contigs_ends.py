from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
contigs = '/home/anna/bioinformatics/outdirs/mut9/contigs_mut9.fasta'
file_out = '/home/anna/bioinformatics/outdirs/mut9_contigs_ends.fasta'
out = []
for record in SeqIO.parse(contigs, "fasta"): 
	seq1_out = SeqRecord(record.seq[0:1000], id = 'start_' + str(record.id),  description = '')
	out.append(seq1_out)
	seq2_out = SeqRecord(record.seq[-1000:-1], id = 'end_' + str(record.id),  description = '')
	out.append(seq2_out)
SeqIO.write(out, file_out, "fasta")