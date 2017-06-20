#!/bin/sh

f="/home/kika/MEGAsync/Publikacie/EL_plastid/predict.txt"
r="/home/kika/MEGAsync/Publikacie/EL_plastid/predict_multiloc.txt"

/usr/bin/python2.7 /home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py -fasta=$f -predictor=LowRes -origin=plant -result=$r -output=simple