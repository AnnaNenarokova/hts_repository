#!/bin/bash
#SBATCH --time=999:00:00
#SBATCH --ntasks=1

f="/home/users/nenarokova/blasto/tRNA_tree/all_tryp_tRNAs_bnonstop_linsi_0.fasta"

iqtree -s $f -m TEST -bb 1000