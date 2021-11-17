#!/bin/sh

infile="/Users/anna/work/euk_local/Dp_190104_no_isoforms.faa"
out="Dp_190104_busco"
ref_set="eukaryota_odb10"
mode="proteins"
#--mode sets the assessment MODE: genome, proteins, transcriptome

busco -i $infile -l $ref_set -m proteins -o $out

#muliple files
genome_dir=""

cd $genome_dir

for f in *.fasta
do
    out=$f".out"
    run_BUSCO.py -i $f -l $ref_set -m proteins -o $out
done
