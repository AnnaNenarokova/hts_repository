tblastn -query /home/nenarokova/blast_proteome/reference_proteomes.fasta \
-db /home/nenarokova/blast_proteome/Hemistasia_cutadapt_trinity_run3/blast_db/Hemistasia_cutadapt_trinity_run3.db \
-out /home/nenarokova/blast_proteome/hemistasia_bl_report.csv \
-outfmt "10  qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send " \
-num_threads 32 -evalue 0.01 -word_size 3