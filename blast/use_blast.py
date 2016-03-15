#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from blast.classes.blast import Blast
from blast.classes.blast_parser import BlastParser

#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from blast.classes.blast import Blast
from blast.classes.blast_parser import BlastParser

blast_pairs = [
     {
     'query': '/home/anna/Dropbox/phd/mitoproteomes/proteomes/trypanosoma/rna_edining.fasta',
     'subj_db': '/home/anna/Dropbox/phd/mitoproteomes/proteomes/euglena/data/E_gracilis_transcriptome_final.PROTEINS/blast_db/E_gracilis_transcriptome_final.PROTEINS.db'
          }
            ]

blast_csv_paths = []
for pair in blast_pairs:
    new_blast = Blast(query_path=pair['query'], db_path=pair['subj_db'], db_type='prot')
    custom_outfmt = 'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'
    blast_csv_path = new_blast.blast(bl_type='blastp', evalue=0.01, outfmt='comma_values', custom_outfmt=custom_outfmt, word_size=2)
    print blast_csv_path
    blast_csv_paths.append(blast_csv_path)

for blast_path in blast_csv_paths:
    print blast_path

# query_path = '/home/anna/Dropbox/phd/mitoproteomes/proteomes/trypanosoma/rna_edining.fasta'
# db_path = '/home/anna/Dropbox/phd/mitoproteomes/hemistasia/blastdb/hemistasia.db'

# new_blast = Blast(query_path=query_path, db_path=db_path, db_type='nucl')
# custom_outfmt = 'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'
# blast_csv_path = new_blast.blast(bl_type='tblastn', evalue=0.01, outfmt='comma_values', custom_outfmt=custom_outfmt, word_size=2)

# query_path = '/home/anna/Dropbox/phd/mitoproteomes/hemistasia/Hemistasia_cutadapt_trinity_run3.fasta'
# subj_path = '/home/anna/Dropbox/phd/mitoproteomes/proteomes/trypanosoma/rna_edining.fasta'

# new_blast = Blast(query_path=query_path, subj_path=subj_path, db_type='prot')
# custom_outfmt = 'qseqid qlen sseqid slen length evalue pident bitscore mismatch gaps qstart qend sstart send'
# blast_csv_path = new_blast.blast(bl_type='blastx', evalue=0.01, outfmt='comma_values', custom_outfmt=custom_outfmt, word_size=2)