#!/bin/sh
targetp='/home/kika/programs/targetp-1.1/targetp'
infile='/home/kika/MEGAsync/blasto_project/reference_tryps_proteoms/importome_tritrypdb_2.fa'
outfile='/home/kika/MEGAsync/blasto_project/reference_tryps_proteoms/importome_tritrypdb_2_targetp.txt'
plant='P'
non_plant='N'

$targetp -$plant -c $infile > $outfile