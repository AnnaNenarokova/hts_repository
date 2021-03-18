#!/bin/bash
#SBATCH --time=999:00:00
#SBATCH --ntasks=40

module load flye

flye="/home/users/nenarokova/tools/Flye/bin/flye"
outdir="/home/users/Myxozoa_exchange/genome_workshop/assembly/flye2"
reads="/home/users/Myxozoa_exchange/genome_workshop/mapping/filtered_reads_filtlong_0.1.fq.gz"
$flye --nano-raw $reads --out-dir $outdir --genome-size 40m --threads 40

flye="/home/users/nenarokova/tools/Flye/bin/flye"
outdir="/home/users/Myxozoa_exchange/genome_workshop/assembly/flye3"
reads="/home/users/Myxozoa_exchange/genome_workshop/filtering/filtered_reads_filtlong_len_10_cov_35.fq.gz"
$flye --nano-corr $reads --out-dir $outdir --genome-size 40m --threads 40

flye="/home/users/nenarokova/tools/Flye/bin/flye"
outdir="/home/users/Myxozoa_exchange/genome_workshop/assembly/flye4"
reads="/home/users/Myxozoa_exchange/genome_workshop/filtering/unmapped_reads_carp_pbjelly_all.fq.gz"
$flye --nano-raw $reads --out-dir $outdir --genome-size 40m --threads 40

flye="/home/users/nenarokova/tools/Flye/bin/flye"
outdir="/home/users/Myxozoa_exchange/genome_workshop/assembly/flye5"
reads="/home/users/Myxozoa_exchange/genome_workshop/filtering/reads_qual_7_filtered_carp.fq.gz"
$flye --nano-raw $reads --out-dir $outdir --genome-size 40m --threads 40

flye="/home/users/nenarokova/tools/Flye/bin/flye"
outdir="/home/users/Myxozoa_exchange/genome_workshop/assembly/flye_ron_nano-raw"
reads="/home/users/Myxozoa_exchange/genome_workshop/filtering/reads_qual_7_filtered_filtlong_35x_len10.fq.gz"
$flye --nano-raw $reads --out-dir $outdir --genome-size 40m --threads 40


flye="/home/users/nenarokova/tools/Flye/bin/flye"
outdir="/home/users/Myxozoa_exchange/genome_workshop/assembly/flye6"
reads="/home/users/Myxozoa_exchange/genome_workshop/filtering/qual_7_filtered_filtlong_0.3.fq.gz"
$flye --nano-raw $reads --out-dir $outdir --genome-size 40m --threads 40

flye="/home/users/nenarokova/tools/Flye/bin/flye"
outdir="/home/users/Myxozoa_exchange/genome_workshop/assembly/flye7"
reads="/home/users/Myxozoa_exchange/genome_workshop/filtering/qual_7_filtered_filtlong_0.5.fq.gz"
$flye --nano-raw $reads --out-dir $outdir --genome-size 40m --threads 40

flye="/home/users/nenarokova/tools/Flye/bin/flye"
outdir="/home/users/Myxozoa_exchange/genome_workshop/assembly/flye8"
reads="/home/users/Myxozoa_exchange/genome_workshop/filtering/qual_7_filtered_filtlong_0.4.fq.gz"
$flye --nano-raw $reads --out-dir $outdir --genome-size 40m --threads 40