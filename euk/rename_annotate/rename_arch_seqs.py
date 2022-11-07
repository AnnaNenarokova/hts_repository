#!python3
from os import listdir
from Bio import SeqIO
import re

def listdir_nohidden(path):
	for f in listdir(path):
		if not f.startswith('.'):
			yield f

def read_list(list_path):
	result_list = []
	with open (list_path) as list_file:
		for line in list_file:
			result_list.append(line.rstrip())
	return result_list

def rename_arch_seq(old_name):
	old_name_split = old_name.split("_")
	new_name = "arch_" + old_name_split[0] + "-" + old_name_split[-1]
	return new_name

def rename_seqs(infasta_path, outfasta_path):
	euk_regex = "^EP\d+_P\d+"
	out_records = []
	for record in SeqIO.parse(infasta_path, "fasta"):
		old_name = record.id
		if re.match(euk_regex, old_name):
			new_name = rename_arch_seq(old_name)
			record.id = new_name
		out_records.append(record)
	SeqIO.write(out_records, outfasta_path, "fasta")
	return outfasta_path


def rename_arch_seqs(indir, outdir, arcog_cog_dict):
	for fasta in listdir_nohidden(indir):
		arcog = fasta.split(".")[0]
		infasta_path = indir + fasta
		cog = arcog_cog_dict[arcog]
		outfasta_path = outdir + cog + ".faa"
		rename_seqs(infasta_path, outfasta_path)
	return outdir

indir = "/Users/vl18625/work/euk/markers_euks/nina_markers/ae/68_final_ae_markers/faa/"
outdir = "/Users/vl18625/work/euk/markers_euks/nina_markers/abe/seqs/abc_dataset/arch_faa_renamed/"

arcog_cog_dict = {"arCOG00410":"COG0016","arCOG00412":"COG0072","arCOG00415":"COG0468","arCOG00469":"COG0470","arCOG00779":"COG0200","arCOG00780":"COG1727","arCOG00781":"COG1717","arCOG00782":"COG0199","arCOG00785":"COG0255","arCOG00809":"COG0495","arCOG00865":"COG1156","arCOG00868":"COG1155","arCOG00987":"COG0130","arCOG01001":"COG0024","arCOG01179":"COG0361","arCOG01183":"COG0533","arCOG01227":"COG0552","arCOG01228":"COG0541","arCOG01344":"COG2238","arCOG01358":"COG0621","arCOG01560":"COG0532","arCOG01563":"COG5257","arCOG01704":"COG0452","arCOG01718":"COG0064","arCOG01722":"COG0099","arCOG01758":"COG0051","arCOG01762":"COG0085","arCOG01885":"COG1383","arCOG01887":"COG0180","arCOG01946":"COG2125","arCOG01950":"COG2075","arCOG04049":"COG1552","arCOG04050":"COG0258","arCOG04064":"COG0750","arCOG04067":"COG0090","arCOG04070":"COG0087","arCOG04071":"COG0088","arCOG04072":"COG0089","arCOG04086":"COG1841","arCOG04087":"COG0098","arCOG04088":"COG0256","arCOG04089":"COG2147","arCOG04090":"COG0097","arCOG04091":"COG0096","arCOG04092":"COG0094","arCOG04093":"COG1471","arCOG04094":"COG0198","arCOG04095":"COG0093","arCOG04096":"COG0186","arCOG04097":"COG0092","arCOG04098":"COG0091","arCOG04099":"COG0185","arCOG04108":"COG2051","arCOG04109":"COG1631","arCOG04113":"COG0197","arCOG04121":"COG0164","arCOG04126":"COG2126","arCOG04129":"COG2139","arCOG04154":"COG2007","arCOG04169":"COG0201","arCOG04182":"COG2004","arCOG04183":"COG1998","arCOG04185":"COG0184","arCOG04186":"COG1890","arCOG04208":"COG1997","arCOG04209":"COG1632","arCOG04223":"COG0023","arCOG04239":"COG0522","arCOG04240":"COG0100","arCOG04241":"COG0202","arCOG04242":"COG0102","arCOG04243":"COG0103","arCOG04245":"COG0052","arCOG04254":"COG0049","arCOG04255":"COG0048","arCOG04256":"COG0086","arCOG04257":"COG0086","arCOG04277":"COG0231","arCOG04287":"COG2058","arCOG04288":"COG0244","arCOG04289":"COG0081","arCOG04302":"COG0008","arCOG04304":"COG2451","arCOG04314":"COG2053","arCOG04372":"COG0080","arCOG04473":"COG2097"}
rename_arch_seqs(indir, outdir, arcog_cog_dict)