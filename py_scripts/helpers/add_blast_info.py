#!/usr/bin/python3

in_path = "/home/anna/bioinformatics/diplonema/dpapi_genome_diamond_annotation.tsv"
blast_path = "/home/anna/bioinformatics/diplonema/Dp_PB-MI_190104_dedup_cut_l100.faa_egracilis_bl_report_best.csv"
outpath = "/home/anna/bioinformatics/diplonema/dpapi_genome_diamond_annotation_e_values.tsv"

blast_evalues = {}
with open(blast_path) as blast_f:
    for line in blast_f:
        line_split = line.rstrip().split(",")
        id = line_split[0]
        evalue = line_split[5]
        blast_evalues[id] = evalue

with open(in_path) as input_f, open(outpath, "w") as output_f:
    for line in input_f:
        line = line.rstrip()
        id = line.split("\t")[0]
        if id in blast_evalues.keys():
            evalue = blast_evalues[id]
        else:
            evalue = "#N/A"
        new_line = line + "\t" + evalue + "\n"
        output_f.write(new_line)
