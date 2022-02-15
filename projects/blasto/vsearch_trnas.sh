#!/bin/bash


input="/home/nenarokova/blasto/tRNAseq/blasto/new_tRNA_ill_p57_aligned.fq"
output="/home/nenarokova/blasto/tRNAseq/blasto/corrected_assembly_tRNA_vsearch_clusters.fasta"

vsearch --derep_fulllength $input --output $output --sizeout