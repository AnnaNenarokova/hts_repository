#!/bin/sh

f="/home/kika/scripts/euglena_prediction/input.txt"
r="/home/kika/scripts/euglena_prediction/ml2.txt"
s=animal

/usr/bin/python2.7 /home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py -fasta=$f -predictor=LowRes -origin=$s -result=$r -output=simple