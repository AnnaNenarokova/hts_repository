#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=60

libcpp='/home/nenarokova/tools/blasr_install/blasr/libcpp'
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/nenarokova/tools/blasr/lib
# $libcpp/hdf:$libcpp/alignment:$libcpp/pbdata:/home/nenarokova/tools/blasr_install/hdf5/hdf5-1.8.16-linux-centos6-x86_64-gcc447-shared/lib
blasr='/home/nenarokova/tools/blasr/bin/blasr'

ref='/home/nenarokova/genomes/Trypanoplasma_borreli/miniasm/contigs.fasta'
out='/home/nenarokova/genomes/Trypanoplasma_borreli/miniasm/read_mapping.bam'

f1='/home/nenarokova/genomes/trypanoplasma/miniasm/reads.fasta'
$blasr $f1 $ref --nproc 60 --clipping soft --bam $out
