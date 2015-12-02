from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
f = '/home/anna/bioinformatics/euglenozoa/mitocarta/Human.MitoCarta2.0.fasta'
i = 0
out = []
sum_len = 0
for seqrecord in SeqIO.parse(f, "fasta"):
	length = len(seqrecord.seq)
	if length < 3000:
		out.append(seqrecord)
		sum_len += length
		i+=1
		if i==500: break

print sum_len
outfile = '/home/anna/bioinformatics/euglenozoa/mitocarta/below_4000.fasta'
SeqIO.write(out, outfile, "fasta")

