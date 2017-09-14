#!/bin/bash

iqtree='/home/nenarokova/tools/iqtree-omp-1.4.3-heterotachy-Linux/bin/iqtree-omp'

f="pastajob.marker001.16S_endo_dasha.aln_trimmed.fasta"

# $iqtree -s $f -m TEST -alrt 1000 -bb 1000 -nt 30
$iqtree -s $f -m TEST -bb 1000 -nt 30
