#!/bin/bash
mummer_path="/home/nenarokova/tools/MUMmer3.23"
export PATH=$PATH:$mummer_path

cd /home/nenarokova/tools/medusa/

ref_folder="/media/4TB1/blasto/reference_genomes"
java -jar medusa.jar -f $ref_folder -i /media/4TB1/blasto/p57_scaffolds.fa -v
