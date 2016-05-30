#!/bin/bash
#PBS -d .

files = "/home/nenarokova/contaminants/trimmed_reads/*.fastq"
i = 0
for f in $files
do
    if [ i == $PBS_ARRAYID ]; then
        echo 'WOW'
    fi
    echo $f
    echo $PBS_ARRAYID
done
