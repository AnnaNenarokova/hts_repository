#!/usr/bin/python
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from blast.classes.blast import Blast

subj_pathes = {
# 'amoeba': '/home/anna/bioinformatics/phd/mitoproteomes/acanthamoeba/amoeba_mitoproteins.fasta',
# 'arabidopsis': '/home/anna/bioinformatics/phd/mitoproteomes/arabidopsis/arabidopsis_mito.fasta',
# 'worm': '/home/anna/bioinformatics/phd/mitoproteomes/caenorhabditis/worm_mitoproteins.fasta',
# 'mouse' : '/home/anna/bioinformatics/phd/mitoproteomes/mitocarta/Mouse.MitoCarta2.0.fasta',
# 'human': '/home/anna/bioinformatics/phd/mitoproteomes/mitocarta/Human.MitoCarta2.0.fasta',
# 'yeast' : '/home/anna/bioinformatics/phd/mitoproteomes/saccharomyces/orf_trans_all.fasta',
# 'tetrahymena': '/home/anna/bioinformatics/phd/mitoproteomes/tetrahymena/tetrahymena_mito_gb.fasta',
# 'trypanosoma' : '/home/anna/bioinformatics/phd/mitoproteomes/trypanosoma/trypa_mitoproteins.fasta'
'reference_mitoproteomes': '/home/anna/Dropbox/phd/db/proteomes/reference_mitoproteomes.fasta'
}

for subj in subj_pathes:
	new_blast = Blast(subj_path=subj_pathes[subj], db_type='prot')
	new_blast.makeblastdb()
