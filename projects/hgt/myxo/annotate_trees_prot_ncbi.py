#!python3
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"
from encoder import XML2Dict

def get_lineages_bulk(seqids):
    ncbi_xml_record = Entrez.efetch(db="protein", id=seqids, retmode="xml").read()
    ncbi_dict = XML2Dict().parse(ncbi_xml_record)
    records = ncbi_dict['GBSet']['GBSeq']
    lineages = {}
    for record in records:
        name = record['GBSeq_accession-version']
        lineage = record['GBSeq_taxonomy']

        try:
            lineage = lineage.decode("utf-8")
        except:
            lineage = lineage

        try:
            name = name.decode("utf-8")
        except:
            name = name
        lineages[name] = lineage
    return lineages


def annotate_tree(tree):
	return annotated_tree