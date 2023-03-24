#!/bin/bash
raxmlng="/Users/vl18625/work/tools/raxml-ng/bin/raxml-ng"
msa="/Users/vl18625/work/euk/concat_trees/alignments/abce_94_markers_concat.fasta"
output="/Users/vl18625/work/euk/pythia_analysis/abce_94_markers_concat.txt"
pythia -r $raxmlng -t 8 -m $msa -o $output --removeDuplicates -v -b