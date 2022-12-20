#!/bin/bash
catfasta2phyml=/Users/vl18625/work/tools/catfasta2phyml/catfasta2phyml.pl

workdir='/Users/vl18625/work/euk/markers_euks/nina_markers/be/alpha/brett_data/16_markers/linsi_bmge_renamed/'
outfile='/Users/vl18625/work/euk/markers_euks/nina_markers/be/alpha/brett_data/16_markers/16_markers_brett_concat.fasta'
cd $workdir

$catfasta2phyml --concatenate --verbose -f *.faa > $outfile
