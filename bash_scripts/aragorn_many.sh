#!/bin/bash
indir="/Users/anna/work/blasto_local/genomes/trypanosomatid_genomes/TriTrypDB/"
outdir="/Users/anna/work/blasto_local/tRNA/aragorn_out/aragorn_standalone_out/fasta_tryps/"

cd $indir

for f in *
do
    echo $f
    outfile=$outdir$f"_aragorn.fasta"
    aragorn -fon -o $outfile $f
done
