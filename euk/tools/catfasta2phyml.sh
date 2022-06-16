#!/bin/bash
catfasta2phyml=/Users/vl18625/work/tools/catfasta2phyml/catfasta2phyml.pl
workdir="/Users/vl18625/work/euk/markers_euks/nina_markers/be/be_mono_results/alpha/be_alpha_40/for_concat/"
outfile="/Users/vl18625/work/euk/markers_euks/nina_markers/be/be_mono_results/alpha/be_alpha_40/be_alpha_38_concat.faa"
cd $workdir

$catfasta2phyml --concatenate --verbose -f *.faa > $outfile

