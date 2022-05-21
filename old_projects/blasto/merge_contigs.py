#!/usr/bin/python3
from Bio import SeqIO

record_id_1 = "NODE_239_length_28967_cov_73.6657"
start_1=0
end_1=690

record_id_2 = "Ctg28_length_81690"
start_2=12


fasta_file_1="/Users/anna/work/blasto_local/genomes/ref_genomes/p57_illumina.fa"
fasta_file_2="/Users/anna/work/blasto_local/genomes/ref_genomes/p57_ra_polished.fa"

for record in SeqIO.parse(fasta_file_1, "fasta"):
    if record.id == record_id_1:
        seq1 = record.seq[start_1:end_1]
        break

for record in SeqIO.parse(fasta_file_2, "fasta"):
    if record.id == record_id_2:
        record_2 = record
        break

new_seq = seq1 + record_2.seq[start_2:]

new_seq_length = len(new_seq)
new_name = "Ctg28_length_" + str(new_seq_length)
record_2.seq = new_seq
record_2.id = new_name

result_file="/Users/anna/work/blasto_local/genomes/ref_genomes/Ctg28_corrected.fasta"
SeqIO.write(record_2, result_file, "fasta")