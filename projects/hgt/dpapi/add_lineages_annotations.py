#!python3
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"
from encoder import XML2Dict

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

def get_annotations_ncbi(ncbi_set):
    ncbi_annotation_dict = {}
    ncbi_full_list = list(ncbi_set)
    chunk_size = 1000
    chunk_number = (len(ncbi_full_list) // chunk_size) + 1
    i = 0 
    for ncbi_list in chunks(ncbi_full_list, chunk_size):
        i += 1
        print (f"Chunk {i} out of {chunk_number} is being processed")
        ncbi_record = Entrez.efetch(db="protein", id=ncbi_list, rettype="fasta", retmode="xml")
        print ("Reading NCBI XML")
        ncbi_xml_record = ncbi_record.read()
        print ("Parcing NCBI result")
        ncbi_dict_list = XML2Dict().parse(ncbi_xml_record)['TSeqSet']['TSeq']
        if type(ncbi_dict_list) == dict:
            ncbi_dict_list = [ncbi_dict_list]
        print ("Adding NCBI sequences")
        for dic in ncbi_dict_list:
            try:
                keys = dic.keys()
                if 'TSeq_accver' in keys:
                    try:
                        seqid = dic['TSeq_accver'].decode("utf-8")
                    except:
                        seqid = dic['TSeq_accver']
                elif 'TSeq_sid' in keys:
                    try:
                        seqid = dic['TSeq_sid'].decode("utf-8")
                    except:
                        seqid = dic['TSeq_sid']
                else:
                    print ("Error in the following dict")
                    print (dic)
                try:
                    ncbi_annotation_dict[seqid] = dic['TSeq_defline'].decode("utf-8")
                except:
                    ncbi_annotation_dict[seqid] = dic['TSeq_defline']
            except:
                print ("Error in dic", dic)
    return ncbi_annotation_dict

