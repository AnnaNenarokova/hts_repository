#!/bin/bash
signalp_path="/home/software/signalp-5.0b/bin/"
tbl2asn_path="/home/software/tbl2asn_dir/"
barrnap_path="/home/software/barrnap/bin/"
PATH=$PATH:$signalp_path:$tbl2asn_path:$barrnap_path
prokka="/home/software/prokka/bin/prokka"


genome_dir="/mnt/data/pangenome/genomes_ncbi/ncbi-genomes-2021-03-25/"
prokka_outdir="/mnt/data/pangenome/genomes_ncbi/prokka_out/"

cd $genome_dir

for genome in *.fna
do
    name=${genome:0:12}
    echo $name
    outdir=$prokka_outdir$name
    #mkdir $outdir
    $prokka --cpus 20 --kingdom Bacteria  --gram neg --addgenes --force --outdir $outdir $genome
done
