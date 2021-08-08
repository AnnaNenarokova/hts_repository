#!/bin/bash

in_folder="/mnt/data/pangenome/prokka_out/"
out_folder="/mnt/data/pangenome/prot_database/"

cd $in_folder

for name in *
    do
        file=$(echo $in_folder$name"/"*.faa)
        cp $file $out_folder$name".faa"
    done
