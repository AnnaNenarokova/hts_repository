#!/bin/sh

f="/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Fd+FNR/Sulfite_reductase/EL+EG_SiR.txt"
r="/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Fd+FNR/Sulfite_reductase/EL+EG_SiR_multiloc.txt"

/usr/bin/python2.7 /home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py -fasta=$f -predictor=LowRes -origin=plant -result=$r -output=simple