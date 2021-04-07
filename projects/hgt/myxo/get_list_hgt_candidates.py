#!python3
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"
from encoder import XML2Dict

def read_diamond_result(diamond_taxa_result_path, outfmt_opts):
    outfmt_opt_list = outfmt_opts.split(" ")
    taxid_dict = {}
    with open(diamond_taxa_result_path) as diamond_f:
        for line in diamond_f:
            line_split = line.rstrip().split("\t")
            qseqid = line_split[outfmt_opt_list.index("qseqid")]
            taxid = line_split[outfmt_opt_list.index("taxid")]
            evalue = float(line_split[outfmt_opt_list.index("evalue")])
            if taxid in taxid_dict:
                taxid_dict[taxid]["count"] += 1
                taxid_dict[taxid]["seqs"].append(qseqid)
            else:
                taxid_dict[taxid] = {}
                taxid_dict[taxid]["count"] = 1
                taxid_dict[taxid]["seqs"] = [qseqid]
    return taxid_dict

def add_lineages(taxid_dict):
    taxids = list(taxid_dict.keys())
    # print (taxids)

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

def get_taxid_dict(diamond_taxa_result_path, outfmt_opts):
    taxid_dict = read_diamond_result(diamond_taxa_result_path, outfmt_opts)
    taxid_dict = add_lineages(taxid_dict)
    return taxid_dict

def select_seqs(taxid_dict, name, outpath):
	seq_list = []
	for taxid in taxid_dict:
		if name in taxid_dict[taxid]["lineage"]:
			seq_list.extend(taxid_dict[taxid]["seqs"])

	with open(outpath, "w") as outfile:
	    for seq in seq_list:
	        outfile.write(seq + '\n')
 
	return seq_list

diamond_taxa_result_path = "/Users/annanenarokova/work/dpapi_local/dpapi_recoded_nr_tax.tsv"
outfmt_opts = "qseqid taxid evalue"
name = "Bacteria"
outpath = "/Users/annanenarokova/work/dpapi_local/dpapi_recorded_hgt_cands.txt"

taxid_dict = get_taxid_dict(diamond_taxa_result_path, outfmt_opts)
select_seqs(taxid_dict, name, outpath)

