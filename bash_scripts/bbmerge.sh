#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=60

folder='/home/nenarokova/assembly/wallacemonas/'
fw='18021_1#6_paired_out_fw_ad_q20_l50.fastq'
rv='18021_1#6_paired_out_rv_ad_q20_l50.fastq'
merged='18021_1#6_paired_out_rv_ad_q20_l50.fastq'
/home/nenarokova/tools/bbmap/bbmerge bbmerge.sh in1=$fw in2=$rv out=$merged
