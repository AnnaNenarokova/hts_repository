#!/usr/bin/python
from Bio import SeqIO

record_id = '18021_1#1_trimmed_contig_199'
start = 7626
end = 7939

fasta_file = '/home/anna/Dropbox/phd/bioinformatics/kinetoplastids/CLC_assemblies/Jaenimonas_drosophilae_HiSeqMiSeq_assembly.fa'

for record in SeqIO.parse(fasta_file, "fasta"):
    if record_id == record.id:
        result = record[start:end].reverse_complement()

outpath = '/home/anna/Dropbox/phd/bioinformatics/kinetoplastids/CLC_assemblies/genes/Jaenimonas_drosophilae_sp_SSU.fst'

SeqIO.write(result, outpath, "fasta")
