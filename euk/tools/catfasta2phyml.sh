#!/bin/bash
catfasta2phyml=/Users/vl18625/work/tools/catfasta2phyml/catfasta2phyml.pl
workdir="/Users/vl18625/work/euk/markers_euks/nina_markers/ae/final_ae_sets/final_68ae_all_filtered/only_euks/linsi_bmge_for_concat/"
outfile="/Users/vl18625/work/euk/markers_euks/nina_markers/ae/final_ae_sets/final_68ae_all_filtered/final_68ae_only_euks_concat.fasta"
cd $workdir

$catfasta2phyml --concatenate --verbose -f *.faa > $outfile

