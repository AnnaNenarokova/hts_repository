#!/bin/bash

input='/home/kika/tools/blobtools/example/assembly.fna'
bam='/home/kika/tools/blobtools/example/mapping_1.bam'
blast='/home/kika/tools/blobtools/example/blast.out'
out='/home/kika/tools/blobtools/example/my_first_blobplot/'

# /home/kika/tools/blobtools/blobtools create -i $input -b $bam -o $out
# -t $blast 

v_in=$out+'blobDB.json'
/home/kika/tools/blobtools/blobtools view -i $v_in -o $out