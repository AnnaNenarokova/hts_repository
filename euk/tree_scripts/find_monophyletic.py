#!/usr/bin/python3
from os import listdir
from ete3 import Tree

def listdir_nohidden(path):
	for f in listdir(path):
		if not f.startswith('.'):
			yield f

