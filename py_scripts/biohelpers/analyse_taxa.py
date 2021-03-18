#!python3
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"
from encoder import XML2Dict

def read_diamond_result(diamond_taxa_result_path, outfmt_opts=False):
    if not outfmt_opts:
        outfmt_opts = "qseqid taxid evalue"
    outfmt_opt_list = outfmt_opts.split(" ")
    seq_dict = {}
    taxid_dict = {}
    with open(diamond_taxa_result_path) as diamond_f:
        for line in diamond_f:
            line_split = line.rstrip().split("\t")
            qseqid = line_split[outfmt_opt_list.index("qseqid")]
            taxid = line_split[outfmt_opt_list.index("taxid")]
            evalue = float(line_split[outfmt_opt_list.index("evalue")])
            seq_dict[qseqid] = {"taxid": taxid, "evalue": evalue}
            if taxid in taxid_dict:
                taxid_dict[taxid]["count"] += 1
            else:
                taxid_dict[taxid] = {}
                taxid_dict[taxid]["count"] = 1
    return taxid_dict, seq_dict

def add_lineages(taxid_dict):
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
    taxid_dict['0']["name"] = "none"
    taxid_dict['0']["lineage"] = "none"
    return taxid_dict

def get_taxid_dicts(diamond_taxa_result_path, outfmt_opts=False):
    taxid_dict, seq_dict = read_diamond_result(diamond_taxa_result_path, outfmt_opts)
    taxid_dict = add_lineages(taxid_dict)
    return taxid_dict, seq_dict

def write_taxid_report(taxid_dict, outpath): 
    with open(outpath, "w") as outfile:
        header = "taxid\tcount\tname\tlineage\n"
        outfile.write(header)
        for taxid in taxid_dict:
            count = taxid_dict[taxid]["count"]
            name = taxid_dict[taxid]["name"]
            lineage = taxid_dict[taxid]["lineage"]
            row = "{}\t{}\t{}\t{}\n".format(taxid,count,name,lineage)
            outfile.write(row)
    return outpath



