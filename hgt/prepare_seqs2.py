#!python3
from Bio import SeqIO
from Bio import Entrez

diamond_result_path = "/projects/Diplonema_genome_evolution/hgt/dpapi_hgt_cand_diamond_euglenozoans.tsv"
infasta_path = "/projects/Diplonema_genome_evolution/hgt/dpapi_hgt_candidates.faa"
ref_fasta_path = "/home/shared/BANK/diplonema_dataset/euglenozoa_anzhelika/all_euglenozoans.faa"
outdir="/projects/Diplonema_genome_evolution/hgt/results/fasta2/"
outfmt_opts="qseqid qlen sseqid slen length evalue bitscore"

query_inlist=[
"DIPPA_01494.mRNA.1",
"DIPPA_02975.mRNA.1",
"DIPPA_03183.mRNA.1",
"DIPPA_06774.mRNA.1",
"DIPPA_08933.mRNA.1",
"DIPPA_08957.mRNA.1",
"DIPPA_10301.mRNA.1",
"DIPPA_14778.mRNA.1",
"DIPPA_15740.mRNA.1",
"DIPPA_15749.mRNA.1",
"DIPPA_22792.mRNA.1",
"DIPPA_22798.mRNA.1",
"DIPPA_25054.mRNA.1",
"DIPPA_29700.mRNA.1"
]




outfmt_opt_list = outfmt_opts.split(" ")

dpapi_seqs = {}
for record in SeqIO.parse(infasta_path, "fasta"):
    dpapi_seqs[record.id] = record

ref_seqs = {}
for record in SeqIO.parse(ref_fasta_path, "fasta"):
    ref_seqs[record.id] = record


with open(diamond_result_path) as diamond_f:
    current_qseqid = None
    i = 0
    for line in diamond_f:
        i += 1
        # print (i)
        line_split = line.rstrip().split("\t")
        qseqid = line_split[outfmt_opt_list.index("qseqid")]
        sseqid = line_split[outfmt_opt_list.index("sseqid")]
        evalue = float(line_split[outfmt_opt_list.index("evalue")])
        if qseqid in query_inlist:
            # taxid = line_split[outfmt_opt_list.index("staxids")]
            if qseqid != current_qseqid:
                print (current_qseqid)
                if current_qseqid:
                    SeqIO.write(records, current_path, "fasta")
                current_qseqid = qseqid
                current_path = outdir + current_qseqid + ".faa"
                records = [dpapi_seqs[qseqid]]
                print (current_path)
            ref_record = ref_seqs[sseqid]
            records.append(ref_record)