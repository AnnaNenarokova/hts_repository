#!/bin/bash

module add languages/anaconda3/3.7
source activate busco

cd
outdir="/user/work/vl18625/eukprot/eukprot2_proteins_busco/"
cd $indir

fasta=$(ls *.fasta | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $fasta

busco -i $fasta -l eukaryota_odb10 -o $outdir -m proteins