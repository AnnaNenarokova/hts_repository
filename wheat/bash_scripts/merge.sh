#!/bin/bash
cd /mnt/results/nenarokova/wheat/R/sum_fastq_re/sorted
mkdir merged_alignments
letters=( A B C D E F G H )
for l in letters
do
	for n in {1..5}
	do 
		out_bam='./merged_alignments/'$l$n'.bam'
		in1_bam='./'$l$n'new_assembly_nbs_lrr_ids.bam'
		in2_bam='./'$l'0'$n'new_assembly_nbs_lrr_ids.bam'
		echo $out_bam
		echo $in_bam1
		echo $in_bam2
		ls $out_bam
		ls $in_bam1
		ls $in_bam2
		# samtools merge $out_bam $in_bam1 $in_bam2
	done
done