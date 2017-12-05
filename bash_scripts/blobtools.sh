#!/bin/bash

blob='/home/kika/tools/blobtools/blobtools'
fasta='/media/4TB1/blastocrithidia/bexlh/lhes1_PRJNA238835_trinity/Trinity.fasta'
bam='/media/4TB1/blastocrithidia/mapping/lhes1_bowtie2_RNA/lhes1_bw2_sorted.bam'
blast='/media/4TB1/blastocrithidia/kika_workdir/lhes1_new.diamond_out'
out='/media/4TB1/blastocrithidia/kika_workdir/lhes1_new/'
input=$out'blobDB.json'

$blob create -i $fasta -b $bam -t $blast -o $out
$blob view -i $input -o $out
$blob plot -i $input -o $out