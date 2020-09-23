#!/bin/bash
#SBATCH --time=999:00:00
#SBATCH --ntasks=1
module load samtools

aln="/home/users/Myxozoa_exchange/genome_workshop/mapping/carp_aln.sam"
unmapped="/home/users/Myxozoa_exchange/genome_workshop/mapping/unmapped_reads.fq"

samtools view -f 4 $aln | samtools fastq > $unmapped