#!/bin/bash
sam_dump="/home/nenarokova/tools/sratoolkit.2.8.2-1-ubuntu64/bin/sam-dump.2.8.2"
fastq_dump="/home/nenarokova/tools/sratoolkit.2.8.2-1-ubuntu64/bin/fastq-dump.2.8.2"

cd /home/nenarokova/blasto/rna_cov_analysis/

name="tbrucei"
sra_id="ERR1413153"
$fastq_dump $sra_id

sra_id="ERR1413154"
$sam_dump $sra_id > $sra_id"_"$name".sam"

name="cfasciculata"
sra_id="SRR834693"
$fastq_dump $sra_id
