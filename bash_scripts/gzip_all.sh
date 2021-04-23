#!/bin/bash
gzip /mnt/data/metagenomic_data/reads/trimmed/trimmed_data_janar/Eliska_Crataerina_R1_qtrim_bbduk.fastq &
gzip /mnt/data/metagenomic_data/reads/trimmed/trimmed_data_janar/Eliska_Crataerina_R2_qtrim_bbduk.fastq &
gzip /mnt/data/metagenomic_data/reads/trimmed/K26_adapter_trimmed_merged.fq &
gzip /mnt/data/metagenomic_data/reads/trimmed/K26_adapter_trimmed_unmerged_1.fq &
gzip /mnt/data/metagenomic_data/reads/trimmed/K26_adapter_trimmed_unmerged_2.fq
