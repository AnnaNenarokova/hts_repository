#!/bin/bash
#SBATCH --job-name=hmmsearch
#SBATCH --output=/scratch/nenarokova/code/slurm_out/hmmsearch_%A_%a.out
#SBATCH --partition=high
#SBATCH --time=7-12:00:00
#SBATCH --array=1-200
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=6GB
##SBATCH --nodes=1
## --cpu_bind=v,threads

hmmbuild="/mnt/alvarium2pool/scratch/nenarokova/tools/hmmer-3.3.2/bin/hmmbuild"
hmmsearch="/mnt/alvarium2pool/scratch/nenarokova/tools/hmmer-3.3.2/bin/hmmsearch"

fasta_dir="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/nina_markers/mono_euk_sets/set2/faa/"
msa_dir="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/nina_markers/mono_euk_sets/set2/msa/"
hmm_dir="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/nina_markers/mono_euk_sets/set2/hmm/"
hmm_result_dir="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/nina_markers/mono_euk_sets/set2/hmm_results/"

subject_path="/mnt/alvarium2pool/scratch/nenarokova/euk/nina_prok_proteomes/all_nina_prok.faa"

cd $fasta_dir
fasta=$(ls *.faa | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $fasta

msa=$msa_dir$fasta
hmm_file=$hmm_dir$fasta".hmm"

mafft --anysymbol $fasta > $msa
$hmmbuild $hmm_file $msa


e_threshold="0.00001"

result=$hmm_result_dir$fasta".txt"
echo $result
hmmsearch -E $e_threshold --tblout $result $hmm_file $subject_path
