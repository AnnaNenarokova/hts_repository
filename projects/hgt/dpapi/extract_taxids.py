#!python3
import sys
sys.path.insert(0, "/Users/annanenarokova/work/code/ngs/")
from encoder import XML2Dict
from py_scripts.helpers.parse_csv import *
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"
def get_taxids_ncbi_proteins(protein_list):
    taxid_dict = {}
    ncbi_xml_record = Entrez.efetch(db="protein", id=protein_list, rettype="fasta", retmode="xml").read()
    ncbi_dict = XML2Dict().parse(ncbi_xml_record)
    ncbi_dict_list = ncbi_dict['TSeqSet']['TSeq']
    for record in ncbi_dict_list:
        if 'TSeq_accver' in record.keys():
            prot_id = record['TSeq_accver'].decode("utf-8")
            taxid = record['TSeq_taxid'].decode("utf-8")
            taxid_dict[prot_id] = taxid
        else:
            print ("KeyError: 'TSeq_accver' in the following record:")
            print (record)
    return taxid_dict

def extract_taxids_ncbi(diamond_path, staxids_opts=False, outfmt_opts=False, delimeter="\t"):
    if not outfmt_opts:
        outfmt_opts="qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore"
    outfmt_opt_list = outfmt_opts.split(" ")

    taxid_dict = {}
    empty_taxid_list = []
    with open(diamond_path) as diamond_file:
        for line in diamond_file:
            line_split = line.rstrip().split(delimeter)
            sseqid = line_split[outfmt_opt_list.index("sseqid")]
            if staxids_opts:
                staxids = line_split[outfmt_opt_list.index("staxids")]
                staxid = staxids.split(";")[0]
                taxid_dict[sseqid] = staxid
                if staxid == "":
                    empty_taxid_list.append(sseqid)
            else:
                empty_taxid_list.append(sseqid)

    other_taxids_dict = get_taxids_ncbi_proteins(empty_taxid_list)
    taxid_dict.update(other_taxids_dict)
    return taxid_dict

def extract_taxids_refset(diamond_path, refsetinfo_path, outfmt_opts=False):
    main_key = "new_id"
    refsetinfo_dict = csv_to_dict(refsetinfo_path, main_key)

    if not outfmt_opts:
        outfmt_opts="qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore"
    outfmt_opt_list = outfmt_opts.split(" ")
    sseqid_index = outfmt_opt_list.index("sseqid")
    taxid_dict = {}
    with open(diamond_path) as diamond_file:
        for line in diamond_file:
            line_split = line.rstrip().split("\t")
            sseqid = line_split[sseqid_index]
            taxid_dict[sseqid] = refsetinfo_dict[sseqid]["taxid"]
    return taxid_dict

def extract_taxids(nr_diamond_path, refset_diamond_path, refsetinfo_path, outpath, nr_outfmt_opts=False):
    taxid_dict = {}
    print ("Extracting taxids from the refset")
    refset_taxid = extract_taxids_refset(refset_diamond_path, refsetinfo_path)
    taxid_dict.update(refset_taxid)
    print ("Extracting taxids from the NCBI set")
    ncbi_taxid_dict = extract_taxids_ncbi(nr_diamond_path, staxids_opts=True, outfmt_opts=nr_outfmt_opts)
    taxid_dict.update(ncbi_taxid_dict)
    with open(outpath, 'w') as outfile:
        for seq in taxid_dict:
            outfile.write(seq + "\t" + taxid_dict[seq] + "\n")
    return outpath

nr_diamond_path = "/Users/annanenarokova/work/dpapi_local/dpapi_cand_nr_dmnd_tax.tsv"
nr_outfmt_opts = "qseqid qlen sseqid slen staxids length evalue bitscore"

refset_diamond_path = "/Users/annanenarokova/work/dpapi_local/dpapi_hgt_cand_refdataset_dmnd.tsv"
refsetinfo_path = "/Users/annanenarokova/work/dpapi_local/dpapi_full_dataset_info.csv"

outpath = "/Users/annanenarokova/work/dpapi_local/test_dmd_extracted_taxids.tsv"
extract_taxids(nr_diamond_path, refset_diamond_path, refsetinfo_path, outpath, nr_outfmt_opts=nr_outfmt_opts)
 