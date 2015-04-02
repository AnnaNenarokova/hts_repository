#!/bin/bash
#PBS -l walltime=100:00:00

# fastq_dir='/home/nenarokova/wheat/R1_2/sum_fastq_re/sorted/'
# fastq_dir='/home/nenarokova/wheat/R1_2/sum_fastq_re/sorted/not_trimmed/'
# fastq_dir='/mnt/results/nenarokova/wheat/L/L00000210.BC1D3RACXX.5_1/sorted/not_trimmed/'
fastq_dir='/mnt/results/nenarokova/wheat/L/L00000210.BC1D3RACXX.5_1/sorted/'

trimc_dir='/home/nenarokova/Trimmomatic-0.33/'
# adapters=$trimc_dir'adapters/TruSeq2-PE.fa'
adapters=$trimc_dir'adapters/all_trim.fa'

trim='java -jar '$trimc_dir'trimmomatic-0.33.jar'
illumina_clip='ILLUMINACLIP:'$adapters':2:30:10'
p_out_fw='trim_out/paired_out_fw.fastq'
u_out_fw='trim_out/unpaired_out_fw.fastq'
p_out_rv='trim_out/paired_out_rv.fastq'
u_out_rv='trim_out/unpaired_out_rv.fastq'

cd $fastq_dir
folder=`ls -1 | tail -n $PBS_ARRAYID | head -1`
cd $folder
mkdir trim_out

file_fw=$folder'_1.fastq'
file_rv=$folder'_2.fastq'
   
$trim PE -phred33 $file_fw $file_rv $p_out_fw $u_out_fw $p_out_rv $u_out_rv $illumina_clip LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:30