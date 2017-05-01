#!/bin/bash
fasta1="/home/anna/bioinformatics/blasto/p57_trinity/de_novo/test.fasta"
fasta2="/home/anna/bioinformatics/blasto/SL_P57.fa"
outfile="/home/anna/bioinformatics/blasto/p57_trinity/de_novo/alignment_test"
water -asequence $fasta1 -bsequence $fasta2 -gapopen 10 -gapextend 0.5 -outfile $outfile
