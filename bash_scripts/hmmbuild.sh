#!/bin/bash
folder="/media/anna/data/anna_drive/projects/mitoproteomes/euglena/euglena_mitoproteome/NADH/hmm_searches/"

alignment="/media/anna/data/anna_drive/projects/mitoproteomes/euglena/euglena_mitoproteome/NADH/hmm_searches/atp6_tryp.aln"
name="atp6_tryp"

outfile=$folder$name".hmm"
/home/anna/bioinformatics/tools/hmmer-3.1b2-linux-intel-x86_64/binaries/hmmbuild -n $name $outfile $alignment
