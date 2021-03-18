#!/bin/bash
#SBATCH --time=999:00:00
#SBATCH --ntasks=40

filtlong="/home/users/nenarokova/tools/Filtlong/bin/filtlong"


nanopore_reads="/home/users/Myxozoa_exchange/genome_workshop/mapping/unmapped_reads_carp_pbjelly.fq.gz"
target_bases=1414000000
output="/home/users/Myxozoa_exchange/genome_workshop/mapping/filtered_reads_filtlong.fq.gz"
$filtlong --target_bases $target_bases --length_weight $length_weight $nanopore_reads | gzip > $output

nanopore_reads="/home/users/Myxozoa_exchange/genome_workshop/mapping/unmapped_reads_carp_pbjelly.fq.gz"
output="/home/users/Myxozoa_exchange/genome_workshop/mapping/filtered_reads_filtlong_0.1.fq.gz"
$filtlong --min_length 1000 --keep_percent 10 $nanopore_reads | gzip > $output


nanopore_reads="/home/users/Myxozoa_exchange/genome_workshop/filtering/reads_qual_7_filtered_carp.fq"
output="/home/users/Myxozoa_exchange/genome_workshop/filtering/reads_qual_7_filtered_filtlong_35x_len10.fq.gz"
target_bases=1414000000
length_weight=10

$filtlong --target_bases $target_bases --length_weight $length_weight $nanopore_reads | gzip > $output


nanopore_reads="/home/users/Myxozoa_exchange/genome_workshop/filtering/reads_qual_7_filtered_carp.fq.gz"
output="/home/users/Myxozoa_exchange/genome_workshop/filtering/qual_7_filtered_filtlong_0.3.fq.gz"
$filtlong --min_length 1000 --keep_percent 30 $nanopore_reads | gzip > $output

nanopore_reads="/home/users/Myxozoa_exchange/genome_workshop/filtering/reads_qual_7_filtered_carp.fq.gz"
output="/home/users/Myxozoa_exchange/genome_workshop/filtering/qual_7_filtered_filtlong_0.5.fq.gz"
$filtlong --min_length 1000 --keep_percent 50 $nanopore_reads | gzip > $output

nanopore_reads="/home/users/Myxozoa_exchange/genome_workshop/filtering/reads_qual_7_filtered_carp.fq.gz"
output="/home/users/Myxozoa_exchange/genome_workshop/filtering/qual_7_filtered_filtlong_0.4.fq.gz"
$filtlong --min_length 1000 --keep_percent 40 $nanopore_reads | gzip > $output