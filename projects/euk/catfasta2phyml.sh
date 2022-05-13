#!/bin/bash
catfasta2phyml=/Users/vl18625/work/tools/catfasta2phyml/catfasta2phyml.pl
workdir="/Users/vl18625/work/euk/markers_euks/nina_markers/final_ae_sets/only_euks_files/linsi_bmge_trimal_75_to_concat/"

outfile="/Users/vl18625/work/euk/markers_euks/nina_markers/final_ae_sets/only_euks_files/ae_only_euk_linsi_bmge_trimal_75_concatenated.faa"
cd $workdir

$catfasta2phyml --concatenate --verbose -f *.faa > $outfile

