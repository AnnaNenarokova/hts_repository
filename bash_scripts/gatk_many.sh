#!/bin/bash
reference="/home/users/nenarokova/ku_leishmania/LmxM379-SNV.fa"
input_folder="/home/users/nenarokova/ku_leishmania/LmxM379-SNV_mapping/"
input="/home/users/nenarokova/ku_leishmania/LmxM379-SNV_mapping/EEP_KO1_cl2_sorted.bam"
output="/home/users/nenarokova/ku_leishmania/LmxM379-SNV_mapping/EEP_KO1_cl2_sorted.vcf"

samtools faidx $reference

picard="/home/users/nenarokova/tools/picard.jar"
java -jar $picard CreateSequenceDictionary R= $reference

gatk --java-options "-Xmx20G" HaplotypeCaller -R $reference -I $input -O $output
