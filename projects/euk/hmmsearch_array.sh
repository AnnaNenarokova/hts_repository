#!/bin/bash
module load apps/hmmer/3.3.2
cog_hmm_dir="/user/work/vl18625/euk/ed_markers/hmm_filtered/"
prot_dir="/user/work/vl18625/euk/eukprot/proteins/"
out_dir="/user/work/vl18625/euk/ed_markers/hmm_results_all_euks/"
e_threshold="0.00001"

cd $prot_dir

proteome=$(ls *.fasta | sed -n ${SLURM_ARRAY_TASK_ID}p)

for cog_hmm in $cog_hmm_dir*.faa
    do
        hmm_name="$(basename -- $cog_hmm)"
        result=$out_dir$proteome$hmm_name".txt"
        echo $result
        hmmsearch -E $e_threshold --tblout $result $cog_hmm $proteome
    done


