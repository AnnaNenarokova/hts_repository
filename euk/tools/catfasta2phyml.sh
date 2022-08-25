#!/bin/bash
catfasta2phyml=/Users/vl18625/work/tools/catfasta2phyml/catfasta2phyml.pl
workdir="/Users/anna/work/euk_local/nina_markers/singlehit_results/archaea/ae_all_filtered/euk_65_markers_all_filtered_for_concat/"
outfile="/Users/anna/work/euk_local/nina_markers/singlehit_results/archaea/ae_all_filtered/euk_65_markers_all_filtered_concat.fasta"
cd $workdir

$catfasta2phyml --concatenate --verbose -f *.faa > $outfile

