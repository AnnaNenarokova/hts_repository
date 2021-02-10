#!python3
import csv
def write_gene_ogs(og_path, outpath, name, delimiter):
    gene_delimeter = ", "
    og_dict = {}
    with open(og_path) as og_file:
        reader = csv.DictReader(og_file, delimiter=delimiter)
        for row in reader:
            og = row["Orthogroup"]
            genes = row[name].split(gene_delimeter)
            for gene in genes:
                if gene:
                    og_dict[gene] = og
    with open(outpath, "w") as out_f:
        out_f.write("id\tOG\n")
        for gene in sorted(list(og_dict.keys())):
            new_line = '{}\t{}\n'.format(gene, og_dict[gene])
            out_f.write(new_line)

    return outpath

og_path = "/Users/annanenarokova/work/myxo/orthogroups_smol.csv"
outpath = "/Users/annanenarokova/work/myxo/smol_genes_ogs.tsv"
delimiter = ";"
name = "Sphaerospora_molnari_G"

write_gene_ogs(og_path, outpath, name, delimiter)