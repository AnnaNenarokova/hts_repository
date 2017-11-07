#!/bin/sh

f="/home/kika/MEGAsync/blasto_project/genes/wobbling/PASTA/NSun3.fa"
r="/home/kika/MEGAsync/blasto_project/genes/wobbling/Nsun3_multiloc.txt"
s=animal

/usr/bin/python2.7 /home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py -fasta=$f -predictor=LowRes -origin=$s -result=$r -output=simple
