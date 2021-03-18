#!/bin/bash
aragorn="/home/anna/bioinformatics/tools/aragorn1.2.36/aragorn"
indir="/home/anna/bioinformatics/blasto_local/ciliates/genomes/"
outdir="/home/anna/bioinformatics/blasto_local/ciliates/tRNAs/aragorn_reports/"

cd $indir

for f in *
do
    echo $f
    outfile=$outdir$f"_aragorn.txt"
    $aragorn -fasta -o $outfile $f
done
