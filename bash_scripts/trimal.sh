#!/bin/bash
trimal="/home/users/nenarokova/tools/trimAl/source/trimal"

msa="/home/users/nenarokova/zachar/scf25_dataset/pasta/pastajob.marker001.scf25_dataset.faa.aln"
trimmed_msa="/home/users/nenarokova/zachar/scf25_dataset/scf25_dataset_trimmed_msa.fasta"

$trimal -in $msa -out $trimmed_msa -fasta -automated1

