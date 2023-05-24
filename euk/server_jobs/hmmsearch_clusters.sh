#!/bin/bash
#SBATCH --job-name=hmmsearch_clusters
#SBATCH --output=/scratch/nenarokova/code/slurm_out/hmmsearch/hmmsearch_clusters_%A_%a.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --array=1-115
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1GB
##SBATCH --nodes=1
## --cpu_bind=v,threads


e_threshold="0.00001"
hmmsearch="/mnt/alvarium2pool/scratch/nenarokova/tools/hmmer-3.3.2/bin/hmmsearch"
hmmfile="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/hmm_results/euk_hmm_clusters_nina/Euk_broccoli_clusters_v1.hmm"
hmm_results_dir="/scratch/nenarokova/euk/markers/hmm_results/euk_hmm_clusters_nina/hmm_results/"
subject_dir="/scratch/nenarokova/euk/proteomes/anna_eukprot3_set_v2_21_03_23/"

cd $subject_dir
subject=$(ls *.faa | sed -n ${SLURM_ARRAY_TASK_ID}p)

subject_path=$subject_dir$subject
result=$hmm_results_dir$subject$fasta".txt"
echo $result
hmmsearch -E $e_threshold --tblout $result $hmm_file $subject_path
