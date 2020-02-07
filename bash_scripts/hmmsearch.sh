#!/bin/bash
cpu=60

hmmsearch="/home/users/nenarokova/tools/hmmer/bin/hmmsearch"

hmm="/home/users/nenarokova/zachar/ENOG410ZRF1_scf25_eggnogdb.hmm"

subject="/home/users/nenarokova/diplonema/ref_dataset/no_dpapi_refdataset_cleaned.faa"

output_dir="/home/users/nenarokova/zachar/archaea_ref/hmm_reports/"

pfam_hits=$output_dir"all_ref_dataset_hmm_report.txt"

$hmmsearch --pfamtblout $pfam_hits --cpu $cpu $hmm $subject
