# adapter='/home/anna/bioinformatics/ngs/wheat/right_barcodes.fasta'
# adapter='/home/anna/bioinformatics/wheat/adapter.fasta'
adapter='/home/anna/bioinformatics/wheat/wheat_adapter.fasta'
outfile='/home/anna/bioinformatics/htses/ERR015599/not_bsc_1/not_bsc_1/not_bcs_right_bcs.csv'
blast_db='/home/anna/bioinformatics/htses/ERR015599/not_bsc_1/not_bsc_1/db_folder/not_bsc_1.db'
blastn -query $adapter -db $blast_db -out $outfile -outfmt 10 -task blastn-short -num_threads 8