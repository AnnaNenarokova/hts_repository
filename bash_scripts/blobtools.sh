#!/bin/bash

blob='/home/kika/tools/blobtools/blobtools'
c_in='/media/4TB1/blastocrithidia/bexlh/lhes1_PRJNA238835_trinity/Trinity.fasta'
bam='/media/4TB1/blastocrithidia/mapping/lhes1_bowtie2_RNA/lhes1_bw2_sorted.bam'
blast='/media/4TB1/blastocrithidia/kika_workdir/lhes1.diamond_out'
out='/media/4TB1/blastocrithidia/kika_workdir/lhes1_blobtools/'
v_in=$out'blobDB.json'

$blob create -i $c_in -b $bam -t $blast -o $out
$blob view -i $v_in -o $out
$blob plot -i $v_in -o $out