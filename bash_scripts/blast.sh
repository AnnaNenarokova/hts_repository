#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=krtecek2.local:ppn=30
#PBS -o /home/nenarokova/blast_pbs.out
#PBS -e /home/nenarokova/blast_pbs.err
/home/nenarokova/ngs/py_scripts/blast/use_blast.py
