#!/bin/bash

## Change the paths and the query name, don't forget / at the the end of the directory path ##
ref_db_dir="/mnt/data/metagenomic_data/ref_blast/ref_db"
contigs_path="/mnt/data/vacatko/data/SRA/spadesSRR8334265/contigs.fasta"
query_name="SRR8334265"
outfile=$contigs_path"_info.tsv"

########

threads=120
python_script="/mnt/data/metagenomic_data/scrpits/analyse_metaspades_contigs_standalone.py"

## Diamond blast settings##
blast_outdir="/mnt/data/metagenomic_data/ref_blast/diamond_blast_results/"$query_name"/"
mkdir $blast_outdir

temp_dir=$blast_outdir"temp"
mkdir $temp_dir

custom_db_outdir=$blast_outdir"custom_db_outdir/"
mkdir $custom_db_outdir

custom_outfmt="6 qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send"

## Taxonomy Diamond blast ##
query=$contigs_path
tax_dmnd_out=$blast_outdir$query_name"_nr_tax_dmnd.tsv"

db_path="/mnt/data/databases/nr_tax.dmnd"
taxonmap="/mnt/data/databases/prot.accession2taxid.gz"
taxonnodes="/mnt/data/databases/taxdump/nodes.dmp"

diamond blastx -q $query -d $db_path -o $tax_dmnd_out -p $threads --taxonmap $taxonmap --taxonnodes $taxonnodes -b12 -c1 -f 102 -t $temp_dir

####

cd $ref_db_dir
for fasta in *.faa
    do
        db_path=$fasta".dmnd"
        diamond makedb --in $fasta --db $db_path --threads $threads -t $temp_dir
    done

for db in *.dmnd
    do 
        dmnd_outfile=$custom_db_outdir$db".tsv"
        diamond blastx -q $contigs_path -d $db -o $dmnd_outfile -f $custom_outfmt -p $threads -b12 -c1 -t $temp_dir
    done

python3 $python_script $contigs_path $outfile $tax_dmnd_out $custom_db_outdir
