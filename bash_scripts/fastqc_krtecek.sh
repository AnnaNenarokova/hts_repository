#!/bin/bash
for f in *
    do
        /home/nenarokova/tools/FastQC/fastqc $f &
    done

