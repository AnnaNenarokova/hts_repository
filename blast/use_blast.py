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
    # {'query': '/home/anna/Dropbox/phd/db/proteomes/reference_proteomes.fasta',
    #  'subj_db': '/home/anna/Dropbox/phd/db/proteomes/euglena/data/E_gracilis_transcriptome_final.PROTEINS/blast_db/E_gracilis_transcriptome_final.PROTEINS.db'
    #  },
    # {'query': '/home/anna/Dropbox/phd/db/proteomes/euglena/data/euglena_all_proteins.fasta',
    #  'subj_db': '/home/anna/Dropbox/phd/db/proteomes/reference_mitoproteomes/blast_db/reference_proteomes.db'
     # },
     {'query': '/home/anna/Dropbox/phd/db/proteomes/trichomonas/data/trichomonas_mito.fasta',
     'subj_db': '/home/anna/Dropbox/phd/db/proteomes/giardia/data/giardia/blast_db/giardia.db'
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