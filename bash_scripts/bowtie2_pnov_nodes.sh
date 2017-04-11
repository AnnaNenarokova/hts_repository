#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=30

bw2_dir='/home/nenarokova/tools/bowtie2-2.2.9/'
fasta='/home/nenarokova/genomes/pandoraea_nodes.fasta'
bt2_base="/home/nenarokova/genomes/novymonas/assembly/pandoraea_all_nodes"
$bw2_dir'bowtie2-build' --threads 30 $fasta $bt2_base

se1="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_merged/wt_S2_L001_merged_trimmed.fq"
pe1_1="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_merged/wt_S2_L001_unmerged_trimmed_1.fq"
pe1_2="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_merged/wt_S2_L001_unmerged_trimmed_2.fq"

se2="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_merged/azi_S1_adapter_trimmed_merged.fq"
pe2_1="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_merged/azi_S1_unmerged_trimmed_1.fq"
pe2_2="/home/nenarokova/genomes/novymonas/raw_illumina/miseq_merged/azi_S1_unmerged_trimmed_2.fq"

pe3_1="/home/nenarokova/genomes/novymonas/raw_illumina/old_hiseq_trimmed/E262_1_trimmed.fastq"
pe3_2="/home/nenarokova/genomes/novymonas/raw_illumina/old_hiseq_trimmed/E262_2_trimmed.fastq"

base_name="/home/nenarokova/genomes/novymonas/assembly/pandoraea_all_nodes_mapping"
mapped_unpaired=$base_name"_mapped_unpaired.fq"
mapped_unconc=$base_name"_mapped.fq"
mapped_conc=$base_name"_mapped.fq"
alignment=$base_name".sam"
report=$base_name".txt"

/home/nenarokova/tools/bowtie2-2.2.9/bowtie2 --very-sensitive-local -p 30 -x $bt2_base -U $se1,$se2 -1 $pe1_1,$pe2_1,$pe3_1 -2 $pe1_2,$pe2_2,$pe3_2  --al $mapped_unpaired --un-conc-gz $mapped_unconc --al-conc-gz $mapped_conc -S $alignment 2> $report

