#!/bin/bash
#PBS -l select=1:ncpus=1:mem=1G:NodeType=medium
#PBS -l walltime=00:30:00
#PBS -J 1-93
cd /home/nenarokova/wheat/L00000210.BC1D3RACXX.5/L00000210.BC1D3RACXX.5_1/sorted/
bt2_base=

foldername=`ls -1 inputs/ | tail -n +${PBS_ARRAY_INDEX} | head -1`
# use that file as an input to myApp
myApp < inputs/$filename
bowtie2 '--reorder', '-x' $bt2_base, '-f', '-U', unpaired, '-S', sam_file