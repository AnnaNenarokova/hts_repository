#!/bin/bash
align_dir = '/home/nenarokova/genomes/novymonas/pandoraea_phylogeny/all_OGs_1prot_short_no_Limno_alignment/'
raxml='/home/nenarokova/tools/raxml/standard-RAxML/raxmlHPC'


$raxml -f o -m GTRGAMMA -#1 -s $infile -n $outfile

­$raxml -f c -m PROTGAMMAAUTO -s $infile -n $outfile

/home/nenarokova/tools/raxml/standard-RAxML/raxmlHPC -m PROTGAMMAGTR -s $infile -n $outfile

/home/nenarokova/tools/raxml/standard-RAxML/raxmlHPC -m PROTGAMMAGTR -s test_name.phy -n test_name.tre

