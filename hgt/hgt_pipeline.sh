#!/bin/bash
threads="20"

infasta=""
outdir="/projects/Diplonema_genome_evolution/hgt/results"

bmge="/home/vl18625/bioinformatics/tools/BMGE-1.12/BMGE.jar"

# creating directories
fasta_dir=$outdir"/fasta/"
msa_dir="/msa/"
trimmed_msa_dir="/trimmed_msa/"
iqtree_dir="/iqtree_files/"
tree_dir=""

rm -r $msa_dir
mkdir $msa_dir
rm -r $trimmed_msa_dir
mkdir $trimmed_msa_dir
rm -r $iqtree_dir
mkdir $iqtree_dir
rm -r $tree_dir
mkdir $tree_dir

#Diamond
# nr_diamond_db_path="/projects/Diplonema_genome_evolution/databases/nr/nr_diamond.dmnd"
# taxonmap="/projects/Diplonema_genome_evolution/databases/nr/prot.accession2taxid.gz"
# taxonnodes="/projects/Diplonema_genome_evolution/databases/nr/taxdmp/nodes.dmp"

# diamond_tax_out=$outdir"tax_nr_diamond.tsv"

# diamond_hgt_out=$outdir"hgt_nr_diamond.tsv"

# candidates_path="/projects/Diplonema_genome_evolution/hgt/dpapi_hgt_candidates.faa"

# max_hits="25"
# e_cutoff="0.001"

# outfmt_opts="qseqid qlen sseqid slen staxids length evalue bitscore"
# diamond blastp -q $candidates_path -d $nr_diamond_db_path -o $diamond_hgt_out -p $threads --max-hsps 1 --taxonmap $taxonmap -f 6 $outfmt_opts #-evalue e_cutoff -k $max_hits tab-separated output, staxids for subject taxids


cd $fasta_dir

for fasta in *.faa
do
	msa=$msa_dir$fasta".aligned.fasta"
	trimmed_msa=$trimmed_msa_dir$fasta"_trimmed_msa.fasta"
	tree="$tree_dir$fasta"
	# mafft --auto --inputorder $fasta > $msa
	# java -jar $bmge -i $msa -t "AA" -of $trimmed_msa
	# iqtree -s $trimmed_msa -nt $threads -m LG+G+F -bb 1000 -bnni
	# mv $trimmed_msa"."*
	cp $trimmed_msa".treefile" $tree_dir$fasta".tree"
	mv $trimmed_msa"."* $iqtree_dir
done

