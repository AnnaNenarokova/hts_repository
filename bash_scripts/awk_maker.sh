#!/bin/bash
maker_out="/mnt/data/martij04/Poly_Genome_annotation/Poly_assembly_outLeg_host_89contigs.PedDros.maker.output/Polyplax.all.maker1.noseq.gff"
fasta="/mnt/data/martij04/Poly_Genome_annotation/Poly_assembly_outLeg_host_89contigs.fasta"
fai="/mnt/data/martij04/Poly_Genome_annotation/Poly_assembly_outLeg_host_89contigs.fasta.fai"
bed_out="/home/nenarokova/jana_m/maker_out_rna.bed"
fasta_out="/home/nenarokova/jana_m/maker_out_rna.fasta"

awk -v OFS="\t" '{ if ($3 == "mRNA") print $1, $4, $5 }' $maker_out | \
  while read rna; \
  do \
  scaffold=`echo ${rna} | awk '{ print $1 }'`; \
  end=`cat $fai | awk -v scaffold="${scaffold}" \
    -v OFS="\t" '{ if ($1 == scaffold) print $2 }'`; \
  echo ${rna} | awk -v end="${end}" -v OFS="\t" '{ if ($2 < 1000 && (end - $3) < 1000) print $1, "0", end; \
    else if ((end - $3) < 1000) print $1, "0", end; \
    else if ($2 < 1000) print $1, "0", $3+1000; \
    else print $1, $2-1000, $3+1000 }'; \
  done > $bed_out

bedtools getfasta -fi $fasta -bed $bed_out -fo $fasta_out