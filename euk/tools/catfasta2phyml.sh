#!/bin/bash
catfasta2phyml=/Users/vl18625/work/tools/catfasta2phyml/catfasta2phyml.pl

workdir='/Users/vl18625/work/euk/markers_euks/nina_markers/abe/only_euks/euks_split_markers/linsi_bmge_renamed/'
outfile='/Users/vl18625/work/euk/markers_euks/nina_markers/abe/only_euks/euks_split_markers/only_euks_132_markers_concat.fasta'
cd $workdir

$catfasta2phyml --concatenate --verbose -f *.faa > $outfile
