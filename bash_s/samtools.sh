#!/bin/bash
cd /home/anna/bioinformatics/bioprograms/samtools-1.1
# samtools view -bS /home/anna/bioinformatics/outdirs/T5adapt_ACTTGA_L001_R1_001/bowtie2_out_t5/alignment.sam > /home/anna/bioinformatics/outdirs/T5adapt_ACTTGA_L001_R1_001/bowtie2_out_t5/alignment.bam
# samtools view -f 0x10 /home/anna/bioinformatics/outdirs/T5adapt_ACTTGA_L001_R1_001/bowtie2_out_t5/alignment.sam > /home/anna/bioinformatics/outdirs/T5adapt_ACTTGA_L001_R1_001/bowtie2_out_t5/alignment.bam
# samtools view -F 0x10 /home/anna/bioinformatics/outdirs/T5adapt_ACTTGA_L001_R1_001/bowtie2_out_t5/alignment.bam > /home/anna/bioinformatics/outdirs/T5adapt_ACTTGA_L001_R1_001/bowtie2_out_t5/forward.bam
# samtools view -cS /home/anna/bioinformatics/outdirs/T5adapt_ACTTGA_L001_R1_001/bowtie2_out_t5/forward.sam
samtools view  -c -F 20 /home/anna/bioinformatics/outdirs/T5adapt_ACTTGA_L001_R1_001/bowtie2_out_t5/alignment.bam 

# samtools view -c -F 20 /home/anna/bioinformatics/outdirs/T5adapt_ACTTGA_L001_R1_001/bowtie2_out_t5/alignment.bam
# samtools view -c -f 20 /home/anna/bioinformatics/outdirs/T5adapt_ACTTGA_L001_R1_001/bowtie2_out_t5/alignment.bam
