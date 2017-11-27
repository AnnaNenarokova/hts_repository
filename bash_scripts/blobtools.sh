#!/bin/bash

input='/home/kika/tools/blobtools/example/assembly.fna'
bam='/home/kika/tools/blobtools/example/mapping_1.bam'
blast='/home/kika/tools/blobtools/example/blast.out'
out='/home/kika/tools/blobtools/example/my_first_blobplot/'

/home/kika/tools/blobtools/blobtools create -i $input -b $bam -t $blast -o $out