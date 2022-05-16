#!/bin/bash
#SBATCH --job-name=hmmsearch
#SBATCH --output=/scratch/nenarokova/code/slurm_out/hmmsearch_%A_%a.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --array=1-119
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1GB
##SBATCH --nodes=1
## --cpu_bind=v,threads

hmmbuild="/mnt/alvarium2pool/scratch/nenarokova/tools/hmmer-3.3.2/bin/hmmbuild"
hmmsearch="/mnt/alvarium2pool/scratch/nenarokova/tools/hmmer-3.3.2/bin/hmmsearch"

fasta_dir="/scratch/nenarokova/euk/markers/bacteria/alphaproteo_markers/faa/"
msa_dir="/scratch/nenarokova/euk/markers/bacteria/alphaproteo_markers/msa/"
hmm_dir="/scratch/nenarokova/euk/markers/bacteria/alphaproteo_markers/hmm/"

subject_dir="/scratch/nenarokova/euk/proteomes/anna_set_16_05_22/"
hmm_results_dir="/scratch/nenarokova/euk/markers/be_mono_results/alpha/hmm_results/"

cd $fasta_dir
fasta=$(ls *.faa | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $fasta

msa=$msa_dir$fasta
hmm_file=$hmm_dir$fasta".hmm"

mafft --anysymbol $fasta > $msa
$hmmbuild $hmm_file $msa

e_threshold="0.00001"

cd $subject_dir
for subject in *.fasta
do
	subject_path=subject_dir$subject
	result=$hmm_results_dir$fasta$subject".txt"
	echo $result
	hmmsearch -E $e_threshold --tblout $result $hmm_file $subject_path
done