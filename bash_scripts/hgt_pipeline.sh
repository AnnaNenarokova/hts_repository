#!/bin/bash
threads="30"

infasta=""
outdir=""

#Diamond
nr_diamond_path="/media/4TB3/ncbi/nr_diamond.dmnd"
taxonmap="/media/4TB3/ncbi/prot.accession2taxid.gz"
taxonnodes="/media/4TB3/ncbi/taxdmp/nodes.dmp"

diamond_out=$outdir"dpapi_genome_diamond.out"
