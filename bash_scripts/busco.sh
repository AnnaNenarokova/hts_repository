#!/bin/sh
cd /home/nenarokova/tools/busco

genome=""
name=""
ref_set=""
python scripts/run_BUSCO.py -i $genome -o $name -l $ref_set -m [MODE]
