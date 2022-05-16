#!/usr/bin/python3
from os import listdir
from Bio import SeqIO

def listdir_nohidden(path):
    for f in listdir(path):
        if not f.startswith('.'):
            yield f

def filter_fastas_exclude_sp(exclude_list, indir, outdir, species_id_delimiter="_"):
	for file_name in listdir_nohidden(indir):
		infile = indir + file_name
		out_records = []
		for record in SeqIO.parse(infile, "fasta"):
			species_id = record.id.split(species_id_delimiter)[0]
			if species_id not in exclude_list:
				out_records.append(record)
		outfile = outdir + file_name
		SeqIO.write(out_records, outfile, "fasta")
	return 0

def filter_fasta_keep_sp(keep_list, infasta, outfasta, species_id_delimiter="-"):
	out_records = []
	for record in SeqIO.parse(infasta, "fasta"):
		species_id = record.id.split(species_id_delimiter)[0]
		if species_id in keep_list:
			out_records.append(record)
	SeqIO.write(out_records, outfasta, "fasta")
	return 0

def filter_fastas_keep_sp(keep_list, indir, outdir, species_id_delimiter="-"):
	for fasta in listdir_nohidden(indir):
		infasta = indir + fasta
		outfasta = outdir + fasta
		filter_fasta_keep_sp(keep_list, infasta, outfasta, species_id_delimiter=species_id_delimiter)
	return 0 

alpha_proteo_list=["GCA_002422845.1","GCA_009780035.1","GCA_006738645.1","GCA_002117145.1","GCA_000144605.1","GCA_000013025.1","GCA_000152825.2","GCA_007197755.1","GCA_002717245.1","GCA_002722055.1","GCA_002746255.1","GCA_000427665.1","GCA_002937855.1","GCA_001898075.1","GCA_000742475.1","GCA_000469665.2","GCA_000515255.1","GCA_000226315.1","GCA_004210305.1","GCA_000293845.2","GCA_000012345.1","GCA_000163555.2","GCA_900167455.1","GCA_902799835.1","GCA_000021745.1","GCA_000143145.1","GCA_000192745.1","GCA_000155675.2","GCA_003324715.1","GCA_003970735.1","GCA_002938315.1","GCA_000013085.1","GCA_003403095.1","GCA_000746585.2","GCA_000166935.1","GCA_002787635.1","GCA_002291925.1","GCA_009784235.1","GCA_000616095.1","GCA_002722885.1","GCA_000375545.1","GCA_000186705.2","GCA_009768975.1","GCA_000299935.1","GCA_000264455.2","GCA_002937655.1","GCA_002937675.1","GCA_002937625.1","GCA_002691145.1","GCA_002937495.1","GCA_002422365.1","GCA_002436405.1","GCA_001767855.1","GCA_002728255.1","GCA_011523425.1"]
cyano_list=["GCA_000464785.1","GCA_003503675.1","GCA_000155555.1","GCA_000019485.1","GCA_000346485.2","GCA_000204075.1","GCA_000484535.1","GCA_001870225.1","GCA_000353285.1","GCA_000015645.1","GCA_000195975.1","GCA_000013225.1","GCA_002075285.3","GCA_000317065.1","GCA_000010065.1","GCA_000018105.1","GCA_003149375.1"]
indir="/Users/anna/work/euk_local/nina_markers/fasta_markers/BacEuk_markers_faa/"
outdir="/Users/anna/work/euk_local/nina_markers/fasta_markers/cyano_markers/"

filter_fastas_keep_sp(cyano_list, indir, outdir, species_id_delimiter="-")