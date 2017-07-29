#!/usr/bin/python
from subprocess import call

def get_codon_environs(gff_path, bed_out_path, left_border=-200, right_border=200, spades_ids=False, feature="gene", stops_included="True", starts=False):
    codon_environs = {}
    with open(gff_path, 'r') as gff_file:
        len_contigs={}
        with open(bed_out_path, 'w') as output:
            for row in gff_file:
                if row[0] == "#":
                    if not spades_ids and row[:17] == "##sequence-region" :
                        split_row = row.split(' ')
                        contig_id = split_row[1]
                        contig_length = split_row[3]
                        len_contigs[contig_id] = contig_length
                else:
                    split_row = row.split('\t')
                    contig_id = split_row[0]
                    feature_type = split_row[2]
                    gene_start = int(split_row[3])
                    if stops_included:
                        gene_end = int(split_row[4])
                    else:
                        gene_end = int(split_row[4]) + 3
                    score = split_row[5]
                    strand = split_row[6]
                    if spades_ids:
                        contig_length = int(contig_id.split('_')[3])
                    else:
                        contig_length = len_contigs[contig_id]
                    if feature_type == feature:
                        if gene_end <= gene_start:
                            print "Gene end <= gene start error"
                            print gene_start, gene_end
                            exit(1)
                        if starts:
                            if strand == "+":
                                current_borders = [gene_start+left_border, gene_start+right_border]
                            elif strand == "-":
                                current_borders = [gene_end-right_border-4, gene_end-left_border-4]
                            else:
                                print "GFF strand error"
                        else:
                            if strand == "+":
                                current_borders = [gene_end+left_border, gene_end+right_border]
                            elif strand == "-":
                                current_borders = [gene_start-right_border-4, gene_start-left_border-4]
                            else:
                                print "GFF strand error"
                                exit(1)
                        if current_borders[0] > 0 and current_borders[1] <= contig_length:
                            if contig_id not in codon_environs.keys():
                                codon_environs[contig_id]=[]
                            codon_environs[contig_id].append( {"strand":strand, "borders": current_borders} )
                            new_row = '{}\t{}\t{}\t{}\t{}\t{}\n'.format(contig_id, current_borders[0], current_borders[1], 'name', score, strand)
                            output.write(new_row)
        output.close()
    gff_file.close()
    return codon_environs

def parse_mpileup_file(mpileup_path):
    with open(mpileup_path, 'r') as mpileup_file:
        cov_per_position = {}
        for row in mpileup_file:
            split_row = row.split('\t')
            contig = split_row[0]
            position = split_row[1]
            coverage = split_row[3]

            if contig not in cov_per_position.keys():
                cov_per_position[contig] = {}
            cov_per_position[contig][position] = coverage
    mpileup_file.close()
    return cov_per_position

def count_mean_cov_pos(coverage, regions, region_len):
    cov_matrix = [0 for i in range(region_len)]
    region_number = 0
    print coverage.keys()
    for contig in regions:
        print contig
        for region in regions[contig]:
            if contig in coverage.keys():
                region_number += 1
                cur_cov_matrix = [0 for i in range(region_len)]
                for i,v in enumerate(cur_cov_matrix):
                    position = str(region["borders"][0] + i + 1)
                    if position in coverage[contig].keys():
                        cur_cov_matrix[i] = coverage[contig][position]
                    else:
                        cur_cov_matrix[i] = 0
                if region["strand"] == "+":
                    pass
                elif region["strand"] == "-":
                    cur_cov_matrix.reverse()
                else:
                    print "Strand error"
                    exit (1)
                for i, v in enumerate(cov_matrix):
                    cov_matrix[i] += int(cur_cov_matrix[i])
            else: print contig, "not found in mpileup file"
    cov_matrix = [i/float(region_number) for i in cov_matrix]
    return cov_matrix


left_border = 300
right_border = 300
environ_length = left_border + right_border

gff_path="/home/nenarokova/blasto/rna_cov_analysis/Leptomonas_pyrrhocoris_with_UTRs_all_genes_stops_corrected.gff"
bam_path="/home/nenarokova/blasto/rna_cov_analysis/lpyr_h10_rna_all.bam"

bed_path="/home/nenarokova/blasto/rna_cov_analysis/lpyr_h10_stop_environs.bed"
mpileup_path="/home/nenarokova/blasto/rna_cov_analysis/lpyr_h10_stop_environs.mpileup"

outpath="/home/nenarokova/blasto/rna_cov_analysis/lpyr_h10_stop_environs.txt"

stop_codon_environs = get_stop_codon_environs(gff_path, bed_path, left_border=left_border, right_border=right_border, spades_ids=False, feature="CDS", stops_included=True)
# stop_codon_environs = get_stop_codon_environs(gff_path, bed_path, left_border=left_border, right_border=right_border, spades_ids=True, feature="gene", stops_included=False)
print len(stop_codon_environs)

samtools_call = ['samtools', 'mpileup', '-l', bed_path, bam_path, '-o', mpileup_path]
call(samtools_call)

environ_cov = parse_mpileup_file(mpileup_path)
print len(environ_cov.keys())
result = count_mean_cov_pos(environ_cov, stop_codon_environs, environ_length)

print result

with open(outpath, 'w') as outfile:
    for item in result:
      outfile.write("%s\n" % item)
outfile.close()

