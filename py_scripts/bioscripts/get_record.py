#!/usr/bin/python
from Bio import SeqIO

record_id ="NODE_16_length_151510_cov_87.9355"

# start=67500
# end=70500
# fasta_file = '/media/anna/data/Dropbox/PhD/projects/euglena/data/E_gracilis_transcriptome_final.TRANSCRIPTS.fasta'
fasta_file = '/home/anna/bioinformatics/blasto/p57_DNA_scaffolds.fa'
# fasta_file="/home/anna/bioinformatics/blasto/jaculum/jac_genome.fasta"

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        result = record
        # result = record[start:end]#.reverse_complement()
        # result.id="EG_transcript_59561"
        result.description=""
        break


outpath = '/home/anna/bioinformatics/blasto/ambar/NODE_16_length_151510_cov_87.9355.fna'

SeqIO.write(result, outpath, "fasta")
