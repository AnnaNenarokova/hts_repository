#!/bin/bash
catfasta2phyml=/Users/vl18625/work/tools/catfasta2phyml/catfasta2phyml.pl
workdir="/Users/vl18625/work/euk/markers_euks/nina_markers/ae/final_ae_sets/final_ae_all_filtered/linsi_bmge_trimal_85_for_concat/"
outfile="/Users/vl18625/work/euk/markers_euks/nina_markers/ae/final_ae_sets/final_ae_all_filtered/ae_65_markers_concat.fasta"
cd $workdir

$catfasta2phyml --concatenate --verbose -f *.faa > $outfile

