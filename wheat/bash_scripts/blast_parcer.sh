#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=100:00:00
cd /home/nenarokova/wheat/new_assembly
f=`ls -1 | tail -n $PBS_ARRAYID | head -1`
/home/nenarokova/ngs/wheat/blast_parcer.py $f