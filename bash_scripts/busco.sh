#!/bin/sh

infile="/home/anna/bioinformatics/diplonema/Tbor_RNAseq_cd_hit_est_latest_transdecoder.fa"
out="tbor"
ref_set="/home/anna/bioinformatics/tools/BUSCO/busco_lineages/eukaryota_odb9"
mode="proteins"
#--mode sets the assessment MODE: genome, proteins, transcriptome

run_BUSCO.py -i $infile -l $ref_set -m proteins -o $out
