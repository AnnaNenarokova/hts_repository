#!/usr/bin/python3
from subprocess import call
from Bio import SeqIO
from Bio import motifs

def get_environs(gff_path, bed_out_path=False, left_border=-1, right_border=2, feature="PAS"):
    if not bed_out_path:
        bed_out_path='{}_{}_{}_environs.bed'.format(gff_path[:-4],left_border, right_border)
    with open(gff_path, 'r') as gff_file:
        with open(bed_out_path, 'w') as output:
            for row in gff_file:
                if row[0] != "#":
                    split_row = row.split('\t')
                    # print split_row
                    # break
                    contig_id = split_row[0]
                    feature_type = split_row[2]
                    gene_start = int(split_row[3])
                    gene_end = int(split_row[4])
                    score = split_row[5]
                    strand = split_row[6][0]
                    count = (split_row[8].split(";")[1]).split("=")[1]
                    if feature_type == feature:
                        if gene_end < gene_start:
                            print "Gene end < gene start error"
                            print gene_start, gene_end
                            exit(1)
                        else:
                            if strand == "+":
                                current_borders = [gene_end+left_border, gene_end+right_border]
                            elif strand == "-":
                                current_borders = [gene_start-right_border-1, gene_start-left_border-1]
                            else:
                                print "GFF strand error"
                                exit(1)
                            if current_borders[0] < 0 or current_borders[1] < 0:
                                print current_borders, contig_id
                            else:
                                new_row = '{}\t{}\t{}\t{}\t{}\t{}\n'.format(contig_id, current_borders[0], current_borders[1], count, score, strand)
                            output.write(new_row)
        output.close()
    gff_file.close()
    return bed_out_path

def create_logo_from_fasta(fasta_path, logo_path):
    sequences=[]
    for record in SeqIO.parse(fasta_path, "fasta"):
        seq = record.seq.upper()
        if "N" not in str(seq) and "Y" not in str(seq):
            sequences.append(seq)
    motif = motifs.create(sequences)
    motif.weblogo(logo_path)
    print "Logo is available in " + logo_path
    return 0

gff_path="/home/anna/bioinformatics/blasto/polyA_sites.gff"
in_fasta="/home/anna/bioinformatics/blasto/p57_DNA_scaffolds.fa"

bed_path = get_environs(gff_path, bed_out_path=False, left_border=-1, right_border=2, feature="PAS")

out_fasta=bed_path[:-3]+"fna"

bedtools_call = ['bedtools', 'getfasta', '-fi', in_fasta, '-bed', bed_path, '-fo', out_fasta, '-s']
call(bedtools_call)

logo_path = out_fasta[:-4]+"_logo"
create_logo_from_fasta(out_fasta, logo_path)
