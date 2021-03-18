#!/bin/bash

MMSEQS_NUM_THREADS=100

mmseqs="/home/software/mmseqs/bin/mmseqs"

fasta="/home/nenarokova/trnaseq/p57_cyto_trimmed_vsearch_out.fasta"
db="/home/nenarokova/trnaseq/mmseq_db/p57_cyto_trimmed_vsearch_out_mmseqdb"
cluster_db="/home/nenarokova/trnaseq/mmseq_db/cluster_2/p57_cyto_trimmed_vsearch_out_cluster"
cluster_rep="/home/nenarokova/trnaseq/mmseq_db/cluster_2/p57_cyto_trimmed_vsearch_out_cluster_rep"

cluster_rep_fasta="/home/nenarokova/trnaseq/mmseq_db/p57_cyto_trimmed_vsearch_out_cluster_rep.fasta"

tmp_folder="/home/nenarokova/trnaseq/tmp"

min_cov=0.1

$mmseqs createdb $fasta $db
$mmseqs cluster $db $cluster_db $tmp_folder --min-seq-id 0.9 -c $min_cov

$mmseqs createsubdb $cluster_db $db $cluster_rep

$mmseqs convert2fasta $cluster_rep $cluster_rep_fasta


clusterRes="/home/nenarokova/trnaseq/easy_cluster_vsearch/clusterRes"

$mmseqs easy-cluster $fasta $clusterRes $tmp_folder