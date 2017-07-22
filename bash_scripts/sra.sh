#!/bin/bash
sam_dump="/home/nenarokova/tools/sratoolkit.2.8.2-1-ubuntu64/bin/sam-dump.2.8.2"
fastq_dump="/home/nenarokova/tools/sratoolkit.2.8.2-1-ubuntu64/bin/fastq-dump.2.8.2"
cd /media/4TB1/blastocrithidia/UTR_analyisis/references/

name="lpyrrhocoris"
sra_id="SRR2045882"
mkdir $name
cd $name
$sam_dump $sra_id > $name".sam"
cd ../

name="lseymouri"
sra_id="SRR2048652"
mkdir $name
cd $name
$sam_dump $sra_id > $name".sam"
cd ../

name="lseymouri"
sra_id="SRR2048652"
mkdir $name
cd $name
$fastq_dump $sra_id
cd ../
