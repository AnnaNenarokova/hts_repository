#!/bin/bash
#PBS -l nodes=1:ppn=24
#PBS -l walltime=100:00:00
cd /home/nenarokova/ngs/wheat/
python trim.py
