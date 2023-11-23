#!/bin/bash
# catfasta2phyml='/Users/vl18625/work/tools/catfasta2phyml/catfasta2phyml.pl'
catfasta2phyml='/mnt/alvarium2pool/scratch/nenarokova/tools/catfasta2phyml/catfasta2phyml.pl'
workdir='/scratch/nenarokova/euk/markers/bacteria/all_bacteria_markers/linsi_bmge_renamed/'
outfile='/scratch/nenarokova/euk/markers/bacteria/all_bacteria_markers/concat/bacteria_115_markers_concat.fasta'
cd $workdir

$catfasta2phyml --concatenate --verbose -f *.faa > $outfile
