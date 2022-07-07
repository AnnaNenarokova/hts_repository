#!/bin/bash

outdir="/Users/anna/work/euk_local/nina_markers/ABE/5_markers/faa/euk_all/"
for f in *.faa
do
 echo $f
 outfile=$outdir$f
 cat $f >> $outfile
done