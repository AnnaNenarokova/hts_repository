#!/bin/bash
alignment_file="/home/anna/bioinformatics/blastocrithidia/scaffolding/p57_lmajor_blast.tsv"
gap_size="100"
fragment_lengths="/home/anna/bioinformatics/blastocrithidia/scaffolding/p57_scaffolds_lengths"
output_map="/home/anna/bioinformatics/blastocrithidia/scaffolding/p57_lmajor_fragment_map"
chromosomer fragmentmap $alignment_file $gap_size $fragment_lengths $output_map
