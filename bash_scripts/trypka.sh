#!/bin/bash

for f in *
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

for d1 in hiseq miseq
    do
    for d2 in raw_reads trimmed_reads
        do
        for f in $d1/$d2/*.fastq
            do
            echo "Processing $f"
            /home/nenarokova/tools/FastQC/fastqc $f &
            done
        done
    done

    for d2 in raw_reads trimmed_reads
        do
        for f in $d2/*.fastq
            do
            echo "Processing $f"
            /home/nenarokova/tools/FastQC/fastqc $f &
            done
        done
