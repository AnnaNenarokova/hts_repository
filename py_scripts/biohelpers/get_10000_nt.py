from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
f = '/home/anna/bioinformatics/references/t5.fasta'
end_len = 10000
file_out = '/home/anna/bioinformatics/references/first_10_kb_t5.fasta'
record = SeqIO.read(f, "fasta")
seq = record.seq
seq_out = SeqRecord(seq[0:end_len], id =  str(record.id) + ' ' + 'first ' + str(end_len), description = '')
SeqIO.write(seq_out, file_out, "fasta")