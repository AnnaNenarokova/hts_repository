#!/bin/bash
folder='/media/4TB1/kinetoplastids_hinxton/jaculum/trimmed_reads'
cd $folder
alignment='/media/4TB1/kinetoplastids_hinxton/jaculum/jaculum_mapping/alignment.sam'
bt2_base='/media/4TB1/kinetoplastids_hinxton/pyrrhocoris_bt2/leptomonas'

out='/media/4TB1/kinetoplastids_hinxton/jaculum/bw2_stats/18021_1#5_pyrrhocoris.txt'
clean_reads_paired='/media/4TB1/kinetoplastids_hinxton/jaculum/cleaned_reads/18021_1#5_ad_q20_l50_paired_cleaned'
clean_reads_unpaired='/media/4TB1/kinetoplastids_hinxton/jaculum/cleaned_reads/18021_1#5_ad_q20_l50_unpaired_cleaned'
/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 -D 5 -R 1 -N 0 -L 32 -p 32 -x $bt2_base -1 18021_1#5_ad_q20_l50_paired_out_fw.fastq -2 18021_1#5_ad_q20_l50_paired_out_rv.fastq -U 18021_1#5_ad_q20_l50_unpaired_out_fw.fastq,18021_1#5_ad_q20_l50_unpaired_out_rv.fastq -S $alignment --un $clean_reads_unpaired --un-conc $clean_reads_paired 2> $out
