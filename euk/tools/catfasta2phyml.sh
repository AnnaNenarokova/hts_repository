#!/bin/bash
catfasta2phyml=/Users/vl18625/work/tools/catfasta2phyml/catfasta2phyml.pl

workdir='/Users/vl18625/work/euk/markers_euks/nina_markers/ae/non_asgard_only/linsi_bmge_renamed/'
outfile='/Users/vl18625/work/euk/markers_euks/nina_markers/ae/non_asgard_only/34_ae_non_asgard_concat.fasta'
cd $workdir

$catfasta2phyml --concatenate --verbose -f *.faa > $outfile
