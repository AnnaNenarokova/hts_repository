#!/bin/bash

hmmsearch="/home/users/nenarokova/tools/hmmer/bin/hmmsearch"

hmm="/home/users/nenarokova/zachar/ENOG410ZRF1_scf25_eggnogdb.hmm"

output_dir="/home/users/nenarokova/zachar/archaea_ref/hmm_reports/proteomes/"

ref_folder="/home/users/nenarokova/zachar/archaea_ref/proteomes"

cd $ref_folder

for ref in *.fsa_aa
do
    pfam_hits=$output_dir$ref".hmm"
    $hmmsearch --pfamtblout $pfam_hits $hmm $ref
done

