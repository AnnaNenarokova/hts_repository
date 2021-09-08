#!python3
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"
from encoder import XML2Dict

def get_taxid_dict(taxid_path):
    taxid_dict = {}
    with open(taxid_path) as taxid_file:
        for line in taxid_file:
            taxid = line.strip()
            taxid_dict[taxid] = {}
    return taxid_dict

def add_lineages_taxid_dict(taxid_dict):
    taxids = list(taxid_dict.keys())

    ncbi_xml_record = Entrez.efetch(db="taxonomy", id=taxids).read()

    ncbi_dict = XML2Dict().parse(ncbi_xml_record)

    taxa_dict_list = ncbi_dict['TaxaSet']['Taxon']

    for taxon in taxa_dict_list:
        taxid = taxon['TaxId'].decode("utf-8")
        name = taxon['ScientificName'].decode("utf-8")
        try:
            lineage = taxon['Lineage'].decode("utf-8")
        except:
            lineage = taxon['Lineage']
        taxid_dict[taxid]["name"] = name
        taxid_dict[taxid]["lineage"] = lineage
    return taxid_dict

def write_taxid_report(taxid_dict, outpath): 
    with open(outpath, "w") as outfile:
        header = "taxid\tname\tlineage\n"
        outfile.write(header)
        for taxid in taxid_dict:
            name = taxid_dict[taxid]["name"]
            lineage = taxid_dict[taxid]["lineage"]
            row = "{}\t{}\t{}\n".format(taxid,name,lineage)
            outfile.write(row)
    return outpath

def add_lineages(taxid_path, outpath):
    taxid_dict = get_taxid_dict(taxid_path)
    taxid_dict = add_lineages_taxid_dict(taxid_dict)
    write_taxid_report(taxid_dict, outpath)
    return 0

taxid_path = '/Users/annanenarokova/work/hypsa_local/jana_m/ref_proteomes/taxid_list.tsv'
outpath = '/Users/annanenarokova/work/hypsa_local/jana_m/ref_proteomes/taxids_lineages.tsv'

add_lineages(taxid_path, outpath)
