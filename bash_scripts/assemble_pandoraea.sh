#!/bin/bash

pe1_1="/media/4TB1/novymonas/azi_scaffolds_cov_more_10_unmapped_paired.fq.1.gz"
pe1_2="/media/4TB1/novymonas/azi_scaffolds_cov_more_10_unmapped_paired.fq.2.gz"

outdir="/media/4TB1/novymonas/pandoraea_assembly/"

report=$outdir"spades_report.txt"

/home/nenarokova/tools/SPAdes-3.10.0-Linux/bin/spades.py --pe1-1 $pe1_1 --pe1-2 $pe1_2 --careful -t 30 -o $outdir 2> $report
