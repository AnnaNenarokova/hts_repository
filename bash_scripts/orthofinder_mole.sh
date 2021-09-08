#!/bin/bash
#SBATCH --time=999:00:00
#SBATCH -N 1 --ntasks-per-node=40
module load OrthoFinder

fasta_dir="/home/users/Myxozoa_exchange/orthofinder_anna/proteome_dataset/"
outdir="/home/users/Myxozoa_exchange/orthofinder_anna/orthofinder/"
threads="40"

orthofinder -f $fasta_dir -t $threads -o $outdir -S diamond
