#!/bin/bash
bbmerge="/home/software/bbmap/bbmerge-auto.sh"

trimdir='/mnt/data/metagenomic_data/reads/trimmed/'
name='PLF1'
fw=$trimdir$name'_adapter_trimmed_1.fq.gz'
rv=$trimdir$name'_adapter_trimmed_2.fq.gz'

dir_merged='/mnt/data/metagenomic_data/reads/trimmed/'
name='PLF1_adapter_trimmed'
merged=$dir_merged$name'_merged.fq.gz'
unmerged_fw=$dir_merged$name'_unmerged_1.fq.gz'
unmerged_rv=$dir_merged$name'_unmerged_2.fq.gz'
report=$dir_merged$name'.txt'
threads=40
$bbmerge in1=$fw in2=$rv out=$merged outu1=$unmerged_fw outu2=$unmerged_rv t=$threads strict=t qtrim2=t usejni=t rem extend2=50 k=62 2> $report
