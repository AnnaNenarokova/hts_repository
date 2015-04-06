#!/bin/bash
for i in {3:9}
do
    qsub -t $i-$i -l nodes=node0$i bw2_all_L.sh
done 
for i in {10:32}
do
    qsub -t $i-$i -l nodes=node$i bw2_all_L.sh
done 