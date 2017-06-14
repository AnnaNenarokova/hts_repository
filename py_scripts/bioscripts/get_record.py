#!/usr/bin/python
from Bio import SeqIO

record_id ="EG_transcript_59561"

# start=10100
# end=11950
fasta_file = '/media/anna/data/Dropbox/PhD/projects/euglena/data/E_gracilis_transcriptome_final.TRANSCRIPTS.fasta'
# fasta_file = '/home/anna/bioinformatics/blasto/p57_DNA_scaffolds.fa'

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        result = record
        # result = record[start:end].reverse_complement()
        result.id="EG_transcript_59561"
        result.description=""
        break


outpath = '/media/anna/data/Dropbox/PhD/projects/euglena/data/EG_transcript_59561_transcript.fasta'

SeqIO.write(result, outpath, "fasta")
