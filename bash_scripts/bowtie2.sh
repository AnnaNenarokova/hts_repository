#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=60
#PBS -d.

folder='/home/nenarokova/contaminants/trimmed_reads'
cd $folder
alignment='/home/nenarokova/contaminants/genomes/test.sam'

bt2_base='/home/nenarokova/contaminants/genomes/blechomonas'

/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-fast -p 60 -x $bt2_base -1 B08_S2_L001_ad_q20_l50_paired_out_fw.fastq -2 B08_S2_L001_ad_q20_l50_paired_out_rv.fastq -U B08_S2_L001_ad_q20_l50_unpaired_out_fw.fastq,B08_S2_L001_ad_q20_l50_unpaired_out_rv.fastq -S $alignment 2> /home/nenarokova/bw2_stats/b08s2_b08_vfast.txt
/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --fast -p 60 -x $bt2_base -1 B08_S2_L001_ad_q20_l50_paired_out_fw.fastq -2 B08_S2_L001_ad_q20_l50_paired_out_rv.fastq -U B08_S2_L001_ad_q20_l50_unpaired_out_fw.fastq,B08_S2_L001_ad_q20_l50_unpaired_out_rv.fastq -S $alignment 2> /home/nenarokova/bw2_stats/b08s2_b08_fast.txt
/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --sensitive -p 60 -x $bt2_base -1 B08_S2_L001_ad_q20_l50_paired_out_fw.fastq -2 B08_S2_L001_ad_q20_l50_paired_out_rv.fastq -U B08_S2_L001_ad_q20_l50_unpaired_out_fw.fastq,B08_S2_L001_ad_q20_l50_unpaired_out_rv.fastq -S $alignment 2> /home/nenarokova/bw2_stats/b08s2_b08_sens.txt
/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-sensitive -p 60 -x $bt2_base -1 B08_S2_L001_ad_q20_l50_paired_out_fw.fastq -2 B08_S2_L001_ad_q20_l50_paired_out_rv.fastq -U B08_S2_L001_ad_q20_l50_unpaired_out_fw.fastq,B08_S2_L001_ad_q20_l50_unpaired_out_rv.fastq -S $alignment 2> /home/nenarokova/bw2_stats/b08s2_b08_vsens.txt

bt2_base='/home/nenarokova/contaminants/genomes/leptomonas'

/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-fast -p 60 -x $bt2_base -1 B08_S2_L001_ad_q20_l50_paired_out_fw.fastq -2 B08_S2_L001_ad_q20_l50_paired_out_rv.fastq -U B08_S2_L001_ad_q20_l50_unpaired_out_fw.fastq,B08_S2_L001_ad_q20_l50_unpaired_out_rv.fastq -S $alignment 2> /home/nenarokova/bw2_stats/b08s2_h10_vfast.txt
/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --fast -p 60 -x $bt2_base -1 B08_S2_L001_ad_q20_l50_paired_out_fw.fastq -2 B08_S2_L001_ad_q20_l50_paired_out_rv.fastq -U B08_S2_L001_ad_q20_l50_unpaired_out_fw.fastq,B08_S2_L001_ad_q20_l50_unpaired_out_rv.fastq -S $alignment 2> /home/nenarokova/bw2_stats/b08s2_h10_fast.txt
/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --sensitive -p 60 -x $bt2_base -1 B08_S2_L001_ad_q20_l50_paired_out_fw.fastq -2 B08_S2_L001_ad_q20_l50_paired_out_rv.fastq -U B08_S2_L001_ad_q20_l50_unpaired_out_fw.fastq,B08_S2_L001_ad_q20_l50_unpaired_out_rv.fastq -S $alignment 2> /home/nenarokova/bw2_stats/b08s2_h10_sens.txt
/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-sensitive -p 60 -x $bt2_base -1 B08_S2_L001_ad_q20_l50_paired_out_fw.fastq -2 B08_S2_L001_ad_q20_l50_paired_out_rv.fastq -U B08_S2_L001_ad_q20_l50_unpaired_out_fw.fastq,B08_S2_L001_ad_q20_l50_unpaired_out_rv.fastq -S $alignment 2> /home/nenarokova/bw2_stats/b08s2_h10_vsens.txt
