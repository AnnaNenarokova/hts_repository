#!/bin/bash
cog_dir=""
cog_hmm_dir=""

cd $cog_dir
for cog in *.fa
do
	hmmbuild $outfile $alignment
done
