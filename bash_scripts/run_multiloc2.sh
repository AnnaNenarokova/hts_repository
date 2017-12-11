#!/bin/sh

f="/home/kika/MEGAsync/blasto_project/genes/c_deaminase/tb927.10.8850/p57_aa.txt"
r="/home/kika/MEGAsync/blasto_project/genes/c_deaminase/tb927.10.8850/p57_aa_multiloc.txt"
s=animal

/usr/bin/python2.7 /home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py -fasta=$f -predictor=LowRes -origin=$s -result=$r -output=simple
