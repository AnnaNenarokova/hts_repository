#!/bin/bash

for f in *.fastq
    do
        /home/nenarokova/tools/FastQC/fastqc $f &
    done

for f in */illumina/trimmed_reads/*.fastq
    do
        /home/nenarokova/tools/FastQC/fastqc $f &
    done

for f in *.fastq.tar.gz
    do
        tar -xzf $f &
    done

for f in *.fastq.gz
    do
        gzip -d $f &
    done
