#!/bin/bash
#PBS -l nodes=1:ppn=64
#PBS -o /home/nenarokova/pbs.out
#PBS -e /home/nenarokova/pbs.err

align_dir='/home/nenarokova/genomes/novymonas/pandoraea_phylogeny/all_OGs_1prot_short_no_Limno_alignment/'
raxml='/home/nenarokova/tools/raxml/raxml_sse/standard-RAxML/raxmlHPC-SSE3'

cd $align_dir

$raxml -m PROTGAMMAGTR -s test_name.phy -n test_name2.tre
