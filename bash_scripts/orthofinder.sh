#!/bin/bash
orthofinder="/home/software/OrthoFinder/orthofinder"
fasta_dir="/mnt/data/martij04/Poly_Genome_annotation/orthofinder/polyplax_ref_proteomes/"
outdir="/mnt/data/martij04/Poly_Genome_annotation/orthofinder/orthofinder_out/"
threads="128"
$orthofinder -f $fasta_dir -t $threads -o $outdir -S diamond
