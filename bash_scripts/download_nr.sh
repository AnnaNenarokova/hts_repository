#!/bin/bash
wgs_file="/home/anna/bioinformatics/zachar/wgs_selector.csv"
outdir="/home/anna/bioinformatics/zachar/archaea_genomes/"
cd $outdir

fields="prefix_s project_s targeted_locus_name_s div_s organism_an bioproject_s biosample_ss infra_name_ss other_src_ss contigs_total_length_l contigs_count_l contigs_proteins_count_l contigs_annotated_s scaffolds_count_l scaffolds_proteins_count_l scaffolds_total_length_l scaffolds_annotated_s scaffolds_range_ss"

link_base1="https://sra-download.ncbi.nlm.nih.gov/traces/wgs0"
link_base2="/wgs_aux/"
link_end_nt=".1.fsa_nt.gz"
link_end_aa="P.1.fsa_aa.gz"

while IFS="," read $fields
    do
        echo $prefix_s
        for i in 1 2 3
        do
            link_middle="${prefix_s:0:2}/${prefix_s:2:2}/$prefix_s/$prefix_s"
            link_base=$link_base1$i$link_base2
            link_nt=$link_base$link_middle$link_end_nt
            wget $link_nt
            link_aa=$link_base$link_middle$link_end_aa
            wget $link_aa
        done
    done < $wgs_file
