#!/bin/bash
catfasta2phyml=/Users/vl18625/work/tools/catfasta2phyml/catfasta2phyml.pl

workdir='/Users/vl18625/work/euk/markers_euks/nina_markers/abe/104_species/renamed_to_concat/'
outfile='/Users/vl18625/work/euk/markers_euks/nina_markers/abe/104_species/104_species_abce_concat.fasta'
cd $workdir

$catfasta2phyml --concatenate --verbose -f *.faa > $outfile
