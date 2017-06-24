#!/usr/bin/python
gff_path = "/home/anna/bioinformatics/blasto/igv_session_p57/annotation.gff"
bed_outpath = "/home/anna/bioinformatics/blasto/igv_session_p57/stop_codon_environs.bed"
def get_stop_codon_environs(gff_path, left_border=200, right_border=200):
    stop_codon_environs = {}

    with open(gff_path, 'r') as gff_file:
        with open(bed_outpath, 'w') as output:
            for row in gff_file:
                split_row = row.split('\t')
                contig_id = split_row[0]
                gene_start = int(split_row[3])
                gene_end = int(split_row[4])
                score = split_row[5]
                strand = split_row[6]
                contig_length = int(contig_id.split('_')[3])
                if gene_end <= gene_start:
                    print "Gene end <= gene start error"
                    exit(1)
                if strand == "+":
                    current_borders = [gene_end-left_border, gene_end+right_border]
                elif strand == "-":
                    current_borders = [gene_start-right_border, gene_start+left_border]
                else:
                    print "GFF strand error"
                    exit(1)
                if current_borders[0] > 0 and current_borders[1] <= contig_length:
                    if contig_id not in stop_codon_environs.keys():
                        stop_codon_environs[contig_id]=[]
                    stop_codon_environs[contig_id].append( {"strand":strand, "borders": current_borders} )
                    new_row = '{}\t{}\t{}\t{}\t{}\t{}\n'.format(contig_id, current_borders[0], current_borders[1], 'name', score, strand)
                    output.write(new_row)
        output.close()
    gff_file.close()

    return stop_codon_environs

stop_codon_environs = get_stop_codon_environs(gff_path)
print len(stop_codon_environs)
