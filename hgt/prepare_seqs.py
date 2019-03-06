#!python3
from Bio import SeqIO
from Bio import Entrez
Entrez.email = "a.nenarokova@gmail.com"

diamond_result_path = "/projects/Diplonema_genome_evolution/hgt/hgt_nr_diamond_0e.tsv"
infasta_path = "/projects/Diplonema_genome_evolution/hgt/dpapi_hgt_candidates.faa"
outfmt_opts="qseqid qlen sseqid slen staxids length evalue bitscore"
outdir="/projects/Diplonema_genome_evolution/hgt/results/fasta/"

dpapi_seqs = {}
for record in SeqIO.parse(infasta_path, "fasta"):
	dpapi_seqs[record.id] = record

with open(diamond_result_path) as diamond_f:
	current_qseqid = None
	current_f = None

    for line in diamond_f:
        line_split = line.rstrip().split("\t")
        qseqid = line_split[outfmt_opt_list.index("qseqid")]
        sseqid = line_split[outfmt_opt_list.index("sseqid")]
        taxid = line_split[outfmt_opt_list.index("staxids")]
        evalue = float(line_split[outfmt_opt_list.index("evalue")])
        
        if qseqid != current_qseqid:
        	if current_f: current_f.close()
        	current_qseqid = qseqid
        	current_path = outdir + current_qseqid + ".faa"
        	dpapi_record = [dpapi_seqs[qseqid]]
        	SeqIO.write(dpapi_record, current_path, "fasta")
        	current_f = current_path.open("a")
		ncbi_record = Entrez.efetch(db="protein", id=sseqid, rettype="fasta")
		current_f.write(ncbi_record)
		# handle = Entrez.efetch(db="protein", id="WP_014997480.1", rettype="fasta")
	current_f.close()