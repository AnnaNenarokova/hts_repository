#!/usr/bin/python3
from Bio import pairwise2
from Bio import AlignIO
from Bio import SeqIO

def align_mulitiple_pairwise(ref_fasta, fasta_to_align, outfile):
	ref_fasta_record = SeqIO.read(ref_fasta, "fasta")
	refseq = str(ref_fasta_record.seq)
	for record in SeqIO.parse(fasta_to_align, "fasta"):
		seq = str(record.seq)
		print(pairwise2.align.localms(refseq, seq, 2, -1, -5, -0, one_alignment_only=True))

	return outfile


ref_fasta="/Users/anna/work/blasto_local/tRNA/tRNAseq/tRNA_Trp_cca_Blastocrithidia_nonstop.fasta"
fasta_to_align="/Users/anna/work/blasto_local/tRNA/tRNAseq/p57_Trp_aligned_clusters.fasta"
outfile="/Users/anna/work/blasto_local/tRNA/tRNAseq/p57_Trp_aligned_clusters_aligned.fasta"

align_mulitiple_pairwise(ref_fasta, fasta_to_align, outfile)