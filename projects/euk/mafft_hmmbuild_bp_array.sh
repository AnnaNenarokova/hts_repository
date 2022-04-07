#!/bin/bash

module load apps/mafft/7.429 apps/hmmer/3.3.2

bmge="/sw/apps/BMGE-1.12/BMGE.jar"

fasta_dir="/user/work/vl18625/euk/markers_nina/faa/"
msa_dir="/user/work/vl18625/euk/markers_nina/msa/"
hmm_dir="/user/work/vl18625/euk/markers_nina/hmm_profiles/"

cd $fasta_dir
fasta=$(ls *.faa | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $fasta

msa=$msa_dir$fasta
hmm_file=$hmm_dir$fasta

mafft $fasta > $msa
hmmbuild $hmm_file $msa