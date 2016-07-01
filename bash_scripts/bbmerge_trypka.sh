#!/bin/bash

folder='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/raw_reads/'

fw=$folder'18098_1_1_1.fastq.gz'
rv=$folder'18098_1_1_2.fastq.gz'
merged='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/merged_reads/reads/18098_1_1_merged.fq'
unmerged_fw='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/merged_reads/reads/18098_1_1_unmerged_fw.fq'
unmerged_rv='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/merged_reads/reads/18098_1_1_unmerged_rv.fq'
/home/nenarokova/tools/bbmap/bbmerge.sh in1=$fw in2=$rv out=$merged outu1=$unmerged_fw outu2=$unmerged_rv strict=t qtrim2=t usejni=t

fw=$folder'18021_1_1_1.fastq.gz'
rv=$folder'18021_1_1_2.fastq.gz'
merged='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/merged_reads/reads/18021_1_1_merged.fq'
unmerged_fw='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/merged_reads/reads/18021_1_1_unmerged_fw.fq'
unmerged_rv='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/merged_reads/reads/18021_1_1_unmerged_rv.fq'
/home/nenarokova/tools/bbmap/bbmerge.sh in1=$fw in2=$rv out=$merged outu1=$unmerged_fw outu2=$unmerged_rv strict=t qtrim2=t usejni=t
