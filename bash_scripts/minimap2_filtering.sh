#!/bin/bash
#SBATCH --time=999:00:00
#SBATCH --ntasks=40
module load minimap

outdir="/home/users/Myxozoa_exchange/genome_workshop/mapping/"
reads="/home/users/Myxozoa_exchange/genome_workshop/filtering/raw_reads_min_qual_7.fq.gz"
filtered_reads="/home/users/Myxozoa_exchange/genome_workshop/filtering/reads_qual_7_filtered_carp.fq.gz"
ref="/home/users/Myxozoa_exchange/Anush/carp_pbjelly.fa"
aln=$outdir"aln.sam"


minimap2 -ax map-ont -t 40 $ref $reads | samtools fastq -n -f 4 - > $filtered_reads