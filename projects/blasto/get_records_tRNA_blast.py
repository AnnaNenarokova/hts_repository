#!/usr/bin/python3
from Bio import SeqIO

def parse_blast_result(blast_report_path, outfmt_opts=False, delimeter=","):
    if not outfmt_opts:
        outfmt_opts = 'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'
    outfmt_opt_list = outfmt_opts.split(" ")
    blast_dict = {}
    with open(blast_report_path) as blast_f:
        header_line = True
        for line in blast_f:
            if header_line:
                header_line = False
            else:
                line_split = line.rstrip().split(delimeter)
                qseqid = line_split[outfmt_opt_list.index("qseqid")]
                sseqid = line_split[outfmt_opt_list.index("sseqid")]
                if sseqid not in blast_dict.keys():
                    blast_dict[sseqid] = []
                blast_dict[sseqid].append(qseqid)

    return blast_dict

def get_seqs_blast(blast_report_path, query_path, subject_path):

    blast_dict = parse_blast_result(blast_report_path)

    query_fasta_dict = {}
    for record in SeqIO.parse(query_path, "fasta"):
        record_id = record.id
        query_fasta_dict[record_id] = record

    seq_dict = {}
    for sseqid in blast_dict:
        seq_dict[sseqid] = []

    for record in SeqIO.parse(subject_path, "fasta"):
        sseqid = record.id
        if sseqid in seq_dict:
            seq_dict[sseqid].append(record)

    for sseqid in seq_dict:
        for qseqid in blast_dict[sseqid]:
            seq_dict[sseqid].append(query_fasta_dict[qseqid])

    return seq_dict

def write_blast_seqs(blast_report_path, query_path, subject_path, outfolder):
    seq_dict = get_seqs_blast(blast_report_path, query_path, subject_path)
    for sseqid in seq_dict:
        outpath = outfolder + sseqid + ".fasta"
        results = seq_dict[sseqid]
        SeqIO.write(results, outpath, "fasta")
    return 0

blast_report_path="/Users/anna/work/blasto_local/tRNA/tRNAseq/reference_RNAs_B_nonstop/blast_reports/p57_cyto_vsearch_out_aligned.fasta_bl_report_best.csv"
query_path="/Users/anna/work/blasto_local/tRNA/tRNAseq/p57_cyto_vsearch_out_aligned.fasta"
subject_path="/Users/anna/work/blasto_local/tRNA/tRNAseq/reference_RNAs_B_nonstop.fasta"
outfolder="/Users/anna/work/blasto_local/tRNA/tRNAseq/fasta_results_tRNAseq/"

write_blast_seqs(blast_report_path, query_path, subject_path, outfolder)