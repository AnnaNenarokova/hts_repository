#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=2:ppn=30
#PBS -d.

folder='/home/nenarokova/contaminants/trimmed_reads'
bt2_base='/home/nenarokova/contaminants/genomes/blechomonas'
cd $folder
alignment='/home/nenarokova/contaminants/genomes/blechomonas_test.sam'
/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-sensitive -p 60 -x $bt2_base -1 B08_TAGCTT_L001_ad_q20_l50_paired_out_fw.fastq -2 B08_TAGCTT_L001_ad_q20_l50_paired_out_rv.fastq -U B08_TAGCTT_L001_ad_q20_l50_unpaired_out_fw.fastq,B08_TAGCTT_L001_ad_q20_l50_unpaired_out_rv.fastq -S $alignment 2> /home/nenarokova/bw2_stats/b08_h10_vsens.txt
