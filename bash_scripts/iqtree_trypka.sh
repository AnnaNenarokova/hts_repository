#!/bin/bash

align_dir='/media/4TB1/blasto/trna_phylogeny/'
iqtree='/home/nenarokova/tools/iqtree-omp-1.4.3-heterotachy-Linux/bin/iqtree-omp'

f="/media/4TB1/blasto/trna_phylogeny/pastajob.marker001.trna_phylogeny_deduplicated.fna.aln"

$iqtree -s $f -m GTR+G+H4 -bb 1000 -nt 30 -pers 0.1 -nni-eval 20
