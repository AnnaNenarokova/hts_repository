#!/bin/bash
#SBATCH --time=100:00:00
#SBATCH --mem=50G
#SBATCH -n 40
#SBATCH -N 1
#SBATCH -w node1

module load Phylobayes_MPI

dataset_path="/home/users/nenarokova/hypsa/Enterobacteriales_EVAmatrix_gblocks_concat4_rec.phy"

mpirun -np 40 pb_mpi -d $dataset_path -cat -gtr neohaem