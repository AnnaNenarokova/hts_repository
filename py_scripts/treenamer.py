#!/usr/bin/python3
names = open('/home/kika/MEGAsync/Euglena longa/2013 Sekvenovanie/Rho factor/Tree2/names.txt', 'r')

name_dict = {}

for name in names:
    splitted_line = name.split('\t')
    name_dict[splitted_line[0]] = splitted_line[1][:-1]

tree = open('/home/kika/MEGAsync/Euglena longa/2013 Sekvenovanie/Rho factor/Tree2/Rho_dedupl_trimal.phy.treefile', 'r')
tree_line = tree.readline()

for key in name_dict:
    tree_line = tree_line.replace(key, name_dict[key])


#2 moznosti zapisu vysledku do suboru
###1) na konci nesmiem zabudnut zatvorit subor
##result = open('Tree_renamed.txt', 'w')
##result.write(tree_line)
##result.close()

#2) zatvori sa automaticky
with open('/home/kika/MEGAsync/Euglena longa/2013 Sekvenovanie/Rho factor/Tree2/Rho_tree_renamed.txt', 'w') as result:
    result.write(tree_line)