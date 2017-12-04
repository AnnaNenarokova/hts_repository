#!/bin/bash
cd /home/anna/bioinformatics/all_tryp_references
names=(BayalaiB08-376 CfasciculataCfCl EmonterogeiiLV88 LaethiopicaL147 LarabicaLEM1108 LbraziliensisMHOMBR75M2903 LbraziliensisMHOMBR75M2904 LdonovaniBHU1220 LdonovaniBPK282A1 LenriettiiLEM3045 LgerbilliLEM452 LinfantumJPCM5 LmajorFriedlin LmajorLV39c5 LmajorSD75.1 LmexicanaMHOMGT2001U1103 LpanamensisMHOMCOL81L13 LpyrrhocorisH10 LseymouriATCC30220 LspMARLEM2494 LtarentolaeParrotTarII LtropicaL590 LturanicaLEM423 TbruceigambienseDAL972 TbruceiLister427 TbruceiTREU927 TcongolenseIL3000 TcruziCLBrener TcruziCLBrenerEsmeraldo-like TcruziCLBrenerNon-Esmeraldo-like TcruziDm28c TcruzimarinkelleiB7 TcruziSylvioX10-1 TevansiSTIB805 TgrayiANR4 TrangeliSC58 TvivaxY486)

for name in ${names[*]}
do
    wget "http://tritrypdb.org/common/downloads/Current_Release/"$name"/fasta/data/TriTrypDB-34_"$name"_AnnotatedCDSs.fasta"
    wget "http://tritrypdb.org/common/downloads/Current_Release/"$name"/fasta/data/TriTrypDB-34_"$name"_AnnotatedProteins.fasta"
    wget "http://tritrypdb.org/common/downloads/Current_Release/"$name"/fasta/data/TriTrypDB-34_"$name"_AnnotatedTranscripts.fasta"
    wget "http://tritrypdb.org/common/downloads/Current_Release/"$name"/fasta/data/TriTrypDB-34_"$name"_Genome.fasta"
    wget "http://tritrypdb.org/common/downloads/Current_Release/"$name"/fasta/data/TriTrypDB-34_"$name"_ORFs_AA.fasta"
    wget "http://tritrypdb.org/common/downloads/Current_Release/"$name"/gff/data/TriTrypDB-34_"$name".gff"
    wget "http://tritrypdb.org/common/downloads/Current_Release/"$name"/txt/TriTrypDB-34_"$name"_CodonUsage.txt"
    wget "http://tritrypdb.org/common/downloads/Current_Release/"$name"/txt/TriTrypDB-34_"$name"_InterproDomains.txt"
done

cd /home/anna/bioinformatics/references/tritrypdb_references/tritrypdb_34/everything/
release="34"
for name in ${names[*]}
do
    # wget "http://tritrypdb.org/common/downloads/release-$release/"$name"/fasta/data/TriTrypDB-"$release"_"$name"_AnnotatedCDSs.fasta"
    # wget "http://tritrypdb.org/common/downloads/release-$release/"$name"/fasta/data/TriTrypDB-"$release"_"$name"_AnnotatedProteins.fasta"
    # wget "http://tritrypdb.org/common/downloads/release-$release/"$name"/fasta/data/TriTrypDB-"$release"_"$name"_AnnotatedTranscripts.fasta"
    # wget "http://tritrypdb.org/common/downloads/release-$release/"$name"/fasta/data/TriTrypDB-"$release"_"$name"_Genome.fasta"
    # wget "http://tritrypdb.org/common/downloads/release-$release/"$name"/fasta/data/TriTrypDB-"$release"_"$name"_ORFs_AA.fasta"
    # wget "http://tritrypdb.org/common/downloads/release-$release/"$name"/gff/data/TriTrypDB-"$release"_"$name".gff"
    wget "http://tritrypdb.org/common/downloads/release-"$release"/"$name"/txt/TriTrypDB-"$release"_"$name"_CodonUsage.txt"
    wget "http://tritrypdb.org/common/downloads/release-"$release"/"$name"/txt/TriTrypDB-"$release"_"$name"_InterproDomains.txt"
done
