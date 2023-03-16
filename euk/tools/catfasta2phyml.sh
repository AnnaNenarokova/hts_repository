#!/bin/bash
catfasta2phyml=/Users/vl18625/work/tools/catfasta2phyml/catfasta2phyml.pl

workdir='/Users/vl18625/work/euk/markers_euks/nina_markers/ae/68_final_ae_markers/faa_renamed_concat/'
outfile='/Users/vl18625/work/euk/markers_euks/nina_markers/ae/68_final_ae_markers/68_final_ae.fasta'
cd $workdir

$catfasta2phyml --concatenate --verbose -f *.faa > $outfile
