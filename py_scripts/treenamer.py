#!/usr/bin/python3

#file in format Acc. number \t name of organism
names = open('/home/kika/MEGAsync/Euglena longa/2013 Sekvenovanie/Glycerolipids/SQD pathway/SQD2 tree/names.txt', 'r')

name_dict = {}

for name in names:
    splitted_line = name.split('\t')
    name_dict[splitted_line[0]] = splitted_line[1][:-1]

tree = open('/home/kika/MEGAsync/Euglena longa/2013 Sekvenovanie/Glycerolipids/SQD pathway/SQD2 tree/SQD2_trimal_automated1.phy.treefile', 'r')
tree_line = tree.readline()

for key in name_dict:
    tree_line = tree_line.replace(key, name_dict[key])


#2 ways of writting results to the file:
###1) can't forget to close the file in the end of the code
##result = open('Tree_renamed.txt', 'w')
##result.write(tree_line)
##result.close()

#2) closes result file automatically
with open('/home/kika/MEGAsync/Euglena longa/2013 Sekvenovanie/Glycerolipids/SQD pathway/SQD2 tree/SQD2_iqtree.txt', 'w') as result:
    result.write(tree_line)