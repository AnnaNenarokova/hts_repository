#!/bin/bash

cog_dir="/Users/anna/work/euk_local/ed_markers_untrimmed/"
prot_dir="/Users/anna/work/euk_local/eukprot_proteomes/"
out_dir="/Users/anna/work/euk_local/hmm_results_ed_cogs/"

cd $prot_dir
e_threshold="1"

mkdir $out_dir

for proteome in *.fasta
do
    for cog_hmm in $cog_dir*.hmm
        do
            result=$out_dir
            hmm_name="$(basename -- $cog_hmm)"
            result=$out_dir$proteome$hmm_name".txt"
            echo $result
            hmmsearch -E $e_threshold --tblout $result $cog_hmm $proteome
        done
done

