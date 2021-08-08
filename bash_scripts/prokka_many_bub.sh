#!/bin/bash
signalp_path="/home/software/signalp-5.0b/bin/"
tbl2asn_path="/home/software/tbl2asn_dir/"
barrnap_path="/home/software/barrnap/bin/"
PATH=$PATH:$signalp_path:$tbl2asn_path:$barrnap_path
prokka="/home/software/prokka/bin/prokka"


genome_dir="/mnt/data/pangenome/home_genomes/"

prokka_outdir="/mnt/data/pangenome/prokka_out/"

cd $genome_dir

for genome in *.fna
do
    #name=${genome:0:13}
    name=${genome:0:16}
    echo $name
    outdir=$prokka_outdir$name
    mkdir $outdir
    $prokka --cpus 20 --kingdom Bacteria  --gram neg --addgenes --force --centre X --compliant --outdir $outdir $genome
done
