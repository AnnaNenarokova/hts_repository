#!/bin/bash
catfasta2phyml=/Users/vl18625/work/tools/catfasta2phyml/catfasta2phyml.pl

workdir='/Users/vl18625/work/euk/markers_euks/nina_markers/ae/asgard_only/linsi_bmge_renamed/'
outfile='/Users/vl18625/work/euk/markers_euks/nina_markers/ae/asgard_only/34_ae_asgard_only_concat.faa'
cd $workdir

$catfasta2phyml --concatenate --verbose -f *.faa > $outfile
