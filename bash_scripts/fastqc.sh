#!/bin/bash
#PBS -l walltime=100:00:00

# fastq_dir='/mnt/results/nenarokova/wheat/L/L00000210.BC1D3RACXX.5_1/sorted/'

cd $fastq_dir
folder=`ls -1 | tail -n $PBS_ARRAYID | head -1`

fastqc='/mnt/lustre/nenarokova/FastQC/fastqc'
cd $folder
$fastqc $folder'_1.fastq'
$fastqc $folder'_2.fastq'
rm -r fastqc_reports
rm fastqc_reports.tar
mkdir fastqc_reports
mv *.zip fastqc_reports
mv *.html fastqc_reports
tar -cvf fastqc_reports.tar fastqc_reports
cd trim_out
for f in *paired_out*.fastq
do
    $fastqc $f &
done
wait

mkdir fastqc_reports
mv *.zip fastqc_reports
mv *.html fastqc_reports
tar -cvf fastqc_reports.tar fastqc_reports