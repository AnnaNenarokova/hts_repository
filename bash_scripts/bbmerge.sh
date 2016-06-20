#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=60

folder='/home/nenarokova/kinetoplastids/illumina/miseq/raw_reads/'

fw=$folder'18098_1_7_1.fastq.gz'
rv=$folder'18098_1_7_2.fastq.gz'
merged='/home/nenarokova/kinetoplastids/illumina/miseq/merged_reads/18098_1_7_merged.fq'
unmerged_fw='/home/nenarokova/kinetoplastids/illumina/illumina/miseq/merged_reads/18098_1_7_unmerged_fw.fq'
unmerged_rv='/home/nenarokova/kinetoplastids/illumina/illumina/miseq/merged_reads/18098_1_7_unmerged_rv.fq'
/home/nenarokova/tools/bbmap/bbmerge.sh in1=$fw in2=$rv out=$merged outu1=$unmerged_fw outu2=$unmerged_rv strict=t qtrim2=t usejni=t

fw=$folder'18021_1_7_1.fastq.gz'
rv=$folder'18021_1_7_2.fastq.gz'
merged='/home/nenarokova/kinetoplastids/illumina/miseq/merged_reads/18021_1_7_merged.fq'
unmerged_fw='/home/nenarokova/kinetoplastids/illumina/illumina/miseq/merged_reads/18021_1_7_unmerged_fw.fq'
unmerged_rv='/home/nenarokova/kinetoplastids/illumina/illumina/miseq/merged_reads/18021_1_7_unmerged_rv.fq'
/home/nenarokova/tools/bbmap/bbmerge.sh in1=$fw in2=$rv out=$merged outu1=$unmerged_fw outu2=$unmerged_rv strict=t qtrim2=t usejni=t
