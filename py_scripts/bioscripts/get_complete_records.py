#!/usr/bin/python
from Bio import SeqIO

fasta_files = [
"/home/anna/bioinformatics/euglenozoa_anzhelika/Dataset_cd_hit_est_0_9/Bodo_saltans_trinity_transcriptome_assembly_cd_hit_est5_transdecoder_pep.fa",
"/home/anna/bioinformatics/euglenozoa_anzhelika/Dataset_cd_hit_est_0_9/Dp_transcriptome_cd_hit_est5_transdecoder_pep.fa",
"/home/anna/bioinformatics/euglenozoa_anzhelika/Dataset_cd_hit_est_0_9/Euglena_gracilis_Yoshida_GDJR01.1_cd_hit_est5_transdecoder_pep.fa",
"/home/anna/bioinformatics/euglenozoa_anzhelika/Dataset_cd_hit_est_0_9/Eutreptiella_gymnastica_MMETSP0039_cd_hit_est5_transdecoder_pep.fa",
"/home/anna/bioinformatics/euglenozoa_anzhelika/Dataset_cd_hit_est_0_9/Hemistasia_cutadapt_trinity_run3_cd_hit_est5_transdecoder_pep.fa",
"/home/anna/bioinformatics/euglenozoa_anzhelika/Dataset_cd_hit_est_0_9/LmajorFriedlin_transcriptome_trinity_cd_hit_est5_transdecoder_pep.fa",
"/home/anna/bioinformatics/euglenozoa_anzhelika/Dataset_cd_hit_est_0_9/Neobodo_designis_MMETSP1114_cd_hit_est5_transdecoder_pep.fa",
"/home/anna/bioinformatics/euglenozoa_anzhelika/Dataset_cd_hit_est_0_9/Ngruberi_GCF_000004985.1_V1.0_protein.fa",
"/home/anna/bioinformatics/euglenozoa_anzhelika/Dataset_cd_hit_est_0_9/RhaCos_20160208_all_together_assembly_cd_hit_est5_transdecoder_pep.fa",
"/home/anna/bioinformatics/euglenozoa_anzhelika/Dataset_cd_hit_est_0_9/Tbrucei_Lister427_trinity_cd_hit_est5_transdecoder_pep.fa"
]

for fasta_file in fasta_files:
    results = []
    outpath = fasta_file[:-2]+ "_complete_ORFs.fa"
    for record in SeqIO.parse(fasta_file, "fasta"):
        if "ORF type:complete" in record.description:
            results.append(record)
    SeqIO.write(results, outpath, "fasta")
