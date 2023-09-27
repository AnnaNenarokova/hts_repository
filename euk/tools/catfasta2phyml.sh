#!/bin/bash
catfasta2phyml=/Users/vl18625/work/tools/catfasta2phyml/catfasta2phyml.pl

workdir='/Users/vl18625/work/euk/markers_euks/nina_markers/ab_94_markers/no_idunn/linsi_bmge_renamed/'
outfile='/Users/vl18625/work/euk/markers_euks/nina_markers/ab_94_markers/no_idunn/ab_94_markers_no_idunn_concat.fasta'
cd $workdir

$catfasta2phyml --concatenate --verbose -f *.faa > $outfile
