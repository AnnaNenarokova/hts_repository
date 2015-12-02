from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
f = '/home/anna/bioinformatics/euglenozoa/euglena/sequences/E_gracilis_transcriptome_final.PROTEINS.fasta'
out = []
sum_len = 0
i = 0
for seqrecord in SeqIO.parse(f, "fasta"):
	seqrecord.seq = seqrecord.seq[:130]
	out.append(seqrecord)
	i+=1
	# if i == 10: break

outfile = '/home/anna/bioinformatics/euglenozoa/euglena/sequences/E_gracilis_transcriptome_final_PROTEINS_first_130.fasta'
SeqIO.write(out, outfile, "fasta")