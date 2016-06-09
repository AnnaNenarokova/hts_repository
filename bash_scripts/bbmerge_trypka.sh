#!/bin/bash

folder='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/raw_reads'
fw='18021_1#6_1.fastq'
rv='18021_1#6_2.fastq'
merged='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/merged_reads/18021_1#6_merged.fq'
unmerged_fw='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/merged_reads/18021_1#6_unmerged_fw.fq'
unmerged_rv='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/merged_reads/18021_1#6_unmerged_rv.fq'
/home/nenarokova/tools/bbmap/bbmerge.sh in1=$fw in2=$rv out=$merged outu1=$unmerged_fw outu2=$unmerged_rv strict=t qtrim2=t tbo=t usejni=t
