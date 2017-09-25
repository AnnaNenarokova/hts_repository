#!/bin/bash
fastq_dump="/home/nenarokova/tools/sratoolkit.2.8.2-1-ubuntu64/bin/fastq-dump.2.8.2"

$fastq_dump --defline-seq '@$sn[_$rn]/$ri' --split-files file.sra
