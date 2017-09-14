#!/bin/bash
trimal="/home/nenarokova/tools/trimal/source/trimal"

in="/home/nenarokova/dasha/pastajob.marker001.16S_endo_dasha.aln"

out=$in"_trimmed.phy"

$trimal -in $in -out $out -phylip -nogaps

