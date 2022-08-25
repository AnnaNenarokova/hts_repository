#!/bin/bash
catfasta2phyml=/Users/vl18625/work/tools/catfasta2phyml/catfasta2phyml.pl

workdir="/Users/vl18625/work/euk/markers_euks/nina_markers/be/be_c20/after_filtering/renamed_for_concat/"
outfile="/Users/vl18625/work/euk/markers_euks/nina_markers/be/be_c20/after_filtering/be_c20_filtered_58_markers_concat.fasta"

$catfasta2phyml --concatenate --verbose -f *.faa > $outfile
