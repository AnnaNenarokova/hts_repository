#!/bin/bash
abacas2_dir="/home/nenarokova/tools/ABACAS2/"
export PERL5LIB=$abacas2_dir:$PERL5LIB
export PATH=$abacas2_dir:$PATH

mummer="/home/nenarokova/tools/MUMmer3.23/"
PATH=$PATH:$mummer

reference="/media/4TB1/blastocrithidia/scaffolding/reference_genomes/leish/TriTrypDB-32_LmajorFriedlin_Genome.fasta"
query="/media/4TB1/blastocrithidia/jaculum/spades_assembly/scaffolds.fasta"


min_length="200"
min_ident="30"
do_blast="0"

cd /media/4TB1/blastocrithidia/scaffolding/abacas2/
$abacas2_dir"abacas2.nonparallel.sh" $reference $query $min_length $min_ident $do_blast
