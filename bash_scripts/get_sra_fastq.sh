#!/bin/sh

raw_dir='/media/4TB1/blastocrithidia/kika_workdir/reads/'
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip -O $raw_dir SRR4017993
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files --gzip -O $raw_dir SRR4017973