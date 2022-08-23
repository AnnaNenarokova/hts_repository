#!/bin/bash
catfasta2phyml=/Users/vl18625/work/tools/catfasta2phyml/catfasta2phyml.pl
workdir="/Users/vl18625/work/euk/markers_euks/nina_markers/ae/euk_65_markers_all_filtered_for_concat/"
outfile="/Users/vl18625/work/euk/markers_euks/nina_markers/ae/euk_65_markers_all_filtered_concat.fasta"
cd $workdir

$catfasta2phyml --concatenate --verbose -f *.faa > $outfile

