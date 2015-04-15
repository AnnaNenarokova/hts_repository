#!/bin/bash
cd /home/anna/bioinformatics/wheat/alignments/
for f in *.sam
	do
		echo $f
		bamfile=$f'.bam'
		echo $bamfile
		samtools view -bS $f > $bamfile
		echo $bamfile
		samtools sort $bamfile $f'_sorted'
		sorted_bam=$f'_sorted.bam'
		echo $sorted_bam
		samtools index $sorted_bam $f'_sorted.bam.bai'
		echo 'Success!'
	done