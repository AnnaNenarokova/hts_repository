#!/usr/bin/python
from Bio import SeqIO

fasta_files = [
"/home/anna/bioinformatics/euglenozoa_anzhelika/Dataset_cd_hit_est_0_9/complete_ORFs/Bodo_saltans_trinity_transcriptome_assembly_cd_hit_est5_transdecoder_pep._complete_ORFs.fa",
"/home/anna/bioinformatics/euglenozoa_anzhelika/Dataset_cd_hit_est_0_9/complete_ORFs/Dp_transcriptome_cd_hit_est5_transdecoder_pep._complete_ORFs.fa",
"/home/anna/bioinformatics/euglenozoa_anzhelika/Dataset_cd_hit_est_0_9/complete_ORFs/Euglena_gracilis_Yoshida_GDJR01.1_cd_hit_est5_transdecoder_pep._complete_ORFs.fa",
"/home/anna/bioinformatics/euglenozoa_anzhelika/Dataset_cd_hit_est_0_9/complete_ORFs/Eutreptiella_gymnastica_MMETSP0039_cd_hit_est5_transdecoder_pep._complete_ORFs.fa",
"/home/anna/bioinformatics/euglenozoa_anzhelika/Dataset_cd_hit_est_0_9/complete_ORFs/Hemistasia_cutadapt_trinity_run3_cd_hit_est5_transdecoder_pep._complete_ORFs.fa",
"/home/anna/bioinformatics/euglenozoa_anzhelika/Dataset_cd_hit_est_0_9/complete_ORFs/LmajorFriedlin_transcriptome_trinity_cd_hit_est5_transdecoder_pep._complete_ORFs.fa",
"/home/anna/bioinformatics/euglenozoa_anzhelika/Dataset_cd_hit_est_0_9/complete_ORFs/Neobodo_designis_MMETSP1114_cd_hit_est5_transdecoder_pep._complete_ORFs.fa",
"/home/anna/bioinformatics/euglenozoa_anzhelika/Dataset_cd_hit_est_0_9/complete_ORFs/Ngruberi_GCF_000004985.1_V1.0_protein._complete_ORFs.fa",
"/home/anna/bioinformatics/euglenozoa_anzhelika/Dataset_cd_hit_est_0_9/complete_ORFs/RhaCos_20160208_all_together_assembly_cd_hit_est5_transdecoder_pep._complete_ORFs.fa",
"/home/anna/bioinformatics/euglenozoa_anzhelika/Dataset_cd_hit_est_0_9/complete_ORFs/Tbrucei_Lister427_trinity_cd_hit_est5_transdecoder_pep._complete_ORFs.fa"
]

for fasta_file in fasta_files:
    n_seq = 0
    total_len = 0
    for record in SeqIO.parse(fasta_file, "fasta"):
        n_seq += 1
        total_len += len(record.seq)
    print fasta_file
    print total_len/float(n_seq)



