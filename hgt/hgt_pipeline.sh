#!/bin/bash
threads="8"

bmge="/home/vl18625/bioinformatics/tools/BMGE-1.12/BMGE.jar"

fasta_dir="/home/vl18625/bioinformatics/diplonema/hgt/results/fasta_res/"
msa_dir="/home/vl18625/bioinformatics/diplonema/hgt/results/msa/"
trimmed_msa_dir="/home/vl18625/bioinformatics/diplonema/hgt/results/trimmed_msa/"
tree_dir="/home/vl18625/bioinformatics/diplonema/hgt/results/trees/"

infasta=""
outdir="/projects/Diplonema_genome_evolution/hgt/"

#Diamond
nr_diamond_db_path="/projects/Diplonema_genome_evolution/databases/nr/nr_diamond.dmnd"
taxonmap="/projects/Diplonema_genome_evolution/databases/nr/prot.accession2taxid.gz"
taxonnodes="/projects/Diplonema_genome_evolution/databases/nr/taxdmp/nodes.dmp"

diamond_tax_out=$outdir"tax_nr_diamond.tsv"

diamond_hgt_out=$outdir"hgt_nr_diamond.tsv"

candidates_path="/projects/Diplonema_genome_evolution/hgt/dpapi_hgt_candidates.faa"

max_hits="25"
e_cutoff="0.001"

outfmt_opts="qseqid qlen sseqid slen staxids length evalue bitscore"
diamond blastp -q $candidates_path -d $nr_diamond_db_path -o $diamond_hgt_out -p $threads --max-hsps 1 --taxonmap $taxonmap -f 6 $outfmt_opts #-evalue e_cutoff -k $max_hits tab-separated output, staxids for subject taxids


cd $fasta_dir

for fasta in *.faa
do
	msa=$msa_dir$fasta".aligned.fasta"
	trimmed_msa=$trimmed_msa_dir$fasta"trimmed_msa.fasta"
	tree="$tree_dir$fasta"
	mafft --auto --inputorder $fasta > $msa
	java -jar $bmge -i $msa -t "AA" -of $trimmed_msa
	iqtree -s $trimmed_msa -nt $threads
done


