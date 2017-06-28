#!/bin/sh

f="/home/kika/Dropbox/blasto_project/blastocrithidia/genes/thiolation/mtu11.fasta"
r="/home/kika/Dropbox/blasto_project/blastocrithidia/genes/thiolation/mtu11_multiloc.txt"

/usr/bin/python2.7 /home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py -fasta=$f -predictor=LowRes -origin=plant -result=$r -output=simple