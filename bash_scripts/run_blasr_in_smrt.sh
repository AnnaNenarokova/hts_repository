#!/bin/bash
source /home/smrtanalysis/current/etc/setup.sh

f1="/media/4TB3/trypanoplasma/sequencing_data/TCS_Michael_Giolai_TGAC/Raw_reads/D06_1/Analysis_Results/m151008_074519_42165_c100914232550000001823208104301613_s1_p0.1.bax.h5"
f2="/media/4TB3/trypanoplasma/sequencing_data/TCS_Michael_Giolai_TGAC/Raw_reads/D06_1/Analysis_Results/m151008_074519_42165_c100914232550000001823208104301613_s1_p0.2.bax.h5"
f3="/media/4TB3/trypanoplasma/sequencing_data/TCS_Michael_Giolai_TGAC/Raw_reads/D06_1/Analysis_Results/m151008_074519_42165_c100914232550000001823208104301613_s1_p0.3.bax.h5"
f4="/media/4TB3/trypanoplasma/sequencing_data/TCS_Michael_Giolai_TGAC/Raw_reads/E06_1/Analysis_Results/m151008_120454_42165_c100914232550000001823208104301614_s1_p0.1.bax.h5"
f5="/media/4TB3/trypanoplasma/sequencing_data/TCS_Michael_Giolai_TGAC/Raw_reads/E06_1/Analysis_Results/m151008_120454_42165_c100914232550000001823208104301614_s1_p0.2.bax.h5"
f6="/media/4TB3/trypanoplasma/sequencing_data/TCS_Michael_Giolai_TGAC/Raw_reads/E06_1/Analysis_Results/m151008_120454_42165_c100914232550000001823208104301614_s1_p0.3.bax.h5"

out="/media/4TB3/trypanoplasma/mapping/pacbio_reads.sam"
unaligned="/media/4TB3/trypanoplasma/mapping/unaligned_pacbio_reads"
blasr $f1 $f2 $f3 $f4 $f5 $f6 -clipping soft -unaligned $unaligned -sam -out $out -nproc 31
