#!/bin/bash
minvar_dir="/Users/vl18625/work/tools/MinVar-Rooting/"
PATH=$PATH:$minvar_dir

workdir="/Users/vl18625/work/euk/3_year_project/minvar_test/"
input_tree_dir="/Users/vl18625/work/euk/3_year_project/minvar_test/unrooted_trees/"
output_tree_dir="/Users/vl18625/work/euk/3_year_project/minvar_test/rooted_trees/"
output_log_dir="/Users/vl18625/work/euk/3_year_project/minvar_test/minvar_logs/"

cd $input_tree_dir

for tree_file in *.nwk
do
    echo $tree_file
    input_tree_path=$input_tree_dir$tree_file
    output_tree_path=$output_tree_dir$tree_file
    output_log_path=$output_log_dir$tree_file".log"
    python3 FastRoot.py -i $input_tree_path -o $output_tree_path 2> $output_log_path
done

