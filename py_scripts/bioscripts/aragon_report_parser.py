#!/usr/bin/python
import os

def parse_aragorn_report(aragorn_report_path):
    tRNA_dict ={}
    with open(aragorn_report_path, 'r') as aragorn_file:
        cur_row = 0
        for row in aragorn_file:
            if "nucleotides in sequence" in row:
                if len(prev_row_array) > 1:
                    name = row.rstrip().split(" ")[0]
                    species = row.rstrip().split(" ")[1]
                else:
                    print "Error!"
                tRNA_dict[name] = {}
                tRNA_dict[name]["species"] = species
                cur_row = 1
            elif (row[-2::]==".\n"):
                if cur_row == 1:
                    print "tRNA!"
                    print row
                    cur_row > 0
                    tRNA_dict[name]["species"]["tRNAs"] = []

            elif (28 > cur_row > 1):
                cur_row
            else:
                prev_row_array = row.rstrip().split(" ")

def get_tRNAs(tRNA, aragorn_report_path):
    aragorn_results = []
    tRNA_row_numbers = []
    with open(aragorn_report_path, 'r') as aragorn_file:
        cur_row_number = 0
        for row in aragorn_file:
            aragorn_results.append(row)
            if ("tRNA-"+ tRNA) in row:
                tRNA_row_numbers.append(cur_row_number)
            cur_row_number += 1

    results = []
    for tRNA_row_number in tRNA_row_numbers:
        tRNA_rows = aragorn_results[tRNA_row_number-29 : tRNA_row_number + 3]
        tRNA_seq = ""
        for row in tRNA_rows:
            tRNA_seq += row
        results.append(tRNA_seq)
    return results


aragorn_dir = "/home/anna/bioinformatics/blasto_local/ciliates/ciliate_genomes/aragorn/reports/"

interest_tRNA = "Trp(cca)"
outpath = "/home/anna/bioinformatics/blasto_local/ciliates/ciliate_genomes/aragorn/trp_report.txt"

with open(outpath, "w") as outfile:
    for file in os.listdir(aragorn_dir):
        name = file[0:-24]
        print name
        outfile.write("\n" + name + "\n\n")
        results = get_tRNAs(interest_tRNA, aragorn_dir+file)
        print len(results)
        for tRNA in results:
            outfile.write(tRNA)

