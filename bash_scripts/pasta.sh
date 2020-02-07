#!/bin/bash
pasta="/home/users/nenarokova/tools/pasta-code/pasta/run_pasta.py"
fasta="/home/users/nenarokova/zachar/scf25_dataset.faa"

python $pasta -d PROTEIN -i $fasta
