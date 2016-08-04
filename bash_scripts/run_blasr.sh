#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=60

libcpp='/home/nenarokova/tools/blasr_install/blasr/libcpp'
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$libcpp/hdf:$libcpp/alignment:$libcpp/pbdata:/home/nenarokova/tools/blasr_install/hdf5/hdf5-1.8.16-linux-centos6-x86_64-gcc447-shared/lib
blasr='/home/nenarokova/tools/blasr_install/blasr/blasr'

ref='/home/nenarokova/kinetoplastids/contaminants/genomes/pandoraea_apista_AU2161.fasta'
folder='/home/nenarokova/kinetoplastids/pacbio/raw_reads/e262/'
out='/home/nenarokova/kinetoplastids/contaminants/genomes/pandoraea_apista_e262_pacbio.out'

for f in $folder*.bax.h5
do
  $blasr $f $ref --nproc 60 -m 0 >> out
done
