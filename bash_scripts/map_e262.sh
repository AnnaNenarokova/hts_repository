#!/bin/bash
read_folder='/media/4TB1/kinetoplastids_hinxton/illumina/hiseq/trimmed_reads/'
bt2_base='/media/4TB1/kinetoplastids_hinxton/pyrrhocoris_bt2/leptomonas'

out_folder='/media/4TB1/kinetoplastids_hinxton/illumina/contaminant_mapping/novymonas/'
alignment=$out_folder'alignment.sam'
out=$out_folder'bw2_stats/E262_paired_out_pyrrhocoris.txt'
clean_reads_paired=$out_folder'cleaned_reads/E262_paired_out_ad_q20_l50_paired_cleaned.fastq'
clean_reads_unpaired=$out_folder'cleaned_reads/E262_paired_out_ad_q20_l50_unpaired_cleaned.fastq'
paired_fw=$read_folder'E262_paired_out_paired_out_fw_ad_q20_l50.fastq'
paired_rv=$read_folder'E262_paired_out_paired_out_rv_ad_q20_l50.fastq'
unpaired_fw=$read_folder'E262_paired_out_unpaired_out_fw_ad_q20_l50.fastq'
unpaired_rv=$read_folder'E262_paired_out_unpaired_out_rv_ad_q20_l50.fastq'

/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 -D 5 -R 1 -N 0 -L 32 -p 32 -x $bt2_base -1 $paired_fw -2 $paired_rv -U $unpaired_fw,$unpaired_rv -S $alignment --un $clean_reads_unpaired --un-conc $clean_reads_paired 2> $out
