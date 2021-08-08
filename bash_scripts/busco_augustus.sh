#!/bin/bash

fasta="/home/nenarokova/jana_m/maker_out_rna.fasta"
outdir="/home/nenarokova/jana_m/busco_out/"
cd $outdir

out="busco_augustus"
augustus_config="/home/software/Augustus/config"

export AUGUSTUS_CONFIG_PATH=$augustus_config
metaeuk_path="/home/software/metaeuk/bin"

export PATH="$metaeuk_path:$PATH"

threads=40

busco -i $fasta -o $out -f -l insecta_odb10 -m genome -c $threads --augustus --long --augustus_parameters='--progress=true' --augustus_species Pediculus