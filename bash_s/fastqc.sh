#!/bin/bash
dir='/home/anna/bioinformatics/htses/katya/'
cd $dir
mkdir fastqc_reports

for f in *.fastq
do 
	fastqc $f &
done
wait

mv *.zip fastqc_reports
tar -cvf fastqc_reports.tar fastqc_reports
