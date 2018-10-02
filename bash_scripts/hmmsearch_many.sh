#!/bin/bash

hmm_folder="/home/anna/bioinformatics/euglena/ND_hmm/ncbi_tryps/"
hmmsearch="/home/anna/bioinformatics/tools/hmmer-3.1b2-linux-intel-x86_64/binaries/hmmsearch"
cd $hmm_folder

subject1="/home/anna/bioinformatics/euglena/Egra_Neill_homologs_aa.fa"
subject2="/home/anna/bioinformatics/euglena/Egra_Yosh_homologs_aa.fa"

output_dir="/home/anna/bioinformatics/euglena/ND_hmm/hmm_reports/"

for hmm in *.hmm
do
    echo $hmm
    pfam_hits1=$output_dir"Neill"$hmm
    pfam_hits2=$output_dir"Yoshida"$hmm
    $hmmsearch --pfamtblout $pfam_hits1 $hmm $subject1
    $hmmsearch --pfamtblout $pfam_hits2 $hmm $subject2
done

