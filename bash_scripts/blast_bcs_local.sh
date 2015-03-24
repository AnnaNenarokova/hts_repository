adapter='/home/anna/bioinformatics/ngs/wheat/right_barcodes_adaptered.fasta'
# adapter='/home/anna/bioinformatics/wheat/adapter.fasta'
# adapter='/home/anna/bioinformatics/wheat/wheat_adapter.fasta'
# adapter='/home/anna/bioinformatics/htses/pT7blue-G8esc_rev.fasta'
# adapter='/home/anna/bioinformatics/bioprograms/Trimmomatic-0.33/adapters/TruSeq2-PE.fa'

outfile='/home/anna/bioinformatics/htses/ERR015599/not_bsc_1/not_bcs_right_bcs.csv'
blast_db='/home/anna/bioinformatics/htses/ERR015599/not_bsc_1/blast_db/not_bsc_1.db'
# blast_db='/home/anna/bioinformatics/wheat/H7_1/db_folder/H7_1.db'

blastn -query $adapter -db $blast_db -out $outfile -outfmt 10 -task blastn-short -num_threads 8