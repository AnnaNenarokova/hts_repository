#!/bin/bash
dir='/home/anna/bioinformatics/htses/katya/'

for f in $dir*.fastq
do 
	fastqc $f &
done
wait

# mv *.zip fastqc_reports
# rm -r *_fastqc/
# tar -cvf fastqc_reports.tar fastqc_reports
