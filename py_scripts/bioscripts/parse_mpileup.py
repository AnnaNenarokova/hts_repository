#!/usr/bin/python
def parse_mpileup_file(mpileup_path):
    with open(mpileup_path, 'r') as mpileup_file:
        cov_per_position = {}
        for row in mpileup_file:
            split_row = row.split('\t')
            contig_id = split_row[0]
            position = split_row[1]
            coverage = split_row[3]

            if contig_id not in cov_per_position.keys():
                cov_per_position[contig_id]=[]
            cov_per_position[contig_id].append([position, coverage])
    mpileup_file.close()
    return cov_per_position
