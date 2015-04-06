#!/bin/bash

for i in {3..9}
do
	node='node0'$i
	k=$(($i + 30))
	echo $k
    qsub -t $i-$i -l nodes=$node bw2_all_L.sh
done 

for i in {10..19}
do
	node='node'$i
	k=$(($i + 30))
	echo $k
    qsub -t $i-$i -l nodes=$node bw2_all_L.sh
done 