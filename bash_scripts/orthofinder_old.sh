#!/bin/bash
orthofinder="/home/nenarokova/tools/OrthoFinder-master/orthofinder/orthofinder.py"
fasta_dir="/media/4TB1/euglenozoa_references/euglenozoa_ref/"
threads="30"
python2 $orthofinder -f $fasta_dir -t $threads -S diamond
old_working_dir="/media/4TB1/euglenozoa_references/euglenozoa_ref/OrthoFinder/Results_Aug25/WorkingDirectory/"
new_fasta_dir="/media/4TB1/euglenozoa_references/editing/"
python2 $orthofinder -b $old_working_dir -f $new_fasta_dir -t $threads
