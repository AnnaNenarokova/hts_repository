#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=60
ref='/home/nenarokova/kinetoplastids/contaminants/genomes/pandoraea_apista_AU2161.fasta'
query='/home/nenarokova/kinetoplastids/pacbio/raw_reads/e262/m151013_144051_00127_c100885902550000001823202004021681_s1_p0.1.bax.h5'
alignment='/home/nenarokova/kinetoplastids/pacbio/m151013_144051_00127_c100885902550000001823202004021681_s1_p0_1_test.aln'
libcpp='/home/nenarokova/tools/blasr_install/blasr/libcpp'
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$libcpp/hdf:$libcpp/alignment:$libcpp/pbdata

blasr='/home/nenarokova/tools/blasr_install/blasr/blasr'
$blasr $query $ref -out $alignment -nproc 60 -m 0
