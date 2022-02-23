#!python3
import os

def listdir_nohidden(path):
	for f in os.listdir(path):
		if not f.startswith('.'):
			yield f

def parse_eggnog_annotation(eggnog_path, options_default=True, delimiter = "\t"):
	eggnog_dict = {}
	if options_default:
		options = "query	seed_ortholog	evalue	score	eggNOG_OGs	max_annot_lvl	COG_category	Description	Preferred_name	GOs	EC	KEGG_ko	KEGG_Pathway	KEGG_Module	KEGG_Reaction	KEGG_rclass	BRITE	KEGG_TC	CAZy	BiGG_Reaction	PFAMs"
		options_split = options.split(delimiter)
	with open(eggnog_path) as eggnog_file:
		for line in eggnog_file:
			if line[:2] == "##":
				pass
			elif line[0] == "#" and not options_default:
				options = line.rstrip()[1::]
				options_split = options.split(delimiter)
			else:
				line_split = line.split(delimiter)
				seqid = line_split[options_split.index("query")]
				eggnog_dict[seqid] = {}
				for i, key in enumerate(options_split):
					eggnog_dict[seqid][key] = line_split[i]
	return eggnog_dict

def parse_many_eggnog_files(eggnog_dir):
	
	eggnog_dict = parse_eggnog_annotation(eggnog_path, options_default=True, delimiter = "\t")
	return eggnog_dict