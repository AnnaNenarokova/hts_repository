#!/bin/bash

link_part1="https://trace.ncbi.nlm.nih.gov/Traces/sra/?path=%2Fnetmnt%2Ftraces04%2Fsra29%2FSRR%2F001997%2FSRR2045882&run=SRR2045882&acc=LpyrH10_"
link_part2="&ref=LpyrH10_"
link_part3="&range=&output=bam&output_to=File"

name="LpyrH10_"
padtowidth=2
for i in {1..57}
do
    n=`printf "%0*d\n" $padtowidth $i`
    file_name=$name$n".bam"
    wget -O $file_name $link_part1$n$link_part2$n$link_part3
done


link_part1="https://trace.ncbi.nlm.nih.gov/Traces/sra/?path=%2Fnetmnt%2Ftraces04%2Fsra31%2FSRR%2F002000%2FSRR2048652&run=SRR2048652&acc=Lsey_"
link_part2="&ref=Lsey_"
link_part3="&range=&output=bam&output_to=File"
name="SRR2048652_Lsey_"
padtowidth=4
for i in {1..1190}
do
    n=`printf "%0*d\n" $padtowidth $i`
    file_name=$name$n".bam"
    wget -O $file_name $link_part1$n$link_part2$n$link_part3
done

samtools merge $name"all".bam *.bam
