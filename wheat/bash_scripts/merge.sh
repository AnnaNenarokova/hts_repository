#!/bin/bash
cd /mnt/results/nenarokova/wheat/R/sum_fastq_re/sorted
mkdir merged_alignments
for l in A B C D E F G H
do
	for n in {1..11}
	do 
		out_bam='./merged_alignments/'$l$n'.bam'
		in_bam1='./'$l$n'/new_assembly_nbs_lrr_ids.bam'
		in_bam2='./'$l'0'$n'/new_assembly_nbs_lrr_ids.bam'
		echo $out_bam
		samtools merge $out_bam $in_bam1 $in_bam2
	done
done