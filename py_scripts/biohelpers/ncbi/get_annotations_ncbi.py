#!python3
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"
from encoder import XML2Dict

def add_diamond_qseqs(diamond_path, qseqid_list, outfmt_opts=False, delimeter="\t"):
    if not outfmt_opts:
        outfmt_opts="qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore"
    outfmt_opt_list = outfmt_opts.split(" ")
    subj_set = set()
    seq_dict = {}
    with open(diamond_path) as diamond_f:
        for line in diamond_f:
            line_split = line.rstrip().split(delimeter)
            qseqid = line_split[outfmt_opt_list.index("qseqid")]
            sseqid = line_split[outfmt_opt_list.index("sseqid")]
            evalue = float(line_split[outfmt_opt_list.index("evalue")])
            bitscore = float(line_split[outfmt_opt_list.index("bitscore")])
            if qseqid in qseqid_list:
                subj_set.add(sseqid)
                if qseqid not in seq_dict.keys():
                    seq_dict[qseqid] = {}
                seq_dict[qseqid][sseqid] = {"sseqid": sseqid, "evalue": evalue, "bitscore": bitscore}
    return seq_dict, subj_set

def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

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

def write_results(seq_dict, ncbi_annotation_dict, outpath):
    with open(outpath, "w") as outfile:
        header = "qseqid\tannotations\n"
        outfile.write(header)

        for qseqid in seq_dict:
            subject_dict = seq_dict[qseqid]
            sorted_subject_dicts = sorted(subject_dict.values(), key=lambda x: x['evalue'])
            annotations = []
            for subject_dict in sorted_subject_dicts:
                sseqid = subject_dict["sseqid"]
                if sseqid in ncbi_annotation_dict.keys():
                    annotation = ncbi_annotation_dict[subject_dict["sseqid"]]
                    annotations.append(annotation)
                else:
                    print (f"{sseqid} is not in the annotation dict")
            annotation_string = "; ".join(annotations)
            result = f"{qseqid}\t{annotation_string}\n"
            outfile.write(result)
    return outpath

diamond_path = "/Users/annanenarokova/work/dpapi_local/results_16_08/dpapi_recoded_cand_nr_dmnd_tax_50.tsv"
qseqid_list = ["EEDDpapign_Diplonema-papillatum_17035","EEDDpapign_Diplonema-papillatum_32141","EEDDpapign_Diplonema-papillatum_02771","EEDDpapign_Diplonema-papillatum_05031","EEDDpapign_Diplonema-papillatum_15881","EEDDpapign_Diplonema-papillatum_21885","EEDDpapign_Diplonema-papillatum_21887","EEDDpapign_Diplonema-papillatum_21892","EEDDpapign_Diplonema-papillatum_21897","EEDDpapign_Diplonema-papillatum_21899","EEDDpapign_Diplonema-papillatum_21904","EEDDpapign_Diplonema-papillatum_26772","EEDDpapign_Diplonema-papillatum_05872","EEDDpapign_Diplonema-papillatum_08089","EEDDpapign_Diplonema-papillatum_08091","EEDDpapign_Diplonema-papillatum_08092","EEDDpapign_Diplonema-papillatum_11044","EEDDpapign_Diplonema-papillatum_11074","EEDDpapign_Diplonema-papillatum_11071","EEDDpapign_Diplonema-papillatum_24491","EEDDpapign_Diplonema-papillatum_10852","EEDDpapign_Diplonema-papillatum_01800","EEDDpapign_Diplonema-papillatum_01995","EEDDpapign_Diplonema-papillatum_07911","EEDDpapign_Diplonema-papillatum_08442","EEDDpapign_Diplonema-papillatum_09163","EEDDpapign_Diplonema-papillatum_11676","EEDDpapign_Diplonema-papillatum_14727","EEDDpapign_Diplonema-papillatum_14728","EEDDpapign_Diplonema-papillatum_14729","EEDDpapign_Diplonema-papillatum_14730","EEDDpapign_Diplonema-papillatum_14731","EEDDpapign_Diplonema-papillatum_17083","EEDDpapign_Diplonema-papillatum_24648","EEDDpapign_Diplonema-papillatum_00972","EEDDpapign_Diplonema-papillatum_02716","EEDDpapign_Diplonema-papillatum_03735","EEDDpapign_Diplonema-papillatum_04230","EEDDpapign_Diplonema-papillatum_04707","EEDDpapign_Diplonema-papillatum_05014","EEDDpapign_Diplonema-papillatum_05019","EEDDpapign_Diplonema-papillatum_05022","EEDDpapign_Diplonema-papillatum_05721","EEDDpapign_Diplonema-papillatum_06631","EEDDpapign_Diplonema-papillatum_07137","EEDDpapign_Diplonema-papillatum_09616","EEDDpapign_Diplonema-papillatum_05328","EEDDpapign_Diplonema-papillatum_05334","EEDDpapign_Diplonema-papillatum_05389","EEDDpapign_Diplonema-papillatum_08123","EEDDpapign_Diplonema-papillatum_08126","EEDDpapign_Diplonema-papillatum_10125","EEDDpapign_Diplonema-papillatum_23584","EEDDpapign_Diplonema-papillatum_07404","EEDDpapign_Diplonema-papillatum_10105","EEDDpapign_Diplonema-papillatum_10122","EEDDpapign_Diplonema-papillatum_10774","EEDDpapign_Diplonema-papillatum_15638","EEDDpapign_Diplonema-papillatum_17187","EEDDpapign_Diplonema-papillatum_16308","EEDDpapign_Diplonema-papillatum_16431","EEDDpapign_Diplonema-papillatum_17437","EEDDpapign_Diplonema-papillatum_20609","EEDDpapign_Diplonema-papillatum_26974","EEDDpapign_Diplonema-papillatum_24060","EEDDpapign_Diplonema-papillatum_24360","EEDDpapign_Diplonema-papillatum_24659","EEDDpapign_Diplonema-papillatum_27327","EEDDpapign_Diplonema-papillatum_28315","EEDDpapign_Diplonema-papillatum_28811","EEDDpapign_Diplonema-papillatum_28812","EEDDpapign_Diplonema-papillatum_31245","EEDDpapign_Diplonema-papillatum_31225","EEDDpapign_Diplonema-papillatum_31226","EEDDpapign_Diplonema-papillatum_31250","EEDDpapign_Diplonema-papillatum_33302","EEDDpapign_Diplonema-papillatum_15337","EEDDpapign_Diplonema-papillatum_15379","EEDDpapign_Diplonema-papillatum_17883","EEDDpapign_Diplonema-papillatum_17884","EEDDpapign_Diplonema-papillatum_02209","EEDDpapign_Diplonema-papillatum_11076","EEDDpapign_Diplonema-papillatum_28819","EEDDpapign_Diplonema-papillatum_22187","EEDDpapign_Diplonema-papillatum_09336","EEDDpapign_Diplonema-papillatum_01811","EEDDpapign_Diplonema-papillatum_04074","EEDDpapign_Diplonema-papillatum_07173","EEDDpapign_Diplonema-papillatum_29037","EEDDpapign_Diplonema-papillatum_32902","EEDDpapign_Diplonema-papillatum_00188","EEDDpapign_Diplonema-papillatum_11905","EEDDpapign_Diplonema-papillatum_03293","EEDDpapign_Diplonema-papillatum_03093","EEDDpapign_Diplonema-papillatum_14399","EEDDpapign_Diplonema-papillatum_16571","EEDDpapign_Diplonema-papillatum_31799","EEDDpapign_Diplonema-papillatum_16886","EEDDpapign_Diplonema-papillatum_16887","EEDDpapign_Diplonema-papillatum_16896","EEDDpapign_Diplonema-papillatum_16899","EEDDpapign_Diplonema-papillatum_06622","EEDDpapign_Diplonema-papillatum_11289","EEDDpapign_Diplonema-papillatum_16239","EEDDpapign_Diplonema-papillatum_16245","EEDDpapign_Diplonema-papillatum_16247","EEDDpapign_Diplonema-papillatum_16249","EEDDpapign_Diplonema-papillatum_22607","EEDDpapign_Diplonema-papillatum_22630","EEDDpapign_Diplonema-papillatum_29039","EEDDpapign_Diplonema-papillatum_10165","EEDDpapign_Diplonema-papillatum_13091","EEDDpapign_Diplonema-papillatum_22007","EEDDpapign_Diplonema-papillatum_29034","EEDDpapign_Diplonema-papillatum_29525","EEDDpapign_Diplonema-papillatum_00219","EEDDpapign_Diplonema-papillatum_31935"]
ncbi_outfmt_opts = "qseqid qlen sseqid slen staxids length evalue bitscore"

outpath = "/Users/annanenarokova/work/dpapi_local/results_16_08/annotations_ncbi.tsv"
seq_dict, ncbi_set = add_diamond_qseqs(diamond_path, qseqid_list, outfmt_opts=ncbi_outfmt_opts)
ncbi_annotation_dict = get_annotations_ncbi(ncbi_set)
write_results(seq_dict, ncbi_annotation_dict, outpath)