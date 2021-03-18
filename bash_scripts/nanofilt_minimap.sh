#!/bin/bash
module load minimap

min_qual=7
reads="/home/users/Myxozoa_exchange/Anush/Smolnari_genome_raw_reads/May14_Nanopore_FG1901/FG1901_PAD09615_20190130_porechop.fastq.gz"
ref="/home/users/Myxozoa_exchange/Anush/carp_pbjelly.fa"

outdir="/home/users/Myxozoa_exchange/genome_workshop/filtering/"
logfile="/home/users/Myxozoa_exchange/genome_workshop/filtering/nanofilt.log"
aln=$outdir"carp_pbjelly_q_7.paf"

gunzip -c $reads | NanoFilt -q $min_qual --logfile $logfile| minimap2 -ax map-ont -t 40 $ref > $aln