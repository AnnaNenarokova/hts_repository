#!/bin/bash
catfasta2phyml=/Users/vl18625/work/tools/catfasta2phyml/catfasta2phyml.pl
workdir="/Users/vl18625/work/euk/markers_euks/nina_markers/final_ae_sets/msa_bmge_for_concat/"

outfile="/Users/vl18625/work/euk/markers_euks/nina_markers/final_ae_sets/ae_set_70_concatenated.faa"
cd $workdir

$catfasta2phyml --concatenate --verbose -f *.faa > $outfile

