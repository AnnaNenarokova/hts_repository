#!/bin/bash
folder="/home/nenarokova/genomes/euglena/tom40/"

alignment="/home/nenarokova/genomes/euglena/tom40/pastajob2.marker001.canonical_tom40.aln"
name="canonical_tom40"

alignment="/home/nenarokova/genomes/euglena/tom40/pastajob3.marker001.atom40.aln"
name="atom40"

alignment="/home/nenarokova/genomes/euglena/tom40/pastajob4.marker001.alveolata_tom40.aln"
name="alveolata_tom40"

alignment="/home/nenarokova/genomes/euglena/tom40/pastajob5.marker001.all_tom40.aln"
name="all_tom40"


outfile=$folder$name".hmm"
/home/nenarokova/tools/hmmer-3.1b2-linux-intel-x86_64/binaries/hmmbuild -n $name $outfile $alignment
