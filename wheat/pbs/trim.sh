#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=100:00:00
#PBS -l mem=5gb
cd /home/nenarokova/ngs/wheat/
python trim.py
