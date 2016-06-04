#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=60
#PBS -d.

folder='/home/nenarokova/contaminants/trimmed_reads'
bt2_base='/home/nenarokova/contaminants/genomes/blechomonas'
cd $folder
alignment='/home/nenarokova/contaminants/genomes/blechomonas_test.sam'
/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-fast -p 60 -x $bt2_base -1 H10-3_ACAGTG_L007_001_ad_q20_l50_paired_out_fw.fastq -2 H10-3_ACAGTG_L007_001_ad_q20_l50_paired_out_rv.fastq -U H10-3_ACAGTG_L007_001_ad_q20_l50_unpaired_out_fw.fastq,H10-3_ACAGTG_L007_001_ad_q20_l50_unpaired_out_rv.fastq -S $alignment
