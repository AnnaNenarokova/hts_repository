#!/bin/sh

f="/home/kika/MEGAsync/blasto_project/genes/c_deaminase/p57_imp_mit/p57_hits.txt"
r="/home/kika/MEGAsync/blasto_project/genes/c_deaminase/p57_imp_mit/p57_hits_multiloc.txt"
s=animal

/usr/bin/python2.7 /home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py -fasta=$f -predictor=LowRes -origin=$s -result=$r -output=simple
