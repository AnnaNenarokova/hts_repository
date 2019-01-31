#!/usr/bin/python
from Bio import SeqIO

record_id ="NODE_42_length_111303_cov_86.2536"

# start=121324-800
# end=130140+800
# fasta_file = '/media/anna/data/Dropbox/PhD/projects/euglena/data/E_gracilis_transcriptome_final.TRANSCRIPTS.fasta'
# fasta_file = '/home/anna/bioinformatics/blasto/p57_DNA_scaffolds.fa'
# fasta_file="/home/anna/bioinformatics/blasto/jaculum/jac_genome.fasta"
fasta_file="/home/anna/bioinformatics/blasto_local/p57_scaffolds.fasta"

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        result = record
        # result = record[start:end]#.reverse_complement()
        result.description=""
        break


outpath = '/home/anna/bioinformatics/blasto_local/p57_scaffolds_NODE_42.fasta'

SeqIO.write(result, outpath, "fasta")
