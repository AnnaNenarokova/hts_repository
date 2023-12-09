#!/bin/bash
# catfasta2phyml='/Users/vl18625/work/tools/catfasta2phyml/catfasta2phyml.pl'
catfasta2phyml='/mnt/alvarium2pool/scratch/nenarokova/tools/catfasta2phyml/catfasta2phyml.pl'
workdir='/scratch/nenarokova/euk/markers/be/one_hit/01_07_23/ce_filtered/linsi_bmge_renamed/'
outfile='/scratch/nenarokova/euk/markers/be/one_hit/01_07_23/ce_filtered/concat/CE_81_markers_concat.fasta'
cd $workdir

$catfasta2phyml --concatenate --verbose -f *.faa > $outfile
