#!/bin/bash

align_dir='/media/4TB1/blasto/trna_phylogeny/'
raxml='/home/nenarokova/tools/standard-RAxML/raxmlHPC'

cd $align_dir

f="pastajob.marker001.trna_phylogeny_deduplicated.phy"

$raxml -f a -x $RANDOM -p $RANDOM -m GTRGAMMA -# autoMRE -s $f -n $f"2.tre" > $f"raxml_out.txt"
