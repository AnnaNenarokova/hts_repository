#!/bin/bash

out_dir="/home/users/nenarokova/zachar/archaea_ref/hmm_reports/proteomes/"

prot_dir="/home/users/nenarokova/zachar/archaea_ref/proteomes"

cd $ref_folder

for ref in *.fsa_aa
do
    pfam_hits=$output_dir$ref".hmm"
    hmmsearch $result $hmm_db $fasta
done

