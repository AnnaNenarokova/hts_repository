#!/bin/sh

raw_dir='/media/4TB1/blastocrithidia/bexlh/reads/raw/'
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip -O $raw_dir SRR1186295
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip -O $raw_dir SRR1186315
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip -O $raw_dir SRR1186516
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip -O $raw_dir SRR1186658
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip -O $raw_dir SRR1186749
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip -O $raw_dir SRR1186752
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip -O $raw_dir SRR1186787
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip -O $raw_dir SRR1186788
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip -O $raw_dir SRR1186789