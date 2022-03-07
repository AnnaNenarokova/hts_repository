import os, re, sys
from Bio import SeqIO

#read in a sequence alignment, write a constraint tree for IQ-Tree in which heims + euks are a monophyletic clade, CPR+Chloroflexi are a monophyletic clade, and all other taxa will be placed freely (between these 2 clades) 
target_tree = sys.argv[1]
#map tip IDs to domain
tip_to_domain = {}
inh = open("constraint_groups.csv")
for line in inh:
        fields = re.split(",", line.rstrip())
        tip_to_domain[fields[0]] = fields[1]
inh.close()

Heim = []
CPR = []
Other = []

#read the alignment
seqs = SeqIO.index(sys.argv[1], "fasta")
for rec in seqs:
        species = seqs[rec].id
        if tip_to_domain[species] == "Heim":
                Heim.append(species)
        elif tip_to_domain[species] == "CPR":
                CPR.append(species)
        elif tip_to_domain[species] == "Other":
                Other.append(species)
        else:
                print("Problem with species " + str(species))

#print constraint tree
Heim_bit = ",".join(Heim)
CPR_bit = ",".join(CPR)
Other_bit = ",".join(Other)

tree = "((" + Heim_bit + "),(" + CPR_bit + ")" + ',' + Other_bit + ");"
print(tree)