#!/bin/bash
#SBATCH --job-name=hmm_arch
#SBATCH --output=/scratch/nenarokova/code/slurm_out/hmm_arch_%A_%a.out
#SBATCH --partition=med
#SBATCH --time=7-12:00:00
#SBATCH --array=1-85
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1GB
##SBATCH --nodes=1
## --cpu_bind=v,threads

hmmsearch="/mnt/alvarium2pool/scratch/nenarokova/tools/hmmer-3.3.2/bin/hmmsearch"

hmm_dir="/scratch/nenarokova/euk/markers/archaea/hmm/"
subject_dir="/scratch/nenarokova/euk/proteomes/anna_eukprot3_v3_21_06_23/"
hmm_results_dir="/scratch/nenarokova/euk/hmm_results/eukprot3_v3_21_06_23_abc/archaea/"

cd $hmm_dir
hmm_file=$(ls *.hmm | sed -n ${SLURM_ARRAY_TASK_ID}p)
hmm_path=$hmm_dir$hmm_file
echo $hmm_file

e_threshold="0.0000001"

cd $subject_dir
for subject in *.fasta
do
	subject_path=$subject_dir$subject
	result=$hmm_results_dir$subject$fasta".txt"
	echo $result
	$hmmsearch -E $e_threshold --tblout $result $hmm_path $subject_path
done