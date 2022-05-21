#!/bin/bash
catfasta2phyml=/Users/vl18625/work/tools/catfasta2phyml/catfasta2phyml.pl
workdir="/Users/vl18625/work/euk/markers_euks/nina_markers/final_ae_sets/linsi_bmge_filtered_species_trimal_85_for_concat/"
outfile="/Users/vl18625/work/euk/markers_euks/nina_markers/final_ae_sets/ae_70_filtered_euk_concat.fasta"
cd $workdir

$catfasta2phyml --concatenate --verbose -f *.faa > $outfile

