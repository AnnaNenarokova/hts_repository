#!/bin/bash
#SBATCH --time=999:00:00

#SBATCH --ntasks=40
module load MMseqs2

MMSEQS_NUM_THREADS=40

fasta="/home/users/nenarokova/blasto/tRNAseq/p57_cyto_trimmed_vsearch_out.fasta"
db="/home/users/nenarokova/blasto/tRNAseq/p57_cyto_trimmed_vsearch_out_mmseqdb"
cluster_db="/home/users/nenarokova/blasto/tRNAseq/p57_cyto_trimmed_vsearch_out_mmseqdb_cluster"
cluster_out="/home/users/nenarokova/blasto/tRNAseq/p57_cyto_trimmed_vsearch_out_mmseqdb_cluster_out"
cluster_rep="/home/users/nenarokova/blasto/tRNAseq/p57_cyto_trimmed_vsearch_out_mmseqdb_cluster_rep"
tmp_folder="/home/users/nenarokova/blasto/tRNAseq/tmp"

min_cov=0.1

mmseqs createdb $fasta $db
mmseqs cluster $db $cluster_db $tmp_folder
mmseqs createsubdb $cluster_db $db $cluster_rep