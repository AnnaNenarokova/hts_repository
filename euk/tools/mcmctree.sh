#!/bin/bash
workdir="/Users/vl18625/work/euk/benoit_toy_mcmctree/mcmctree/"
control_file="/mnt/alvarium2pool/scratch/nenarokova/euk/toyset_benoit/mcmctree/mcmctree.ctl"
bin_path="/scratch/nenarokova/tools/paml4.9i/src/"
PATH=$PATH:$bin_path

cd $workdir
mcmctree $control_file