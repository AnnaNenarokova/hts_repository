#!/bin/bash

module add languages/anaconda3/3.7
source activate busco
hmmer_dir="/user/home/vl18625/tools/hmmer-3.3.2/src/"
PATH=$PATH:$hmmer_dir

indir="/user/work/vl18625/eukprot/eukprot2_proteins/"
cd $indir
fasta=$(ls *.fasta | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $fasta

fasta_path=$indir$fasta

outdir="/user/work/vl18625/eukprot/eukprot2_proteins_busco/"

cd $outdir
busco -i $fasta_path --auto-lineage-euk -o $fasta -m proteins -f