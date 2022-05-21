#!/bin/bash

fasta="/Users/anna/work/blasto_local/tRNA/tRNAseq/p57_Trp_aligned_clusters.fasta"
aligned="/Users/anna/work/blasto_local/tRNA/tRNAseq/p57_Trp_aligned_clusters_aligned.fasta"

mafft --localpair --op 10 --ep 0 --maxiterate 1000 $fasta > $aligned
