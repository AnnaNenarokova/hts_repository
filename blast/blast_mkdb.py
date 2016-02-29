#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from blast.classes.blast import Blast

subj_paths = [
# "/home/anna/Dropbox/phd/db/proteomes/arabidopsis/data/arabidopsis.fasta",
# "/home/anna/Dropbox/phd/db/proteomes/giardia/data/giardia.fasta",
# "/home/anna/Dropbox/phd/db/proteomes/homo/data/homo.fasta",
# "/home/anna/Dropbox/phd/db/proteomes/saccharomyces/data/yeast.fasta",
# "/home/anna/Dropbox/phd/db/proteomes/trichomonas/data/trichomonas.fasta",
# "/home/anna/Dropbox/phd/db/proteomes/trypanosoma/data/trypanosoma.fasta"
'/home/anna/Dropbox/phd/db/proteomes/reference_proteomes.fasta'
]

for subj in subj_paths:
	new_blast = Blast(subj_path=subj, db_type='prot')
	new_blast.makeblastdb()
