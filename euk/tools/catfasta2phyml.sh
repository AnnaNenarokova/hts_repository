#!/bin/bash
catfasta2phyml=/Users/vl18625/work/tools/catfasta2phyml/catfasta2phyml.pl

workdir='/Users/vl18625/work/euk/markers_euks/nina_markers/abe/87_markers_29_06_23/linsi_bmge_filtered_ABaE_for_concat/'
outfile='/Users/vl18625/work/euk/markers_euks/nina_markers/abe/87_markers_29_06_23/87_markers_filtered_ABaE_concat.fasta'
cd $workdir

$catfasta2phyml --concatenate --verbose -f *.faa > $outfile
