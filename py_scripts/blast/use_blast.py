#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from blast.classes.blast import Blast
from blast.classes.blast_parser import BlastParser

query_pathes = {
# 'human' : '/home/anna/bioinformatics/euglenozoa/mitocarta/Human.MitoCarta2.0.fasta',
# 'yeast' : '/home/anna/bioinformatics/euglenozoa/yeast/yeast_orf_trans_all.fasta',
# 'tripanosoma' : '/home/anna/bioinformatics/euglenozoa/tripanosoma/tr_proteins.fasta',
'euglena' : '/home/anna/bioinformatics/euglenozoa/euglena/all_euglena_proteins/E_gracilis_transcriptome_final.PROTEINS.fasta'
}

db_pathes = {
'human' : '/home/anna/bioinformatics/euglenozoa/mitocarta/Human.MitoCarta2.0/blast_db/Human.MitoCarta2.0.db',
'yeast' : '/home/anna/bioinformatics/euglenozoa/yeast/orf_trans_all_yeast/blast_db/orf_trans_all_yeast.db',
'tripanosoma' : '/home/anna/bioinformatics/euglenozoa/tripanosoma/tr_proteins/blast_db/tr_proteins.db'
# 'euglena' : '/home/anna/bioinformatics/euglenozoa/euglena/all_euglena_proteins/E_gracilis_transcriptome_final.PROTEINS/blast_db/E_gracilis_transcriptome_final.PROTEINS.db'
}

blast_csv_pathes = []
for query in query_pathes:
    for db in db_pathes:
        new_blast = Blast(query_path=query_pathes[query], db_path=db_pathes[db], db_type='prot')
        custom_outfmt = 'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'
        blast_csv_path = new_blast.blast(bl_type='blastp', evalue=0.01, outfmt='comma_values', custom_outfmt=custom_outfmt, word_size=3)
        print blast_csv_path
        blast_csv_pathes.append(blast_csv_path)

for blast_path in blast_csv_pathes:
    print blast_path
# blast_dicts = BlastParser(blast_csv_path, features=custom_outfmt).read_hits()