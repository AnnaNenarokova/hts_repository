#!/bin/bash

for d in *
do
    mv $d/hiseq $d/illumina
    mv $d/miseq $d/illumina
    mv $d/illumina/raw_reads/hiseq/* $d/illumina/hiseq/
done
