#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=krtecek2:ppn=60
#PBS -d.

folder='/home/nenarokova/contaminants/trimmed_reads'
cd $folder
alignment='/home/nenarokova/contaminants/genomes/test.sam'

bt2_base='/home/nenarokova/contaminants/genomes/seymouri'

/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-fast -p 30 -x $bt2_base -1 H10-3_ACAGTG_L007_001_ad_q20_l50_paired_out_fw.fastq -2 H10-3_ACAGTG_L007_001_ad_q20_l50_paired_out_rv.fastq -U H10-3_ACAGTG_L007_001_ad_q20_l50_unpaired_out_fw.fastq,H10-3_ACAGTG_L007_001_ad_q20_l50_unpaired_out_rv.fastq -S $alignment 2> /home/nenarokova/contaminants/bw2_stats/h10_seymouri_vfast.txt
/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --fast -p 30 -x $bt2_base -1 H10-3_ACAGTG_L007_001_ad_q20_l50_paired_out_fw.fastq -2 H10-3_ACAGTG_L007_001_ad_q20_l50_paired_out_rv.fastq -U H10-3_ACAGTG_L007_001_ad_q20_l50_unpaired_out_fw.fastq,H10-3_ACAGTG_L007_001_ad_q20_l50_unpaired_out_rv.fastq -S $alignment 2> /home/nenarokova/contaminants/bw2_stats/h10_seymouri_fast.txt
/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --sensitive -p 30 -x $bt2_base -1 H10-3_ACAGTG_L007_001_ad_q20_l50_paired_out_fw.fastq -2 H10-3_ACAGTG_L007_001_ad_q20_l50_paired_out_rv.fastq -U H10-3_ACAGTG_L007_001_ad_q20_l50_unpaired_out_fw.fastq,H10-3_ACAGTG_L007_001_ad_q20_l50_unpaired_out_rv.fastq -S $alignment 2> /home/nenarokova/contaminants/bw2_stats/h10_seymouri_sens.txt
/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-sensitive -p 30 -x $bt2_base -1 H10-3_ACAGTG_L007_001_ad_q20_l50_paired_out_fw.fastq -2 H10-3_ACAGTG_L007_001_ad_q20_l50_paired_out_rv.fastq -U H10-3_ACAGTG_L007_001_ad_q20_l50_unpaired_out_fw.fastq,H10-3_ACAGTG_L007_001_ad_q20_l50_unpaired_out_rv.fastq -S $alignment 2> /home/nenarokova/contaminants/bw2_stats/h10_seymouri_vsens.txt

