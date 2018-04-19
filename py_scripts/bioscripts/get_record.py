#!/usr/bin/python
from Bio import SeqIO

record_id ="NODE_66_length_163735_cov_20.876"

start=121324-800
end=130140+800
# fasta_file = '/media/anna/data/Dropbox/PhD/projects/euglena/data/E_gracilis_transcriptome_final.TRANSCRIPTS.fasta'
# fasta_file = '/home/anna/bioinformatics/blasto/p57_DNA_scaffolds.fa'
# fasta_file="/home/anna/bioinformatics/blasto/jaculum/jac_genome.fasta"
fasta_file="/media/anna/data/anna_drive/projects/novymonas/novymonas/novymonas_no_pand_scaffolds.fasta"

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        result = record
        result = record[start:end]#.reverse_complement()
        # result.id="EG_transcript_59561"
        result.description=""
        break


outpath = '/media/anna/data/anna_drive/projects/novymonas/novymonas/for_paula/NESM_000750700.1_genome_region.fna'

SeqIO.write(result, outpath, "fasta")
