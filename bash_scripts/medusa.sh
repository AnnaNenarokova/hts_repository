#!/bin/bash
mummer_path="/home/nenarokova/tools/MUMmer3.23"
export PATH=$PATH:$mummer_path

cd /home/nenarokova/tools/medusa/

genome="/media/4TB1/blastocrithidia/scaffolding/medusa/jaculum_scaffolds.fna"
ref_folder="/media/4TB1/blastocrithidia/scaffolding/medusa/reference_genomes/all_best/"
java -jar medusa.jar -f $ref_folder -i $genome -v -w2 &

genome="/media/4TB1/blastocrithidia/scaffolding/medusa/triat_scaffolds.fa"
ref_folder="/media/4TB1/blastocrithidia/scaffolding/medusa/reference_genomes/all_best/"
java -jar medusa.jar -f $ref_folder -i $genome -v -w2 &


genome="/media/4TB1/blastocrithidia/scaffolding/medusa/p57_scaffolds.fa"
ref_folder="/media/4TB1/blastocrithidia/scaffolding/medusa/reference_genomes/all_best/"
java -jar medusa.jar -f $ref_folder -i $genome -v -w2 &
