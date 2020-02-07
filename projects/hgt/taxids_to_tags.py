#!python
from ete3 import NCBITaxa
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"

taxid_list_path="/home/anna/bioinformatics/diplonema/hgt/results_last/taxids_from_trees.txt"
taxid_set_path="/home/anna/bioinformatics/diplonema/hgt/results_last/taxids_set.txt"
def uniqueize_taxids(taxid_list_path, taxid_set_path):
    with open(taxid_list_path) as taxid_list_file, open(taxid_set_path,"w") as taxid_set_f:
        taxids = []
        seqids_without_taxid = []
        for line in taxid_list_file:
            seqid, taxid = line.rstrip().split("\t")
            if taxid == "0":
                seqids_without_taxid.append(seqid)
            else:
                taxids.append(int(taxid))
        taxids = list(set(taxids))
        taxids.sort()
        for taxid in taxids:
            taxid_set_f.write(str(taxid) + "\n")

def taxids_to_tags(taxid_path, outpath, ncbi_taxa):
    bacteria_taxid = 2
    diplonemid_taxid = 191814
    with open(taxid_path) as taxid_file, open(outpath,"w") as outfile:
        for line in taxid_file:
            taxid = int(line.rstrip())
            tag = "other"
            bad_taxids = [2005002]
            if (taxid not in bad_taxids) and (taxid < 2447898):
                lineage = ncbi_taxa.get_lineage(taxid)
                if bacteria_taxid in lineage:
                    tag = "bacteria"
                elif diplonemid_taxid in lineage:
                    tag = "diplonemid"
            else:
                entrez_handle = Entrez.efetch(db="taxonomy", id=taxid)
                data_parsed = Entrez.read(entrez_handle)
                lineage = data_parsed[0]["Lineage"].split("; ")
                lineage_len = len(lineage)
                if lineage_len > 1:
                    if lineage[1] == "Bacteria":
                        tag = "bacteria"
                    elif lineage_len > 3 :
                        if lineage[3] == "Diplonemea":
                            tag = "diplonemid"
            outfile.write(str(taxid)+"\t"+tag+"\n")

ncbi_taxa = NCBITaxa()

tag_outpath = "/home/anna/bioinformatics/diplonema/hgt/results_last/taxids_tags.tsv"
taxids_to_tags(taxid_set_path, tag_outpath, ncbi_taxa)

