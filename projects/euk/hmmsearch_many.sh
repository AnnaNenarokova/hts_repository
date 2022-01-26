#!/bin/bash

cog_hmm_dir="/Users/anna/work/euk_local/ed/ed_markers/hmm_filtered/"
prot_dir="/Users/anna/work/euk_local/uniprot_proteomes/renamed_fastas/"
out_dir="/Users/anna/work/euk_local/ed/ed_markers/hmm_results_filt/"

cd $prot_dir
e_threshold="0.0001"

mkdir $out_dir

for proteome in *.fasta
do
    for cog_hmm in $cog_hmm_dir*.hmm
        do
            result=$out_dir
            hmm_name="$(basename -- $cog_hmm)"
            result=$out_dir$proteome$hmm_name".txt"
            echo $result
            hmmsearch -E $e_threshold --tblout $result $cog_hmm $proteome
        done
done

