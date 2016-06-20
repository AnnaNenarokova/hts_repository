#!/bin/bash
folder='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/merged_reads/reads'

fw=$folder'18021_1_7_unmerged_fw.fq'
rv=$folder'18021_1_7_unmerged_rv.fq'
trimmed_fw='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/merged_reads/18021_1_7_unmerged_trimmed_fw.fq'
trimmed_rv='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/merged_reads/18021_1_7_unmerged_trimmed_rv.fq'

/home/nenarokova/tools/bbmap/bbduk.sh in=$fw in=$rv out1=$trimmed_fw out2=$trimmed_rv qtrim=rl trimq=20


fw=$folder'18098_1_7_unmerged_fw.fq'
rv=$folder'18098_1_7_unmerged_rv.fq'
trimmed_fw='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/merged_reads/18098_1_7_unmerged_trimmed_fw.fq'
trimmed_rv='/media/4TB1/kinetoplastids_hinxton/illumina/miseq/merged_reads/18098_1_7_unmerged_trimmed_rv.fq'

/home/nenarokova/tools/bbmap/bbduk.sh in=$fw in=$rv out1=$trimmed_fw out2=$trimmed_rv qtrim=rl trimq=20
