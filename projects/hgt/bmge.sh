#!/bin/bash
bmge="/home/users/nenarokova/tools/BMGE-1.12/BMGE.jar"
msa="/home/users/nenarokova/zachar/scf25_dataset/pasta/pastajob.marker001.scf25_dataset.faa.aln"
trimmed_msa="/home/users/nenarokova/zachar/scf25_dataset/scf25_dataset_trimmed_msa.fasta"

java -jar $bmge -i $msa -t "AA" -of $trimmed_msa
