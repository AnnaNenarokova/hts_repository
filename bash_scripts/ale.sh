#!/bin/bash
ale="/home/nenarokova/tools/ALE/src/ALE"
bam="/media/4TB1/blastocrithidia/mapping/jac_genome_transc/jac_genome_transc_DNA_sorted.bam"
genome="/media/4TB1/blastocrithidia/genome_assembly/jaculum_spades_transcriptome/scaffolds.fasta"
out="/media/4TB1/blastocrithidia/genome_assembly/jaculum_spades_transcriptome/ale_out.txt"
$ale $bam $genome $out
