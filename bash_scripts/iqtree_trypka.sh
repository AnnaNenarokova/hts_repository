#!/bin/bash

align_dir='/home/nenarokova/genomes/euglena/mterf_phylogeny/'
iqtree='/home/nenarokova/tools/iqtree-omp-1.4.3-heterotachy-Linux/bin/iqtree-omp'

f="/home/nenarokova/genomes/euglena/pastajob.marker001.OG000124.aln.trimmed.gt_0.1"

# $iqtree -s $f -m GTR+G+H4 -bb 1000 -nt 30 -pers 0.1 -nni-eval 20


$iqtree -s $f -m TEST -alrt 1000 -bb 1000 -nt 30
