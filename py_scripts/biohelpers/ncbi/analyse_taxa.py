#!python3
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"
from encoder import XML2Dict

def read_diamond_result(diamond_taxa_result_path, outfmt_opts=False):
    if not outfmt_opts:
        outfmt_opts = "qseqid taxid evalue"
    outfmt_opt_list = outfmt_opts.split(" ")
    seq_tax_dict = {}
    taxid_set = set()
    with open(diamond_taxa_result_path) as diamond_f:
        for line in diamond_f:
            line_split = line.rstrip().split("\t")
            qseqid = line_split[outfmt_opt_list.index("qseqid")]
            taxid = line_split[outfmt_opt_list.index("taxid")]
            evalue = float(line_split[outfmt_opt_list.index("evalue")])
            seq_tax_dict[qseqid] = {"taxid": taxid, "evalue": evalue}
            taxid_set.add(taxid)
    return taxid_set, seq_tax_dict

def get_taxid_set(seq_taxid_dict):
    taxid_set = set()
    for seqid in seq_taxid_dict:
        taxid_set.add(seq_taxid_dict[seqid])
    return taxid_set

def get_lineages_bulk(taxid_list):
    ncbi_xml_record = Entrez.efetch(db="taxonomy", id=taxid_list).read()
    ncbi_dict = XML2Dict().parse(ncbi_xml_record)
    taxa_dict_list = ncbi_dict['TaxaSet']['Taxon']
    taxid_dict = {}
    for taxon in taxa_dict_list:
        taxid = taxon['TaxId'].decode("utf-8")
        name = taxon['ScientificName'].decode("utf-8")
        try:
            lineage = taxon['Lineage'].decode("utf-8")
        except:
            lineage = taxon['Lineage']
        taxid_dict[taxid] = {}
        taxid_dict[taxid]["name"] = name
        taxid_dict[taxid]["lineage"] = lineage
    return taxid_dict

def get_lineages_singly(taxid_set):
    taxid_dict = {}
    for taxid in taxid_set:
        if taxid == "0":
            taxid_dict[taxid] = { "lineage" : "", "name" : "" }
        else:
            ncbi_xml_record = Entrez.efetch(db="taxonomy", id=taxid).read()
            ncbi_dict = XML2Dict().parse(ncbi_xml_record)
            taxon = ncbi_dict['TaxaSet']['Taxon']
            name = taxon['ScientificName'].decode("utf-8")
            try:
                lineage = taxon['Lineage'].decode("utf-8")
            except:
                lineage = taxon['Lineage']
            taxid_dict[taxid] = { "lineage" : lineage, "name" : name }
    return taxid_dict

def get_taxid_dict(taxid_list):
    taxid_set = set(taxid_list)
    taxid_list = list(taxid_list)

    print ("Getting lineages")
    taxid_dict = get_lineages_bulk(taxid_list)
    taxid_dict_set = set(taxid_dict.keys())

    not_in_taxids_set = taxid_set - taxid_dict_set
    missing_taxid_dict = get_lineages_singly(not_in_taxids_set)

    taxid_dict.update(missing_taxid_dict)
    return taxid_dict

def get_taxid_dicts(diamond_taxa_result_path, outfmt_opts=False):
    taxid_set, seq_tax_dict = read_diamond_result(diamond_taxa_result_path, outfmt_opts)
    taxid_dict = get_taxid_dict(taxid_set)
    return taxid_dict, seq_tax_dict

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

def get_seq_lineages(diamond_taxa_result_path, outfmt_opts=False):
    taxid_dict, seq_tax_dict = get_taxid_dicts(diamond_taxa_result_path, outfmt_opts=outfmt_opts)
    for seqid in seq_tax_dict:
        taxid = seq_tax_dict[seqid]["taxid"]
        if taxid in taxid_dict.keys():
            lineage = taxid_dict[taxid]["lineage"]
        else:
            print (taxid, "is not in the taxid_dict keys!")
            lineage = ""
        seq_tax_dict[seqid]["lineage"] = lineage
    return seq_tax_dict

def write_lineages(diamond_taxa_result_path, outpath, outfmt_opts=False):
    taxid_dict, seq_tax_dict = get_taxid_dicts(diamond_taxa_result_path, outfmt_opts=outfmt_opts)
    with open(outpath, "w") as outfile:
        for seqid in seq_tax_dict:
            taxid = seq_tax_dict[seqid]["taxid"]
            if taxid in taxid_dict.keys():
                lineage = taxid_dict[taxid]["lineage"]
            else:
                print (taxid, "is not in the taxid_dict keys!")
                lineage = ""
            outfile.write(seqid + "\t" + lineage + "\n")
    return 0
