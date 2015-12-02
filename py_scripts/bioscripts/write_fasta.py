from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
s = SeqRecord(Seq('AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCT'), id = 'wheat adapter', description = '')
SeqIO.write(s, "/home/anna/bioinformatics/wheat_adapter.fasta", "fasta")