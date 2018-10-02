#!/usr/bin/python
from Bio import SeqIO

record_id ="E_gracilis_V1_Scaffold_14118"

# start=121324-800
# end=130140+800
# fasta_file = '/media/anna/data/Dropbox/PhD/projects/euglena/data/E_gracilis_transcriptome_final.TRANSCRIPTS.fasta'
# fasta_file = '/home/anna/bioinformatics/blasto/p57_DNA_scaffolds.fa'
# fasta_file="/home/anna/bioinformatics/blasto/jaculum/jac_genome.fasta"
fasta_file="/media/anna/data/big_files/Euglena_gracilis_genome_V1_nt.fasta/Euglena_gracilis_genome_V1.fasta"

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        result = record
        # result = record[start:end]#.reverse_complement()
        result.description=""
        break


outpath = '/home/anna/bioinformatics/euglena/E_gracilis_V1_Scaffold_14118.fasta'

SeqIO.write(result, outpath, "fasta")
