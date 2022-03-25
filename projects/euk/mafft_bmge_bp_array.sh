#!/bin/bash

module load apps/bmge/1.12 apps/mafft/7.429

bmge="/sw/apps/BMGE-1.12/BMGE.jar"

fasta_dir="/user/work/vl18625/euk/ed_markers/faa_with_euks/"
msa_dir="/user/work/vl18625/euk/ed_markers/msa_with_euks/"
trimmed_msa_dir="/user/work/vl18625/euk/ed_markers/msa_w_euks_trimmed/"

cd $fasta_dir
fasta=$(ls *.faa | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $fasta

msa=$msa_dir$fasta
trimmed_msa=$trimmed_msa_dir$fasta

mafft-linsi $fasta > $msa
java -jar $bmge -i $msa -t "AA" -m BLOSUM30 -of $trimmed_msa