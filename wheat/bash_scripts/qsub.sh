#!/bin/bash

for i in {3..9}
do
	node='node0'$i
    qsub -t $i-$i -l nodes=$node bw2_all_L.sh
done 

for i in {10..32}
do
	node='node'$i
    qsub -t $i-$i -l nodes=$node bw2_all_L.sh
done 