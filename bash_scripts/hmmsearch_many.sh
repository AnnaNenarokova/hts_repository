#!/bin/bash

cog_dir="/home/anna/work/euk_local/cogs/"
prot_dir="/home/anna/work/euk_local/proteomes/"
out_dir="/home/anna/work/euk_local/hmm_results/"

cd $prot_dir

for proteome in *.fasta
do
    for cog_hmm in $cog_dir*.hmm
        do
            result=$out_dir
            hmm_name="$(basename -- $cog_hmm)"
            result=$out_dir$proteome$hmm_name".txt"
            echo $result
            hmmsearch --tblout $result $cog_hmm $proteome
        done
done

