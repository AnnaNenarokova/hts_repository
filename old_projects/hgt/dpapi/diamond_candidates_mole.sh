#!/bin/bash
#SBATCH --time=999:00:00
#SBATCH --ntasks=120
#SBATCH -N 1
module load diamond2
threads="80"
nr_db_path="/home/users/nenarokova/dbs/nr_tax.dmnd"
taxonmap="/home/users/nenarokova/dbs/prot.accession2taxid.gz"
refdb_path="/home/users/nenarokova/diplonema/ref_dataset/dpapi_full_dataset.dmnd"

candidates_path="/home/users/nenarokova/diplonema/hgt/dpapi_recoded_hgt_cands.faa"

diamond_nr_out="/home/users/nenarokova/diplonema/hgt/diamond_results/dpapi_recoded_cand_nr_dmnd_tax_50.tsv"
outfmt_nr_opts="qseqid qlen sseqid slen staxids length evalue bitscore"

diamond_refset_out="/home/users/nenarokova/diplonema/hgt/diamond_results/dpapi_recoded_cand_refset_dmnd.tsv"

diamond blastp -q $candidates_path -d $nr_db_path -o $diamond_nr_out -p $threads --max-target-seqs 50 --max-hsps 1 --taxonmap $taxonmap -f 6 $outfmt_nr_opts -b12 -c1 #-evalue e_cutoff -k $max_hits -f 6 tab-separated output, staxids for subject taxids

diamond blastp -q $candidates_path -d $refdb_path -o $diamond_refset_out -p $threads --max-target-seqs 0 --max-hsps 1 -f 6 -b12 -c1 #-evalue e_cutoff -k $max_hits -f 6 tab-separated output, staxids for subject taxids