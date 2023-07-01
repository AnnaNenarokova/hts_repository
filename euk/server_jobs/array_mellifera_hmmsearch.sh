#!/bin/bash
#SBATCH --job-name=alpha_hmm
#SBATCH --output=/scratch/nenarokova/code/slurm_out/alpha_hmm_%A_%a.out
#SBATCH --partition=med
#SBATCH --time=7-12:00:00
#SBATCH --array=1-114
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1GB
##SBATCH --nodes=1
## --cpu_bind=v,threads

hmmsearch="/mnt/alvarium2pool/scratch/nenarokova/tools/hmmer-3.3.2/bin/hmmsearch"

subject_dir="/scratch/nenarokova/euk/proteomes/anna_eukprot3_v2_21_06_23/"
hmm_dir="/scratch/nenarokova/euk/markers/bacteria/alphaproteo_markers/hmm/"
hmm_results_dir="/scratch/nenarokova/euk/hmm_results/eukprot3_v3_21_06_23_abc/alpha/"

cd $hmm_dir
hmm_file=$(ls *.hmm | sed -n ${SLURM_ARRAY_TASK_ID}p)
hmm_path=$hmm_dir$hmm_file
echo $hmm_path

e_threshold="0.0000001"

cd $subject_dir
for subject in *.fasta
do
	subject_path=$subject_dir$subject
	result=$hmm_results_dir$subject$hmm_file".txt"
	echo $result
	$hmmsearch -E $e_threshold --tblout $result $hmm_path $subject_path
done