#!/usr/bin/python
from subprocess import call
def parse_bed_file(bed_path):
    with open(bed_path, 'r') as bed_file:
        regions = {}
        for row in bed_file:
            split_row = row.split('\t')
            contig_id = split_row[0]
            start = split_row[1]
            end = split_row[2]
            strand = split_row[5][0]
            if contig_id not in regions.keys():
                regions[contig_id]=[]
            regions[contig_id].append( {"strand":strand, "borders": [int(start), int(end)]})
    bed_file.close()
    return regions

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
    print "Mpileup parsing is finished"
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

# bam_path="/media/4TB1/blastocrithidia/UTR_analyisis/references/blechomonas/mapping/blechomonas_rna_sorted.bam"
# bed_path="/media/4TB1/blastocrithidia/UTR_analyisis/references/blechomonas/TriTrypDB-33_BayalaiB08-376_-300_300_stop_environs.clean.bed"

# bam_path="/media/4TB1/blastocrithidia/UTR_analyisis/references/lseymouri/mapping/lseymouri_23_1_rna_sorted.bam"
# bed_path="/media/4TB1/blastocrithidia/UTR_analyisis/references/lseymouri/TriTrypDB-33_LseymouriATCC30220_-300_300_stop_environs.clean.bed"

# bam_path="/media/4TB1/novymonas/transcriptome/mapping/bowtie2_no_pand_pseudochr/no_pand_pseudochr_sorted.bam"
# bed_path="/media/4TB1/blastocrithidia/UTR_analyisis/references/novymonas/nesm_pseudo.out._-300_300_stop_environs.clean.bed"

bam_path="/home/nenarokova/blasto/rna_cov_analysis/lpyr/lpyr_h10_rna_all.bam"
bed_path="/home/nenarokova/blasto/rna_cov_analysis/lpyr/Leptomonas_pyrrhocoris_with_UTRs_all_genes_stops_corrected_-300_300_stop_environs.clean.bed"

mpileup_path=bed_path[:-4]+".mpileup"
outpath=bed_path[:-4]+"_cov_analysis.txt"

regions=parse_bed_file(bed_path)
print regions

samtools_call = ['samtools', 'mpileup', '-l', bed_path, bam_path, '-o', mpileup_path]
call(samtools_call)
print "Mpileup is finished"

environ_cov = parse_mpileup_file(mpileup_path)
print len(environ_cov.keys())
result = count_mean_cov_pos(environ_cov, regions, environ_length)

with open(outpath, 'w') as outfile:
    for item in result:
      outfile.write("%s\n" % item)
outfile.close()
