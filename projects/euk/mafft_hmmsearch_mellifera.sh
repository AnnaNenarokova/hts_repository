#!/usr/bin/python3

hmmbuild="/scratch/nenarokova/tools/hmmer-3.3.2/bin/hmmbuild"
hmmsearch="/scratch/nenarokova/tools/hmmer-3.3.2/bin/hmmsearch"

fasta_dir="/scratch/nenarokova/euk/markers/nina_markers/mono_euk_sets/set1/faa/"
msa_dir="/scratch/nenarokova/euk/markers/nina_markers/mono_euk_sets/set1/msa/"
hmm_dir="/scratch/nenarokova/euk/markers/nina_markers/mono_euk_sets/set1/hmm/"
hmm_result_dir="/scratch/nenarokova/euk/markers/nina_markers/mono_euk_sets/set1hmm_results/"

subject_path="/scratch/nenarokova/euk/nina_prok_proteomes/all_nina_prok.faa"

cd $fasta_dir
fasta=$(ls *.fasta | sed -n ${SLURM_ARRAY_TASK_ID}p)

echo $fasta

msa=$msa_dir$fasta
hmm_file=$hmm_dir$fasta".hmm"

mafft --anysymbol $fasta > $msa
$hmmbuild $hmm_file $msa


e_threshold="0.00001"

result=$hmm_result_dir$fasta".txt"
echo $result
hmmsearch -E $e_threshold --tblout $result $cog_hmm $proteome
