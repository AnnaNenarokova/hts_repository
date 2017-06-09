#!/bin/bash
fasta="/home/nenarokova/genomes/euglena/tom40/canonical_tom40.fasta"
python /home/nenarokova/tools/pasta_tools/pasta/run_pasta.py -d PROTEIN -i $fasta
