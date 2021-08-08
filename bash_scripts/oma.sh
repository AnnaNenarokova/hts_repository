#!/bin/bash

oma_path="/usr/local/OMA"
export PATH=$PATH:/usr/local/OMA/bin

workdir="/mnt/data/martij04/Poly_Genome_annotation/orthofinder/oma_workdir/"
cd $workdir

threads=128

oma -p
#check OutgroupSpecies := []; in parameters.drw
oma -n $threads