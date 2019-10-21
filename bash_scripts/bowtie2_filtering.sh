#!/bin/bash
threads=32
fasta="/media/4TB1/blastocrithidia/mapping/tRNA_to_rRNA/rRNA_reference.fa"

bt2_base="/media/4TB1/blastocrithidia/mapping/tRNA_to_rRNA/rRNA_reference.fa.bw2"

bowtie2-build --threads $threads $fasta $bt2_base

file_path="/media/4TB1/blastocrithidia/mapping/tRNA_to_rRNA/p57_tRNA_trimmed_not_aligned_to_rRNA"
r1="/media/4TB1/blastocrithidia/mapping/tRNA_to_rRNA/p57_tRNA_trimmed_not_aligned.fq.1.gz"
r2="/media/4TB1/blastocrithidia/mapping/tRNA_to_rRNA/p57_tRNA_trimmed_not_aligned.fq.2.gz"
unaligned="/media/4TB1/blastocrithidia/mapping/tRNA_to_rRNA/p57_tRNA_trimmed_not_aligned_to_rRNA_ref.fq.gz"

alignment=$file_path".sam"
report=$file_path".txt"

bowtie2 --very-sensitive -p $threads -x $bt2_base -1 $r1 -2 $r2 --un-conc-gz $unaligned -S $alignment 2> $report
