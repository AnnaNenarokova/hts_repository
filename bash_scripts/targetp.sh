#!/bin/sh
targetp='/home/kika/programs/targetp-1.1/targetp'
infile='/home/kika/MEGAsync/blasto_project/genes/c_deaminase/p57_imp_mit/p57_hits.txt'
outfile='/home/kika/MEGAsync/blasto_project/genes/c_deaminase/p57_imp_mit/p57_hits_targetp.txt'
plant='P'
non_plant='N'

$targetp -$non-plant -c $infile > $outfile
