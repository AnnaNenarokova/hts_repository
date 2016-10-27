#!/bin/bash

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/nenarokova/tools/pitchfork/deployment/lib
blasr='/home/nenarokova/tools/pitchfork/deployment/bin/blasr'

ref='/home/nenarokova/genomes/trypanoplasma/miniasm_contigs_sorted.fasta'
out='/home/nenarokova/genomes/trypanoplasma/pacbio_read_mapping.bam'

f1='/home/nenarokova/genomes/trypanoplasma/TCS_Michael_Giolai_TGAC/Raw_reads/D06_1/Analysis_Results/m151008_074519_42165_c100914232550000001823208104301613_s1_p0.bas.h5'
$blasr $f1 $ref --nproc 32 --clipping soft --bam $out
