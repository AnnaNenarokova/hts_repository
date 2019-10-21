#!/bin/bash
rawdir="/media/4TB1/lmexicana_ku/reads/raw/"
trimdir="/media/4TB1/lmexicana_ku/reads/trimmed/"
files=( EEP_KO1_cl2 EEP_KO2_pop1 L_mexicana_LmxM.28.0090_KO L_mexicana_LmxM.16.0790_KO Lmex_Ku70_cl_9 Lmex_Ku80_cl_2 )
for f in ${files[@]}
do
    echo $f
    fw=$rawdir$f"_1.fastq.gz"
    rv=$rawdir$f"_2.fastq.gz"
    name=$f
    trimmed_fw=$trimdir$name"_trimmed_1.fq.gz"
    trimmed_rv=$trimdir$name"_trimmed_2.fq.gz"
    report=$trimdir$name"_report.txt"
    threads="30"
    adapters="/home/nenarokova/tools/bbmap/resources/adapters.fa"
    /home/nenarokova/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapters usejni=t ktrim=r k=22 mink=11 hdist=2 tpe tbo t=$threads qtrim=rl trimq=20
done
