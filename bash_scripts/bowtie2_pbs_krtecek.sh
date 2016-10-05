#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=60

bt2_base='/home/nenarokova/contaminants/genomes/'
bw2_reports='/home/nenarokova/genomes/kinetoplastids/pacbio/assembly/bw2_reports/'
read_folder='/home/nenarokova/contaminants/trimmed_reads/'
alignment_folder='/home/nenarokova/genomes/kinetoplastids/pacbio/assembly/bw2_mapping/alignments/'

fw_paired='18021_1_4_paired_out_fw_ad_q20_l50.fastq.gz'
rv_paired='18021_1_4_paired_out_rv_ad_q20_l50.fastq.gz'
fw_unpaired=$read_folder'18021_1_4_unpaired_out_fw_ad_q20_l50.fastq.gz'
rv_unpaired=$read_folder'18021_1_4_unpaired_out_rv_ad_q20_l50.fastq.gz'
alignment=$alignment_folder'18021_1_4_alignment.sam'
report=$reads_folder'18021_1_4_mapping_report.txt'
/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-sensitive -p 60 -x $bt2_base -1 $fw_paired -2 $rv_paired -U $fw_unpaired,$rv_unpaired -S $alignment 2> $report
