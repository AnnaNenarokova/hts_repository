#!/bin/bash

alignment="/home/anna/bioinformatics/blasto/deaminases/LmjF33.1760/LmjF33.1760_aligned.faa"
name="OTT_1508-like_deaminase"
hmm="/home/anna/bioinformatics/blasto/deaminases/LmjF33.1760/LmjF33.1760.hmm"

hmmbuild -n $name $hmm $alignment


subject="/home/anna/bioinformatics/references/tritrypdb_references/tritrypdb_34/proteins/TriTrypDB-34_TbruceiTREU927_AnnotatedProteins.fasta"

pfam_hits="/home/anna/bioinformatics/blasto/deaminases/LmjF33.1760/LmjF33.1760_hits_hmmsearch.txt"

hmmsearch --pfamtblout $pfam_hits $hmm $subject
