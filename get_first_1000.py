from Bio import SeqIO
for f in ('CTG_CCGTCC_L001_1.fastq', 'CTG_CCGTCC_L001_2.fastq'):
#for f in ('Kan-frag_ATGTCA_L001_1.fastq', 'Kan-frag_ATGTCA_L001_2.fastq'):
	input_dir = '/home/anna/HTS-all/HTSes/'
	seq_file = input_dir + f
	handle = open(seq_file, "rU")
	records = []
	i = 0
	for seq in SeqIO.parse(handle, "fastq"):
		records.append(seq)
		# print seq
		i += 1
		if i >= 1000: break
	output =  "/home/anna/HTS-all/HTS-programming/" + '1000_' + f
	print output
	SeqIO.write(records, output, "fastq")
	handle.close()
# print records[0].id  #first record
# print records[-1].id #last record