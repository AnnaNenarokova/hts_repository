#!/bin/bash
bbmerge="/home/software/bbmap/bbmerge-auto.sh"

trimdir='/mnt/data/metagenomic_data/reads/trimmed/'
name='K26'
fw=$trimdir$name'_adapter_trimmed_1.fq'
rv=$trimdir$name'_adapter_trimmed_2.fq'

dir_merged='/mnt/data/metagenomic_data/reads/trimmed/'
name='K26_adapter_trimmed'
merged=$dir_merged$name'_merged.fq'
unmerged_fw=$dir_merged$name'_unmerged_1.fq'
unmerged_rv=$dir_merged$name'_unmerged_2.fq'
report=$dir_merged$name'.txt'
threads=40
$bbmerge in1=$fw in2=$rv out=$merged outu1=$unmerged_fw outu2=$unmerged_rv t=$threads strict=t qtrim2=t usejni=t rem extend2=50 k=62 2> $report
