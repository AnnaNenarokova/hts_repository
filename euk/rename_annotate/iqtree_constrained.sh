#SBATCH --job-name=ae_constrained_lgg
#SBATCH --output=/scratch/nenarokova/code/slurm_out/ae_constrained_lgg_%A.out
#SBATCH --partition=high
#SBATCH --time=99-12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=50G

msa="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ae/one_hit/final_68ae_filtered_concat/constraint_heimdall_lgg/68_final_ae.fasta"
constraint_tree="/mnt/alvarium2pool/scratch/nenarokova/euk/markers/ae/one_hit/final_68ae_filtered_concat/constraint_heimdall_lgg/ae_constrained_heimdall_euk.tree"

iqtree -s $msa -m LG+G -g $constraint_tree -T 10