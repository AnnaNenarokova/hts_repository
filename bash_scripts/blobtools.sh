#!/bin/bash

blob='/home/kika/tools/blobtools/blobtools'
c_in='/media/4TB1/blastocrithidia/bexlh/lhes1_PRJNA238835_trinity/Trinity.fasta'
bam='/media/4TB1/blastocrithidia/mapping/lhes1_bowtie2_RNA/lhes1_bw2_sorted.bam'
blast='/home/kika/tools/blobtools/example/blast.out'
out='/media/4TB1/blastocrithidia/bexlh/blobtools_results/'
v_in=$out'blobDB.json'

$blob create -i $c_in -b $bam -o $out -t $blast 
$blob view -i $v_in -o $out
$blob plot -i $v_in -o $out