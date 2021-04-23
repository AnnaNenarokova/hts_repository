
gff_path = "/Users/annanenarokova/work/myxo_local/augustus_annot.gff3"
contig_dict = {}
gene_dict = {}

with open(gff_path, 'r') as gff_file:
    for line in gff_file:
        if "gene" in line and line[0] != "#":
            split_line = line.rstrip().split('\t')
            contig_id = split_line[0]
            gene_start = int(split_line[3])
            gene_end = int(split_line[4])
            strand = split_line[6]
            gene_id = split_line[8].split("=")[1]
            if contig_id in contig_dict:
            else:
                contig_dict[] = 





