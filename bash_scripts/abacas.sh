#!/bin/sh
abacas="/home/nenarokova/tools/abacas.1.3.1.pl"
cd /media/4TB1/blastocrithidia/scaffolding/medusa/
reference="leptomonas.fasta"
query="p57_scaffolds.fasta"
perl $abacas -r $reference -q $query -p promer
