#!python3
from encoder import XML2Dict
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"
import sys
sys.path.insert(0, "/Users/annanenarokova/work/code/ngs/")
from projects.hgt.common.seqids_to_tags import *

def add_diamond_result(diamond_path, outfmt_opts, seq_dict, ncbi=False, delimeter="\t"):
    if not outfmt_opts:
        outfmt_opts="qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore"
    outfmt_opt_list = outfmt_opts.split(" ")
    subj_set = set()
    with open(diamond_path) as diamond_f:
        for line in diamond_f:
            line_split = line.rstrip().split(delimeter)
            qseqid = line_split[outfmt_opt_list.index("qseqid")]
            sseqid = line_split[outfmt_opt_list.index("sseqid")]
            evalue = float(line_split[outfmt_opt_list.index("evalue")])
            bitscore = float(line_split[outfmt_opt_list.index("bitscore")])
            subj_set.add(sseqid)
            if qseqid not in seq_dict.keys():
                seq_dict[qseqid] = {"ncbi":{}, "refset":{}}
            sseqid_dict = {}
            if ncbi:
                seq_dict[qseqid]["ncbi"][sseqid] = {"sseqid": sseqid, "evalue": evalue, "bitscore": bitscore}
            else:
                seq_dict[qseqid]["refset"][sseqid] = {"sseqid": sseqid, "evalue": evalue, "bitscore": bitscore}
    return seq_dict, subj_set

def group_seq_dict(seq_dict):
    used_dpapi_ids = set()
    new_seq_dict = {}
    for qseqid in seq_dict:
        refset = set(seq_dict[qseqid]["refset"])
        ncbi_set = set(seq_dict[qseqid]["ncbi"])
        if qseqid in used_dpapi_ids:
            for key in new_seq_dict:
                if qseqid in new_seq_dict[key]["refset"]:
                    new_seq_dict[key]["refset"].update(refset)
                    new_seq_dict[key]["ncbi"].update(ncbi_set)
        else:
            used_dpapi_ids.add(qseqid)
            new_seq_dict[qseqid] = {"ncbi": ncbi_set, "refset": refset}
        for seqid in refset:
            if "EEDDpapign" in seqid:
                used_dpapi_ids.add(seqid)
    return new_seq_dict

def filter_refset_dict(seq_dict, keep_number=20, filter_key="bitscore"):
    for qseqid in seq_dict:
        other_dict_list = []
        refset = seq_dict[qseqid]["refset"]
        for sseqid in refset:
            if "EEDDpapign" not in sseqid:
                other_dict_list.append(refset[sseqid])
        other_dict_list = sorted(other_dict_list, key = lambda i: i[filter_key])
        remove_list = other_dict_list[::keep_number]
        for dic in remove_list:
            sseqid = dic["sseqid"]
            del seq_dict[qseqid]['refset'][sseqid]
    return seq_dict

def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

def get_seqs_ncbi(ncbi_set):
    taxid_dict = {}
    ncbi_result_dict = {}
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
                if 'TSeq_taxid' in keys:
                    try:
                        taxid = dic['TSeq_taxid'].decode("utf-8")
                    except:
                        taxid = dic['TSeq_taxid']
                else:
                    print ("No taxid in the following dict")
                    print (dic)
                try:
                    seq = dic['TSeq_sequence'].decode("utf-8")
                except:
                    seq = dic['TSeq_sequence']
                ncbi_result_dict[seqid] = seq
                taxid_dict[seqid] = taxid
            except:
                print ("Error in dic", dic)
    return ncbi_result_dict, taxid_dict

def get_seqs_refset(ref_set, ref_fasta_path):
    refset_dict = {}
    i = 0
    for record in SeqIO.parse(ref_fasta_path, "fasta"):
        if i % 100000 == 0:
            print (i)
        i += 1
        record_id = record.id
        if record_id in ref_set:
            refset_dict[record_id] = record
    return refset_dict

def combine_seq_dicts(seq_dict, ncbi_result_dict, refset_dict):
    for qseqid in seq_dict:
        refseq_ids = seq_dict[qseqid]['refset']
        seq_dict[qseqid]['refset'] = {}
        for refseq_id in refseq_ids:
            seq_dict[qseqid]['refset'][refseq_id] = refset_dict[refseq_id]
        ncbi_ids = seq_dict[qseqid]['ncbi']
        seq_dict[qseqid]['ncbi'] = {}
        bad_ncbi_ids = []
        for ncbi_id in ncbi_ids:
            try:
                if ncbi_id in ncbi_result_dict.keys():
                    key = ncbi_id
                else:
                    print (f"No ncbi_id {ncbi_id} in ncbi_result_dict, accessing NCBI")
                    ncbi_set = {ncbi_id}
                    ncbi_dict, taxid_dict = get_seqs_ncbi(ncbi_set)
                    key = list(ncbi_dict.keys())[0]
                seq = Seq(ncbi_result_dict[key])
                seq_record = SeqRecord(seq=seq, id=ncbi_id, description='')
                seq_dict[qseqid]['ncbi'][ncbi_id] = seq_record
            except:
                print (f"Can not get output for ncbi_id {ncbi_id}, will remove the element")
                bad_ncbi_ids.append(ncbi_id)
    return seq_dict

def check_dicts(seq_dict, ncbi_result_dict):
    bad_ncbi_set = set()
    for qseqid in seq_dict:
        ncbi_ids = seq_dict[qseqid]['ncbi'].keys()
        for ncbi_id in ncbi_ids:
            if ncbi_id not in ncbi_result_dict.keys():
                bad_ncbi_set.add(ncbi_id)
    return bad_ncbi_set

def write_seqs(outfolder, seq_dict):
    i = 0
    for qseqid in seq_dict:
        i += 1
        if i % 100 == 0:
            print (i)
        outpath = outfolder + qseqid + ".faa"
        results = []
        for seq_subdict in (seq_dict[qseqid]['ncbi'], seq_dict[qseqid]['refset']):
            for seqid in seq_subdict:
                results.append(seq_subdict[seqid])
        SeqIO.write(results, outpath, "fasta")
    print ("Writing finished")
    return 0

def write_seq_tags(seq_taxid_dict, tag_path, tag_list):
    taxid_set = get_taxid_set(seq_taxid_dict)
    taxid_set_list = list(taxid_set)
    chunk_size = 1000
    chunk_number = (len(taxid_set_list) // chunk_size) + 1
    taxid_dict = {}
    i = 0
    for ncbi_list in chunks(taxid_set_list, chunk_size):
        i += 1
        print (f"Chunk {i} out of {chunk_number} is being processed")
        taxid_dict_new = get_taxid_dict(ncbi_list)
        taxid_dict.update(taxid_dict_new)
    taxid_tag_dict = taxids_to_tags(taxid_dict, tag_list)
    print ("Writing down the results")
    write_tags(seq_taxid_dict, taxid_tag_dict, tag_path)
    return outpath

ref_fasta_path = "/Users/annanenarokova/work/dpapi_local/dpapi_full_dataset.faa"

diamond_ref_path = "/Users/annanenarokova/work/dpapi_local/results_16_08/dpapi_recoded_cand_refset_dmnd.tsv"
ref_outfmt_opts = "qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore"

diamond_ncbi_path = "/Users/annanenarokova/work/dpapi_local/results_16_08/dpapi_recoded_cand_nr_dmnd_tax_50.tsv"
ncbi_outfmt_opts = "qseqid qlen sseqid slen staxids length evalue bitscore"

outfolder = "/Users/annanenarokova/work/dpapi_local/results_16_08/fasta/"

tag_path = "/Users/annanenarokova/work/dpapi_local/results_16_08/ncbi_tags.tsv"

seq_dict = {}

print ("Reading refset diamond")
seq_dict, ref_set = add_diamond_result(diamond_ref_path, ref_outfmt_opts, seq_dict, ncbi=False)
print (f"Refset diamond dataset length is {len(ref_set)}")

print ("Reading ncbi diamond results")
seq_dict, ncbi_set = add_diamond_result(diamond_ncbi_path, ncbi_outfmt_opts, seq_dict, ncbi=True)
print (f"NCBI diamond dataset length is {len(ncbi_set)}")

seq_dict = group_seq_dict(seq_dict)

print ("Adding sequences from refset")
refset_dict = get_seqs_refset(ref_set, ref_fasta_path)

print ("Adding sequences from ncbi")
ncbi_result_dict, seq_taxid_dict = get_seqs_ncbi(ncbi_set)

tag_list = ["Bacteria", "Diplonemea"]
print ("Writing down seq tags for ncbi")
write_seq_tags(seq_taxid_dict, tag_path, tag_list)

print ("Combining sequences")
seq_dict = combine_seq_dicts(seq_dict, ncbi_result_dict, refset_dict)

print("Writing fasta files")
write_seqs(outfolder, seq_dict)
