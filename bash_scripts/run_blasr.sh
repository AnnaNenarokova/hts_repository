#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=60

libcpp='/home/nenarokova/tools/blasr_install/blasr/libcpp'
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$libcpp/hdf:$libcpp/alignment:$libcpp/pbdata:/home/nenarokova/tools/blasr_install/hdf5/hdf5-1.8.16-linux-centos6-x86_64-gcc447-shared/lib
blasr='/home/nenarokova/tools/blasr_install/blasr/blasr'

ref='/home/nenarokova/genomes/Trypanoplasma_borreli/miniasm/contigs.fasta'
folder='/home/nenarokova/genomes/Trypanoplasma_borreli/TCS_Michael_Giolai_TGAC/Raw_reads/all_subreads/'
out='/home/nenarokova/genomes/Trypanoplasma_borreli/miniasm/read_mapping.bam'

# for f in $folder*.fastq
# do
#   $blasr $f $ref --nproc 60 -sam >> $out
# done

f1="/home/nenarokova/genomes/Trypanoplasma_borreli/TCS_Michael_Giolai_TGAC/Raw_reads/D06_1/Analysis_Results/m151008_074519_42165_c100914232550000001823208104301613_s1_p0.bas.h5"
f2="/home/nenarokova/genomes/Trypanoplasma_borreli/TCS_Michael_Giolai_TGAC/Raw_reads/E06_1/Analysis_Results/m151008_120454_42165_c100914232550000001823208104301614_s1_p0.bas.h5"
$blasr $f1 $2 $ref --nproc 60 --bam -clipping soft --out $out
