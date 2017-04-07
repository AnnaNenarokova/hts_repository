#!/usr/bin/python3
from collections import OrderedDict
from Bio import SeqIO
import pandas as pd

infile = SeqIO.parse('/home/kika/Dropbox/blasto_project/blastocrithidia/genes/insertions/alignments/out_p57_nt.fasta', 'fasta')


codon_list = ['GCG', 'GCA', 'GCT', 'GCC', 'TGT', 
              'TGC', 'GAT', 'GAC', 'GAG', 'GAA', 
              'TTT', 'TTC', 'GGG', 'GGA', 'GGT', 
              'GGC', 'CAT', 'CAC', 'ATA', 'ATT', 
              'ATC', 'AAG', 'AAA', 'TTG', 'TTA', 
              'CTG', 'CTA', 'CTT', 'CTC', 'ATG', 
              'AAT', 'AAC', 'CCG', 'CCA', 'CCT', 
              'CCC', 'CAG', 'CAA', 'AGG', 'AGA', 
              'CGG', 'CGA', 'CGT', 'CGC', 'AGT', 
              'AGC', 'TCG', 'TCA', 'TCT', 'TCC', 
              'ACG', 'ACA', 'ACT', 'ACC', 'GTG', 
              'GTA', 'GTT', 'GTC', 'TGG', 'TAT', 
              'TAC', 'TGA', 'TAG', 'TAA']

aa_list = ['Ala', 'Ala', 'Ala', 'Ala', 'Cys', 
           'Cys', 'Asp', 'Asp', 'Glu', 'Glu', 
           'Phe', 'Phe', 'Gly', 'Gly', 'Gly', 
           'Gly', 'His', 'His', 'Ile', 'Ile', 
           'Ile', 'Lys', 'Lys', 'Leu', 'Leu', 
           'Leu', 'Leu', 'Leu', 'Leu', 'Met', 
           'Asn', 'Asn', 'Pro', 'Pro', 'Pro', 
           'Pro', 'Gln', 'Gln', 'Arg', 'Arg', 
           'Arg', 'Arg', 'Arg', 'Arg', 'Ser', 
           'Ser', 'Ser', 'Ser', 'Ser', 'Ser', 
           'Thr', 'Thr', 'Thr', 'Thr', 'Val', 
           'Val', 'Val', 'Val', 'Trp', 'Tyr', 
           'Tyr', 'zEnd', 'zEnd', 'zEnd']

def count_codons(sequence):
    codon_table = OrderedDict()
    for cod in codon_list:
        codon_table[cod] = 0
    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]
        if codon not in codon_table:
            codon_table[codon] = 1
        else:
            for key, value in codon_table.items():
                if codon == key:
                    codon_table[codon] += 1
    for key,value in codon_table.items():
        return codon_table

aa_dict = {}
for i in range(len(codon_list)):
    aa_dict[codon_list[i]] = aa_list[i]

pandas_dict = {}
for sequence in infile:
	seq = sequence.seq.upper()
	name = sequence.name
	pandas_dict[name] = count_codons(sequence)
    
pandas_dict['AA'] = aa_dict

df = pd.DataFrame(pandas_dict)
df.sort('AA', ascending=1, inplace=True)
df.fillna(0, inplace=True)
df['AA'][df['AA'] == 0] = 'X'
df['AA'][df['AA'] == 'zEnd'] = 'END'
df.reset_index(level=0, inplace=True)
df.rename(columns={'index': 'codon'}, inplace=True)
col_list = list(df)
col_list[0], col_list[1] = col_list[1], col_list[0]
df = df.reindex(columns=col_list)
df.set_index('AA', inplace=True)
df = df.transpose()
df.to_csv('/home/kika/Dropbox/blasto_project/blastocrithidia/genes/insertions/alignments/p57_ins_codons.tsv', sep='\t')