from Bio import SeqIO
handle = open("/home/anna/HTS-all/HTS-programming/0min_R1.fasta", "rU")
i = 0

records = []

for seq in SeqIO.parse(handle, "fasta"):
	records.append(seq)
	# print seq
	i += 1
	if i >= 1000: break

SeqIO.write(records, "/home/anna/HTS-all/my_example.fasta", "fasta")

handle.close()
# print records[0].id  #first record
# print records[-1].id #last record