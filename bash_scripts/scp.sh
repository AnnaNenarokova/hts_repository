#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=100:00:00

scp -r 172.18.4.4:/media/4TB1/kinetoplastids_hinxton/illumina .
