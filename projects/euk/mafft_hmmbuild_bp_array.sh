#!/bin/bash

module load apps/mafft/7.429 apps/hmmer/3.3.2

bmge="/sw/apps/BMGE-1.12/BMGE.jar"

fasta_dir="/user/work/vl18625/euk/markers/nina_markers/anna_set_results/mono_euk_sets/set1/faa/"
msa_dir="/user/work/vl18625/euk/markers/nina_markers/anna_set_results/mono_euk_sets/set1/msa/"
hmm_dir="/user/work/vl18625/euk/markers/nina_markers/anna_set_results/mono_euk_sets/set1/hmm/"

cd $fasta_dir
fasta=$(ls *.fasta | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $fasta

msa=$msa_dir$fasta
hmm_file=$hmm_dir$fasta".hmm"

mafft --anysymbol $fasta > $msa
hmmbuild $hmm_file $msa