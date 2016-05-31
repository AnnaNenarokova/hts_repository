#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=30
#PBS -d.

folder='/home/nenarokova/contaminants/trimmed_reads'
bt2_base='/home/nenarokova/contaminants/genomes/leptomonas'
cd $folder
alignment='/home/nenarokova/contaminants/genomes/leptomonas.sam'
/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-sensitive -p 30 --reorder -x $bt2_base -1 Leptomonas_seymouri_ad_q20_l50_paired_out_fw.fastq -2 Leptomonas_seymouri_ad_q20_l50_paired_out_rv.fastq -U Leptomonas_seymouri_ad_q20_l50_unpaired_out_fw.fastq,Leptomonas_seymouri_ad_q20_l50_unpaired_out_rv.fastq -S $alignment
