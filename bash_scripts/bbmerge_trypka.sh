#!/bin/bash

folder='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/trimmed_reads/'
fw=$folder'18021_1#6_paired_out_fw_ad_q20_l50.fastq'
rv=$folder'18021_1#6_paired_out_rv_ad_q20_l50.fastq'
merged='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/merged_reads/18021_1#6_merged.fq'
unmerged_fw='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/merged_reads/18021_1#6_unmerged_fw.fq'
unmerged_rv='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/merged_reads/18021_1#6_unmerged_rv.fq'
/home/nenarokova/tools/bbmap/bbmerge.sh in1=$fw in2=$rv out=$merged outu1=$unmerged_fw outu2=$unmerged_rv strict=t qtrim2=t tbo=t usejni=t
