#!/usr/bin/python3
#Check spliting names in all three files!
import os
import re
from collections import OrderedDict

os.chdir('/home/kika/MEGAsync/blasto_project/genes/c_deaminase/p57_imp_mit/')
multiloc = open('p57_hits_multiloc.txt', 'r')
targetp = open('p57_hits_targetp.txt', 'r')
predsl = open('p57_hits_predsl.txt', 'r')
predictions = open('p57_hits_predictions.tsv', 'w')

ml_dict = OrderedDict()
for line in multiloc:
	try:
		name = line.split('\t')[0]
		first = line.split('\t')[1]
		second = line.split('\t')[2]
		if 'mitochondrial' in first:
			first = first.replace('mitochondrial', 'mit')
			ml_dict[name] = first
		elif 'secretory pathway' in first:
			if 'mitochondrial' in second:
				pred = second.replace('mitochondrial', 'mit') + ' (' + first.replace('secretory pathway', 'sp') + ')'
				ml_dict[name] = pred
			else:
				ml_dict[name] = first.replace('secretory pathway', 'sp')
		elif 'nuclear' in first:
			first = first.replace('nuclear', 'nuc')
			ml_dict[name] = first
		elif 'cytoplasmic' in first:
			first = first.replace('cytoplasmic', 'cyt')
			ml_dict[name] = first
		else:
			print(name + '_____ml')
	except:
		pass
# print(ml_dict)

tp_dict = {}
for line in targetp:
	try:
		name = line.split('\t')[0]
		mit = line.split('\t')[2]
		sp = line.split('\t')[3]
		other = line.split('\t')[4]
		loc = line.split('\t')[5]
		if loc == 'M':
			pred = 'mit: ' + mit
			tp_dict[name] = pred
		elif loc == 'S':
			pred = 'mit: ' + mit + ' (sp: ' + sp + ')'
			tp_dict[name] = pred
		elif loc == '_':
			pred = 'other: ' + other
			tp_dict[name] = pred
		else:
			print(name + '_____tp')
	except:
		pass
# print(tp_dict)

ps_dict = {}
for line in predsl:
	name = line.split('\t')[0]
	mit = line.split('\t')[2]
	sp = line.split('\t')[3]
	loc = line.split('\t')[4]
	if loc == 'mitochondrion':
		pred ='mit: ' + mit
		ps_dict[name] = pred
	elif loc == 'secreted':
		pred = 'mit: ' + mit + ' (sp: ' + sp + ')'
		ps_dict[name] = pred
	elif loc == 'other':
		ps_dict[name] = '-'
	else:
		print(name + '_____ps')
# print(ps_dict)

predictions.write('Name\tMultiLoc2\tTargetP\tPredSL\n')

for key, value in ml_dict.items():
	if key in tp_dict.keys():
		if key in ps_dict.keys():
			predictions.write('{}\t{}\t{}\t{}\n'.format(key, value, tp_dict[key], ps_dict[key]))
		else:
			print(key + ' not in ps')
	else:
		print(key + ' not in tp')