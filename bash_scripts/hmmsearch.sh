#!/bin/bash
hmmsearch="/home/anna/bioinformatics/tools/hmmer-3.1b2-linux-intel-x86_64/binaries/hmmsearch"


# subject="/media/anna/data/anna_drive/projects/mitoproteomes/euglena/mitogenome/LQMU01_orfs_50aa.faa"
# pfam_hits="/media/anna/data/anna_drive/projects/mitoproteomes/euglena/mitogenome/ND_hmm/hmmsearch_reports/COG0377_hmm_NUOB_LQMU01_orfs_50aa.txt"

subject1="/home/anna/bioinformatics/euglena/LQMU01_orfs_50aa.faa"
subject2="/home/anna/bioinformatics/euglena/E_gracilis_transcriptome_final.PROTEINS.fasta"

output_dir="/home/anna/bioinformatics/euglena/ND_hmm/"

hmm="/home/anna/bioinformatics/euglena/ND_hmm/ncbi_tryps/atp6_tryp.hmm"
hmm="/home/anna/bioinformatics/euglena/ND_hmm/ncbi_tryps/nd2_tryp.hmm"
hmm="/home/anna/bioinformatics/euglena/ND_hmm/ncbi_tryps/nd3_tryp.hmm"



pfam_hits1=$output_dir"LQMU01_orfs_50aa_hmm_atp6_tryp.txt"
pfam_hits2=$output_dir"E_gracilis_PROTEINS_hmm_atp6_tryp.txt"
$hmmsearch --pfamtblout $pfam_hits1 $hmm $subject1
$hmmsearch --pfamtblout $pfam_hits2 $hmm $subject2
