#!/bin/bash

iqtree='/home/nenarokova/tools/iqtree-omp-1.4.3-heterotachy-Linux/bin/iqtree-omp'

f="/home/users/nenarokova/zachar/scf25_dataset/pasta/pastajob.marker001.scf25_dataset.faa.aln"

# $iqtree -s $f -m TEST -alrt 1000 -bb 1000 -nt 30
$iqtree -s $f -m TEST -bb 1000 -nt 30
