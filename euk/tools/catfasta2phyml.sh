#!/bin/bash
# catfasta2phyml='/Users/vl18625/work/tools/catfasta2phyml/catfasta2phyml.pl'
catfasta2phyml='/mnt/alvarium2pool/scratch/nenarokova/tools/catfasta2phyml/catfasta2phyml.pl'
workdir='/scratch/nenarokova/euk/markers/ae/one_hit/ae_81_markers_11_03_24_all/ae_no_meta_81_markers_11_03_24/linsi_bmge_renamed/'
outfile='/scratch/nenarokova/euk/markers/ae/one_hit/ae_81_markers_11_03_24_all/ae_no_meta_81_markers_11_03_24/concat/ae_81_markers_no_meta.fasta'
cd $workdir

$catfasta2phyml --concatenate --verbose -f *.faa > $outfile
