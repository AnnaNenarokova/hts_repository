#!/bin/sh

# infile="/home/anna/bioinformatics/diplonema/proteins_SL_Loc+PFAM+BLASTP_trim_newIDs.faa"
# out="dpapillatum_transcriptome"
ref_set="/home/anna/bioinformatics/tools/BUSCO/busco_lineages/eukaryota_odb9"
mode="proteins"
#--mode sets the assessment MODE: genome, proteins, transcriptome

#run_BUSCO.py -i $infile -l $ref_set -m proteins -o $out

#muliple files
genome_dir=""

cd $genome_dir

for f in *.fasta
do
    out=$f".out"
    run_BUSCO.py -i $f -l $ref_set -m proteins -o $out
done
