#!/bin/bash

module add languages/anaconda3/3.7
source activate busco

indir="/user/work/vl18625/eukprot/eukprot2_proteins/"
cd $indir
fasta=$(ls *.fasta | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $fasta

fasta_path=$indir$fasta

outdir="/user/work/vl18625/eukprot/eukprot2_proteins_busco/"

cd $outdir
busco -i $fasta_path -l eukaryota_odb10 -o $fasta -m proteins -f