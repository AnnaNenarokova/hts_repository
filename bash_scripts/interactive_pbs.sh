#!/bin/bash
qsub -I -l nodes=1:ppn=60,walltime=24:00:00

qsub -I -l nodes=krtecek3:ppn=1,walltime=24:00:00
