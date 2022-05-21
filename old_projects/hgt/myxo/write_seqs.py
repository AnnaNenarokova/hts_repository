#!python3
from Bio import SeqIO
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"

def get_ncbi_seqs(seqid_list):
    ncbi_record = Entrez.efetch(db="protein", id=seqid_list, rettype="fasta")
    seq_str = ncbi_record.read()
    return seq_str

def get_ncbi_taxids(seqid_list, outpath):
    return taxid_list

def get_hgt_cand_dict(hgt_cand_path, diamond_result_path, outfmt_opts):
    max_seqs = 20
    hgt_cand_list = []
    with open(hgt_cand_path) as hgt_cand_f:
        for line in hgt_cand_f:
            seqid = line.rstrip()
            hgt_cand_list.append(seqid)

    hgt_cand_dict = {}
    ncbi_seqid_list = []

    with open(diamond_result_path) as diamond_f:
        outfmt_opt_list = outfmt_opts.split(" ")
        for line in diamond_f:
            line_split = line.rstrip().split("\t")
            qseqid = line_split[outfmt_opt_list.index("qseqid")]
            sseqid = line_split[outfmt_opt_list.index("sseqid")]
            evalue = float(line_split[outfmt_opt_list.index("evalue")])
            if qseqid in hgt_cand_list:
                if qseqid in hgt_cand_dict.keys():
                    if count <= max_seqs:
                        hgt_cand_dict[qseqid].append(sseqid)
                        ncbi_seqid_list.append(sseqid)
                    count += 1
                else:
                    count = 0
                    hgt_cand_dict[qseqid] = [sseqid]
                    ncbi_seqid_list.append(sseqid)

    return hgt_cand_dict, ncbi_seqid_list

def write_seqs(in_fasta, hgt_cand_dict, outfolder):
    hgt_candidates = hgt_cand_dict.keys()

    for record in SeqIO.parse(in_fasta, "fasta"):
        seqid = record.id
        if seqid in hgt_candidates and len(hgt_cand_dict[seqid]) >= 4:
            outpath = outfolder + str(seqid) + ".faa"
            SeqIO.write(record, outpath, "fasta")
            ncbi_seqids = hgt_cand_dict[seqid]
            ncbi_str = get_ncbi_seqs(ncbi_seqids)
            with open(outpath, "a") as outfile:
                outfile.write(ncbi_str)
    return outfolder

hgt_cand_path = "/Users/annanenarokova/work/hgt/smol_vertebrate_hgt_candidates.txt"
diamond_result_path = "/Users/annanenarokova/work/hgt/smol_diamond_nr_normal.tsv"
outfmt_opts = "qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore"

in_fasta = "/Users/annanenarokova/work/hgt/augustus_6_annot_prot.faa"

outfolder = "/Users/annanenarokova/work/hgt/hgt_candidates_vertebrates/"

hgt_cand_dict, ncbi_seqid_list = get_hgt_cand_dict(hgt_cand_path, diamond_result_path, outfmt_opts)

write_seqs(in_fasta, hgt_cand_dict, outfolder)

