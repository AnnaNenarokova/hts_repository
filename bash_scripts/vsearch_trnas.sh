#!/bin/bash

#input="/home/nenarokova/blasto/tRNAseq/p57_ra_polished_tRNAs_new_unaligned.fq.gz"
#output="/home/nenarokova/blasto/tRNAseq/P57-cyto_trimmed_unaligned_vsearch_out.fasta"

input="/home/nenarokova/blasto/tRNAseq/tbrucei/TriTrypDB-52_TbruceiTREU927_Genome.fasta.tRNAseq_mapping_aligned.fq.gz"
output="/home/nenarokova/blasto/tRNAseq/tbrucei/tbrucei_cyto_tRNAseq_aligned_vsearch.fasta"

vsearch --derep_fulllength $input --output $output --sizeout