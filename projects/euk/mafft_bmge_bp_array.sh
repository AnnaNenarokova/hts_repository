#!/bin/bash

module load apps/bmge/1.12 apps/mafft/7.429

bmge="/sw/apps/BMGE-1.12/BMGE.jar"

fasta_dir="/user/work/vl18625/euk/ed_markers/anna_set_results/initial_results/faa/"
msa_dir="/user/work/vl18625/euk/ed_markers/anna_set_results/initial_results/msa_linsi/"
trimmed_msa_dir="/user/work/vl18625/euk/ed_markers/anna_set_results/initial_results/msa_linsi_bmge/"

cd $fasta_dir
fasta=$(ls *.faa | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $fasta

msa=$msa_dir$fasta
trimmed_msa=$trimmed_msa_dir$fasta

mafft-linsi --anysymbol $fasta > $msa
java -jar $bmge -i $msa -t "AA" -m BLOSUM30 -of $trimmed_msa