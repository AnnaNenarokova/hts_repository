#!/bin/bash

input="/home/nenarokova/blasto/tRNAseq/p57_ra_polished_tRNAs_new_unaligned.fq.gz"
output="/home/nenarokova/blasto/tRNAseq/P57-cyto_trimmed_unaligned_vsearch_out.fasta"

vsearch --derep_fulllength $input --output $output --sizeout