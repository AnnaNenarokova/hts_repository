#!/bin/bash
#SBATCH --time=999:00:00
#SBATCH --ntasks=40
outdir="/home/users/Myxozoa_exchange/genome_workshop/mapping/"
reads="/home/users/Myxozoa_exchange/Anush/Smolnari_genome_raw_reads/May14_Nanopore_FG1901/FG1901_PAD09615_20190130_porechop.fastq.gz"
ref="/home/users/Myxozoa_exchange/Anush/carp_pbjelly.fa"
aln=$outdir"aln.sam"
module load minimap2

minimap2 -ax map-ont -t 40 $ref $reads > $aln