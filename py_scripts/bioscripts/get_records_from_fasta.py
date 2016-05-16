#!/usr/bin/python
from Bio import SeqIO

l = ['comp36539_c1_seq4','comp36157_c0_seq1','comp35277_c0_seq2','comp31291_c0_seq1','comp30671_c0_seq1','comp30466_c0_seq1','comp24161_c0_seq2','comp24059_c0_seq2','comp31765_c0_seq1','comp30649_c0_seq1','comp31473_c0_seq1','comp26338_c0_seq1','comp25319_c0_seq1','comp25680_c0_seq1','comp24300_c0_seq2','comp35213_c2_seq1','comp27950_c1_seq3','comp28715_c0_seq1','comp30567_c0_seq1','comp14920_c0_seq1 ','comp28286_c0_seq1','comp8127_c0_seq1','comp25697_c0_seq1','comp32961_c0_seq1','comp19503_c0_seq1','comp25660_c0_seq2','comp31856_c1_seq5','comp34185_c0_seq1','comp27161_c0_seq1','comp21396_c0_seq1','comp25126_c0_seq1','comp19974_c0_seq1','comp25642_c0_seq1','comp17468_c0_seq1','comp20171_c0_seq1','comp21369_c1_seq1','comp25091_c0_seq1','comp8148_c0_seq1','comp36615_c0_seq1','comp34870_c1_seq1','comp23967_c1_seq1','comp8156_c0_seq1','comp30296_c0_seq1','comp33743_c0_seq1','comp30366_c1_seq1','comp30451_c0_seq1','comp34484_c0_seq4','comp33450_c1_seq3','comp29409_c1_seq1','comp8159_c0_seq1','comp23081_c0_seq1','comp31136_c1_seq3','comp12747_c0_seq1','comp26715_c0_seq4','comp21099_c0_seq1','comp27519_c0_seq1','comp29498_c0_seq1','comp31034_c0_seq1','comp36638_c0_seq1','comp17496_c0_seq1','comp17821_c0_seq1','comp31551_c0_seq1','comp33055_c0_seq1','comp22846_c0_seq1','comp24971_c0_seq1','comp25049_c0_seq1','comp36568_c0_seq1','comp29182_c0_seq3','comp20039_c0_seq1','comp34527_c0_seq1','comp27719_c0_seq1','comp34564_c0_seq6','comp32935_c0_seq1','comp29154_c0_seq1','comp32985_c0_seq2','comp25371_c1_seq1','comp17081_c0_seq1','comp29378_c0_seq1','comp17367_c0_seq1','comp31582_c0_seq2','comp34975_c0_seq2','comp33545_c0_seq1','comp34299_c0_seq1']
fasta = '/home/anna/Dropbox/phd/mitoproteome_project/genomes/euglena/euglena_transcr_assembly_japan.fasta'
results = []

for record in SeqIO.parse(fasta, "fasta"):
    for id in l:
        if id in record.description:
            results.append(record)

outpath = '/home/anna/Dropbox/phd/mitoproteome_project/genomes/euglena/paramylon_wax_ester.fasta'

SeqIO.write(results, outpath, "fasta")