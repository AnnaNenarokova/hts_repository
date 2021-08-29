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

def get_seqs_ncbi(ncbi_set):
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
            except:
                print ("Error in dic", dic)
    return ncbi_result_dict

diamond_path = "/Users/annanenarokova/work/myxo_local/smol_diamond_nr_normal.tsv"
qseqid_list = ["g8031.t1", "g13533.t1", "g6756.t1", "g13534.t1", "g13561.t1", "g12517.t1", "g5528.t1", "g4866.t1", "g14280.t1", "g4610.t1", "g14805.t1", "g12511.t1", "g803.t1", "g13020.t1", "g4207.t1", "g9721.t1", "g12712.t1", "g6898.t1", "g12950.t1", "g8569.t1", "g2194.t1", "g8402.t1", "g3066.t1", "g11341.t1", "g14859.t1", "g14858.t1", "g12827.t1", "g13451.t1", "g14579.t1", "g4108.t1", "g11168.t1", "g3710.t1", "g4076.t1", "g13547.t1", "g13597.t1", "g8999.t1", "g11688.t1", "g8844.t1", "g1860.t1", "g2627.t1", "g10185.t1", "g3149.t1", "g1719.t1", "g4774.t1", "g6007.t1", "g2849.t1", "g1721.t1", "g8789.t1", "g13261.t1", "g7632.t1", "g10017.t1", "g3729.t1", "g4065.t1", "g3715.t1", "g13550.t1", "g249.t1", "g716.t1", "g7368.t1", "g6850.t1", "g3241.t1", "g3242.t1", "g12170.t1", "g776.t1", "g6601.t1", "g13259.t1", "g14581.t1", "g11169.t1", "g254.t1", "g263.t1", "g13612.t1", "g13535.t1", "g8032.t1", "g4653.t1", "g5211.t1", "g4008.t1", "g7212.t1", "g13187.t1", "g13196.t1", "g14857.t1", "g2101.t1", "g6757.t1", "g11764.t1", "g5338.t1", "g5330.t1", "g7617.t1", "g9599.t1", "g13045.t1", "g9774.t1", "g4737.t1", "g9315.t1", "g9329.t1", "g14794.t1", "g13103.t1", "g10968.t1", "g8792.t1", "g12829.t1", "g11170.t1", "g359.t1"]
seq_dict, ncbi_set = add_diamond_qseqs(diamond_path, qseqid_list)
ncbi_result_dict = get_seqs_ncbi(ncbi_set)
