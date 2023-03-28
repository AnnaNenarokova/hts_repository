#!/bin/bash
raxmlng="/Users/vl18625/work/tools/raxml-ng/bin/raxml-ng"
msa="/Users/vl18625/work/euk/markers_euks/nina_markers/ae/asgard_only/34_ae_asgard_only_concat.faa"
output="/Users/vl18625/work/euk/pythia_analysis/34_ae_asgard_only_concat.txt"
pythia -r $raxmlng -t 8 -m $msa --removeDuplicates -v -b 2> $output