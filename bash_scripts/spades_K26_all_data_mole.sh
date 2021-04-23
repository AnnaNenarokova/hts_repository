#!/bin/bash
module load SPAdes-3.14.0
se1="/home/users/nenarokova/hypsa/crataerina/crataerina_AN/K26_adapter_trimmed_merged.fq.gz"
pe1_1="/home/users/nenarokova/hypsa/crataerina/crataerina_AN/K26_adapter_trimmed_unmerged_1.fq.gz"
pe1_2="/home/users/nenarokova/hypsa/crataerina/crataerina_AN/K26_adapter_trimmed_unmerged_2.fq.gz"

pe2_1="/home/users/nenarokova/hypsa/crataerina/crataerina_AN/Eliska_Crataerina_R1_qtrim_bbduk.fastq.gz"
pe2_2="/home/users/nenarokova/hypsa/crataerina/crataerina_AN/Eliska_Crataerina_R2_qtrim_bbduk.fastq.gz"

outdir="/home/users/nenarokova/hypsa/crataerina/K26_all_data_spades/"

threads=120
ram=1000

mkdir $outdir
spades.py -m $ram --s1 $se1 --pe1-1 $pe1_1 --pe1-2 $pe1_2 --pe2-1 $pe2_1 --pe2-2 $pe2_2 -t $threads -o $outdir 