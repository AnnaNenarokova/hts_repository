#!/bin/bash
tophat --b2-very-sensitive -p 16 '/home/anna_nenarokova/euglena/euglena_genome/euglena_genome' \
'/home/anna_nenarokova/euglena/2_KE_reads/trim_out/paired_out_fw.fastq',\
'/home/anna_nenarokova/euglena/2_KE_reads/trim_out/unpaired_out_fw.fastq',\
'/home/anna_nenarokova/euglena/2_KE_reads/trim_out/unpaired_out_rv.fastq' \
'/home/anna_nenarokova/euglena/2_KE_reads/trim_out/paired_out_rv.fastq'

tophat --b2-very-fast -p 16 '/home/nenarokova/euglena/euglena_100_contigs/euglena_100_contigs' \
'/home/nenarokova/euglena/1_ELIS_reads/Sample_1-light/trim_out/paired_out_fw.fastq',\
'/home/nenarokova/euglena/1_ELIS_reads/Sample_2-dark/trim_out/paired_out_fw.fastq',\
'/home/nenarokova/euglena/2_KE_reads/trim_out/paired_out_fw.fastq',\
'/home/nenarokova/euglena/1_ELIS_reads/Sample_1-light/trim_out/unpaired_out_fw.fastq',\
'/home/nenarokova/euglena/1_ELIS_reads/Sample_2-dark/trim_out/unpaired_out_fw.fastq',\
'/home/nenarokova/euglena/2_KE_reads/trim_out/unpaired_out_fw.fastq',\
'/home/nenarokova/euglena/1_ELIS_reads/Sample_1-light/trim_out/unpaired_out_rv.fastq',\
'/home/nenarokova/euglena/1_ELIS_reads/Sample_2-dark/trim_out/unpaired_out_rv.fastq',\
'/home/nenarokova/euglena/2_KE_reads/trim_out/unpaired_out_rv.fastq' \
'/home/nenarokova/euglena/1_ELIS_reads/Sample_1-light/trim_out/paired_out_rv.fastq',\
'/home/nenarokova/euglena/1_ELIS_reads/Sample_2-dark/trim_out/paired_out_rv.fastq',\
'/home/nenarokova/euglena/2_KE_reads/trim_out/paired_out_rv.fastq'