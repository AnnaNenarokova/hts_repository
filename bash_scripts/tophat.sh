#!/bin/bash
tophat --b2-very-sensitive -p 16 '/home/anna_nenarokova/euglena/euglena_first_scaffold/euglena_first_scaffold' \
'/home/anna_nenarokova/euglena/1_ELIS_reads/Sample_1-light/trim_out/paired_out_fw.fastq',\
'/home/anna_nenarokova/euglena/1_ELIS_reads/Sample_2-dark/trim_out/paired_out_fw.fastq',\
'/home/anna_nenarokova/euglena/2_KE_reads/trim_out/paired_out_fw.fastq',\
'/home/anna_nenarokova/euglena/1_ELIS_reads/Sample_1-light/trim_out/unpaired_out_fw.fastq',\
'/home/anna_nenarokova/euglena/1_ELIS_reads/Sample_2-dark/trim_out/unpaired_out_fw.fastq',\
'/home/anna_nenarokova/euglena/2_KE_reads/trim_out/unpaired_out_fw.fastq',\
'/home/anna_nenarokova/euglena/1_ELIS_reads/Sample_1-light/trim_out/unpaired_out_rv.fastq',\
'/home/anna_nenarokova/euglena/1_ELIS_reads/Sample_2-dark/trim_out/unpaired_out_rv.fastq',\
'/home/anna_nenarokova/euglena/2_KE_reads/trim_out/unpaired_out_rv.fastq' \
'/home/anna_nenarokova/euglena/1_ELIS_reads/Sample_1-light/trim_out/paired_out_rv.fastq',\
'/home/anna_nenarokova/euglena/1_ELIS_reads/Sample_2-dark/trim_out/paired_out_rv.fastq',\
'/home/anna_nenarokova/euglena/2_KE_reads/trim_out/paired_out_rv.fastq'