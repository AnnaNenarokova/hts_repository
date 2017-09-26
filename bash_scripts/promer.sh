#!/bin/bash
promer="/home/nenarokova/tools/MUMmer3.23/promer"
reference="/media/4TB1/blastocrithidia/scaffolding/reference_genomes/leish/TriTrypDB-32_LmajorFriedlin_Genome.fasta"
query="/media/4TB1/blastocrithidia/genome_assembly/p57_scaffolds.fa"
workdir="/media/4TB1/blastocrithidia/scaffolding/mummer/"
out=$workdir"promer_out.txt"
cd $workdir
$promer $reference $query > $out
