#!/usr/bin/python
from subprocess import call


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

