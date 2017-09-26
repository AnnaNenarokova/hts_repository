#!/bin/bash
abacas="/home/nenarokova/tools/abacas.1.3.1.pl"
promer="/home/nenarokova/tools/MUMmer3.23/"
PATH=$PATH:$promer
reference="/media/4TB1/blastocrithidia/scaffolding/reference_genomes/leish/leptomonas_concatenated.fasta"
query="/media/4TB1/blastocrithidia/genome_assembly/p57_scaffolds.fa"
cd /media/4TB1/blastocrithidia/scaffolding

perl $abacas -r $reference -q $query -p promer -t -b
