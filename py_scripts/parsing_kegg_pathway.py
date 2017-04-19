#!/usr/bin/python3
from bioservices.kegg import KEGG

output = open('/home/kika/Dropbox/blasto_project/blastocrithidia/genes/HR/tbr_acc.txt', 'w')

kegg = KEGG()
pathway = kegg.get('tbr03440')
dict_data = kegg.parse(pathway)

# g = x.get('tbr03440:Tb11.01.0910/aaseq')
# print(g)

# res = x.parse_kgml_pathway("tbr03440")
# print(res['entries'][0])

# for key, value in dict_data['GENE'].items():
# 	print(key, value)

for gene in dict_data['GENE']:
	output.write(gene + '\n')