#!/usr/bin/python3
from os import listdir
from Bio import SeqIO
from Bio.Seq import Seq
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

def filter_fastas_exclude_sp_new(exclude_list, indir, outdir):
	for file_name in listdir_nohidden(indir):
		infile = indir + file_name
		out_records = []
		for record in SeqIO.parse(infile, "fasta"):
			species_id = record.id.split("-")[0]
			try:
				species_id = species_id.split("_")[1]
			except:
				pass
			if species_id not in exclude_list:
				out_records.append(record)
		outfile = outdir + file_name
		SeqIO.write(out_records, outfile, "fasta")
	return 0

def filter_fasta_keep_sp_old(keep_list, infasta, outfasta, species_id_delimiter="-", euk=False):
	out_records = []
	euk_regex = "^EP\d+-P\d+"
	for record in SeqIO.parse(infasta, "fasta"):
		species_id = record.id.split(species_id_delimiter)[0]
		if euk:
			if re.match(euk_regex, record.id):
				if species_id in keep_list:
					out_records.append(record)
			else:
				out_records.append(record)
		else:
			if species_id in keep_list:
				out_records.append(record)
	SeqIO.write(out_records, outfasta, "fasta")
	return 0

def filter_fasta_keep_sp(keep_list, infasta, outfasta, species_id_delimiter="-", euk=False):
	out_records = []
	# euk_regex = "\w+_EP\d+-P\d+"
	euk_regex = "EP\d+_\S+_P\d+"
	for record in SeqIO.parse(infasta, "fasta"):
		seq_id = record.id.split("-")[0]
		if re.match(euk_regex, record.id):
			species_id = seq_id.split("_")[0]
		else:
			species_id = seq_id
		if species_id in keep_list:
			out_records.append(record)
	SeqIO.write(out_records, outfasta, "fasta")
	return 0

def filter_fastas_keep_sp(keep_list, indir, outdir, species_id_delimiter="-", euk=False, abce=False):
	for fasta in listdir_nohidden(indir):
		print(fasta)
		infasta = indir + fasta
		outfasta = outdir + fasta
		if abce:
			filter_abce_keep_sp(keep_list, infasta, outfasta)
		else:
			filter_fasta_keep_sp(keep_list, infasta, outfasta, species_id_delimiter=species_id_delimiter,euk=euk)
	return 0 

def filter_fastas_keep_sp_read_list(list_dir, indir, outdir, list_ext=".txt", euk=False):
	for fasta in listdir_nohidden(indir):
		print(fasta)
		name = fasta.split(".")[0]
		infasta = indir + fasta
		outfasta = outdir + fasta
		keep_list_path = list_dir + name + list_ext
		print(keep_list_path)
		try:
			keep_list = read_list(keep_list_path)
		except:
			print(keep_list_path, "not found")
		else:
			filter_fasta_keep_seqs(keep_list, infasta, outfasta, euk=euk)
	return 0 

def filter_fasta_exclude_sp_simple(exclude_list, infasta_path, outfasta_path):
	out_records = []
	for record in SeqIO.parse(infasta_path, "fasta"):
		species_id = record.id
		if species_id not in exclude_list:
			out_records.append(record)
	SeqIO.write(out_records, outfasta_path, "fasta")
	return outfasta_path

def filter_fasta_keep_seq_simple(keep_list, infasta_path, outfasta_path):
	out_records = []
	for record in SeqIO.parse(infasta_path, "fasta"):
		seq_id = record.id
		if seq_id in keep_list:
			out_records.append(record)
	SeqIO.write(out_records, outfasta_path, "fasta")
	return outfasta_path


def filter_fasta_keep_seqs(keep_list, infasta_path, outfasta_path, euk=False):
	out_records = []
	euk_regex = "EP\d+_\S+_P\d+"
	for record in SeqIO.parse(infasta_path, "fasta"):
		seq_id = record.id
		if euk:
			if re.match(euk_regex, seq_id):
				if seq_id in keep_list:
					out_records.append(record)
			else:
				out_records.append(record)
		else:
			if seq_id in keep_list:
				out_records.append(record)
	SeqIO.write(out_records, outfasta_path, "fasta")
	return outfasta_path

def remove_euks_fasta(infasta_path, outfasta_path):
	out_records = []
	euk_regex = "\w+_EP\d+-P\d+"
	for record in SeqIO.parse(infasta_path, "fasta"):
		if re.match(euk_regex, record.id):
			pass
		else:
			out_records.append(record)
	SeqIO.write(out_records, outfasta_path, "fasta")
	return outfasta_path

def remove_euks_fastas(indir, outdir):
	for fasta in listdir_nohidden(indir):
		print(fasta)
		infasta_path = indir + fasta
		outfasta_path = outdir + fasta
		remove_euks_fasta(infasta_path, outfasta_path)
	return outdir

def filter_fasta_keep_seq_simple(keep_list, infasta_path, outfasta_path):
	out_records = []
	for record in SeqIO.parse(infasta_path, "fasta"):
		seq_id = record.id
		if seq_id in keep_list:
			out_records.append(record)
	SeqIO.write(out_records, outfasta_path, "fasta")
	return outfasta_path

def filter_fasta_complex(infasta_path, outfasta_path, euk_keep_list, prok_sp_list, euk_sp_excude_list=False, prok_delimiter="-"):
	euk_regex = "EP\d+_\S+_P\d+"
	out_records = []
	for record in SeqIO.parse(infasta_path, "fasta"):
		seq_id = record.id
		if re.match(euk_regex, seq_id):
			if euk_sp_excude_list:
				species = seq_id.split("_")[0]
				if species in euk_sp_excude_list:
					# print (species, "excluded")
					pass
				else:
					out_records.append(record)
			elif seq_id in euk_keep_list:
				out_records.append(record)
		else:
			prok_sp = seq_id.split(prok_delimiter)[0]
			if prok_sp in prok_sp_list:
				out_records.append(record)
	SeqIO.write(out_records, outfasta_path, "fasta")
	return outfasta_path


def filter_fastas_keep_complex_read_list(euk_list_dir, indir, outdir, prok_sp_list, euk_sp_excude_list=False, list_ext=".txt"):
	for fasta in listdir_nohidden(indir):
		name = fasta.split(".")[0]
		print(name)
		infasta_path = indir + fasta
		outfasta_path = outdir + fasta
		keep_list_path = euk_list_dir + name + list_ext
		# print(keep_list_path)
		try:
			euk_keep_list = read_list(keep_list_path)
		except:
			print(keep_list_path, "not found")
		else:
			filter_fasta_complex(infasta_path, outfasta_path, euk_keep_list, prok_sp_list, euk_sp_excude_list=euk_sp_excude_list, prok_delimiter="-")
	return outdir
# infasta_path="/Users/vl18625/work/euk/molecular_clock/aebece_23_01/abce_94_markers_concat.fasta"
# outfasta_path="/Users/vl18625/work/euk/molecular_clock/aebece_23_01/abce_94_markers_concat_filtered.fasta"
# filter_fasta_keep_seq_simple(keep_list, infasta_path, outfasta_path)

euk_list_dir="/Users/vl18625/work/euk/markers_euks/nina_markers/01_07_23/archaea/ae_euk_mono_ids/" 
indir="/Users/vl18625/work/euk/markers_euks/nina_markers/01_07_23/archaea/faa_unfiltered/"
outdir="/Users/vl18625/work/euk/markers_euks/nina_markers/01_07_23/archaea/ae_81_m_no_metamonada_11_03_24/faa/"
archaea_keep_list=["GCA_016294985.1","GCA_019057385.1","GCA_016292335.1","GCA_019056805.1","GCA_016840905.1","GCA_002728275.1","GCA_001940725.1","GCA_016839295.1","GCA_001940645.1","GCA_016840025.1","GCA_016840425.1","Heimdallarchaeum_endolithica_PR6","GCA_019057815.1","GCA_008000775.1","GCA_001940655.1","GCA_019058015.1","GCA_019058515.1","GCA_019058445.1","GCA_019058365.1","GCA_019057795.1","GCA_005191425.1","GCA_019058315.1","GCA_011365055.1","GCA_014729935.1","GCA_016839265.1","GCA_001940665.1","GCA_019058495.1","GCA_016839805.1","GCA_004524565.1","GCA_008080745.1","GCA_011364985.1","GCA_004524445.1","GCA_016840825.1","GCA_011362025.1","GCA_016840465.1","GCA_018901755.1","GCA_015521825.1","GCA_016198755.1","GCA_001784635.1","GCA_011333035.1","GCA_017608955.1","GCA_018304545.1","GCA_018304615.1","GCA_016181005.1","GCA_011335085.1","GCA_016202815.1","GCA_016931255.1","GCA_015520105.1","GCA_016932215.1","GCA_018816245.1","GCA_000806115.1","GCA_015522745.1","GCA_016198685.1","GCA_018920315.1","GCA_016187335.1","GCA_002785505.1","GCA_001742785.1","GCA_002254565.1","GCA_016931955.1","GCA_003663045.1","GCA_014727915.1","GCA_001723855.1","GCA_016935655.1","GCA_019429125.1","GCA_018897155.1","GCA_015520605.1","GCA_009392915.1","GCA_003553825.1","GCA_018304505.1","GCA_017608805.1","GCA_016205145.1","GCA_017610205.1","GCA_000830275.1","GCA_000402355.1","GCA_016699555.1","GCA_016187745.1","GCA_018304425.1","GCA_015521515.1","GCA_003661685.1","GCA_015522845.1","GCA_016926295.1","GCA_016212395.1","GCA_902384795.1","GCA_902385155.1","GCA_013426015.1","GCA_902385515.1","GCA_903884115.1","GCA_002214165.1","GCA_002204695.1","GCA_014874295.1","GCA_001871475.1","GCA_011362975.1","GCA_902384585.1","GCA_903828955.1","GCA_903835385.1","GCA_016212525.1","GCA_016935455.1","GCA_018812625.1","GCA_018304385.1","GCA_002792955.1","GCA_011358415.1","GCA_016188965.1","GCA_018819225.1","GCA_902384935.1","GCA_016194335.1","GCA_017608385.1","GCA_902385255.1","GCA_014729335.1","GCA_007130955.1","GCA_011333755.1","GCA_011364745.1","GCA_000008085.1","GCA_011331665.1","GCA_003568775.1","GCA_001552015.1","GCA_000387965.1","GCA_902385655.1","GCA_018691935.1","GCA_002762835.1","GCA_902385625.1","GCA_903828205.1","GCA_018650665.1","GCA_002763115.1","GCA_016211995.1","GCA_018303885.1","GCA_002897655.1","GCA_902385635.1","GCA_018653175.1","GCA_017991485.1","GCA_017609175.1","GCA_017609405.1","GCA_017609755.1","GCA_018304175.1","GCA_018815925.1","GCA_001786395.1","GCA_017609115.1","GCA_002780285.1","GCA_017609885.1","GCA_018818285.1","GCA_013331705.1","GCA_002763075.1","GCA_018303825.1","GCA_015121965.1","GCA_002499655.1","GCA_002503995.1","GCA_002763265.1","GCA_002687815.1","GCA_018648525.1","GCA_013329215.1","GCA_000806155.1","GCA_002688355.1","GCA_000830315.1","GCA_018302225.1","GCA_018303545.1","GCA_018671245.1","GCA_018829185.1","GCA_000402515.1","GCA_016188045.1","GCA_002505585.1","GCA_014240455.1","GCA_017608345.1","GCA_903878405.1","GCA_002505525.1","GCA_002779235.1","GCA_016203225.1","GCA_017609645.1","GCA_018302815.1","GCA_019323015.1","GCA_018221105.1","GCA_903904885.1","GCA_002762865.1","GCA_001871415.1","GCA_011368255.1","GCA_016192995.1","GCA_013202845.1","GCA_005222965.1","GCA_000830295.1","GCA_016185945.1","GCA_018696595.1","GCA_018657845.1","GCA_018671675.1","GCA_018812765.1","GCA_016185625.1","GCA_018302605.1","GCA_002762785.1","GCA_003695265.1","GCA_016187565.1","GCA_014729995.1","GCA_015519985.1","GCA_016180135.1","GCA_016180195.1","GCA_017608625.1","GCA_018263355.1","GCA_018303285.1","GCA_018303425.1","GCA_018646625.1","GCA_018653045.1","GCA_019322485.1","GCA_019323755.1","GCA_016927245.1","GCA_007117065.1","GCA_016930415.1","GCA_016935265.1","GCA_002688315.1","GCA_018668595.1","GCA_002762985.1","GCA_003599145.1","GCA_016180285.1","GCA_016935985.1","GCA_018658365.1","GCA_000806095.1","GCA_000220355.1","Halo_Nar1","GCA_001761425.1","GCA_009617975.1","GCA_017610385.1","GCA_016432325.1","GCA_003663345.1","GCA_003554845.1","GCA_016932615.1","GCA_003663355.1","GCA_018220935.1","GCA_018221005.1","GCA_018220955.1","GCA_014189685.1","GCA_002502135.1","GCA_002494525.1","GCA_011361855.1","GCA_011367225.1","GCA_003661465.1","GCA_001515205.2","GCA_003555245.1","GCA_000008665.1","GCA_000385565.1","GCA_000025285.1","GCA_000194625.1","GCA_000025505.1","GCA_002011165.1","GCA_900156425.1","GCA_000196895.1","GCA_000755225.1","GCA_000023965.1","GCA_009617995.1","GCA_900102305.1","GCA_003730195.1","GCA_900100385.1","GCA_000026045.1","GCA_007421925.1","GCA_000006805.1","GCA_000336675.1","GCA_002952775.1","GCA_000306765.2","GCA_900114455.1","GCA_001282785.1","GCA_006861655.1","GCA_900107665.1","GCA_000022205.1","GCA_900103505.1","GCA_000328525.1","GCA_003430825.1","GCA_000025625.1","GCA_000230715.3","GCA_000328685.1","GCA_018609935.1","GCA_003021085.1","GCA_003675855.1","GCA_007118975.1","GCA_009889665.1","GCA_000063445.1","GCA_004212075.1","GCA_000015765.1","GCA_000304355.2","GCA_004102725.1","GCA_001571385.1","GCA_001315945.1","GCA_000784355.1","GCA_018263335.1","GCA_000017625.1","GCA_017873855.1","GCA_000021965.1","GCA_000013445.1","GCA_015660865.1","GCA_004211975.1","GCA_004193545.1","GCA_019429385.1","GCA_000685155.1","GCA_000013725.1","GCA_000196655.1","GCA_000328665.1","GCA_000970205.1","GCA_003162615.1","GCA_000204415.1","GCA_000235565.1","GCA_000014945.1","GCA_000711905.1","GCA_016207465.1","GCA_003194425.1","GCA_011049045.1","GCA_001766825.1","GCA_002897955.1","GCA_002011125.1","GCA_003695745.1","GCA_015521895.1","GCA_002813695.1","GCA_000024185.1","GCA_000016525.1","GCA_000404165.1","GCA_002072215.1","GCA_000012545.1","GCA_003491285.1","GCA_018141185.1","GCA_000166095.1","GCA_000008645.1","GCA_003584625.1","GCA_000023985.1","GCA_002945325.1","GCA_000017185.1","GCA_000214415.1","GCA_000007185.1","GCA_001587575.1","GCA_004212155.1","GCA_015520705.1","GCA_000725425.1","GCA_000007305.1","GCA_002214585.1","GCA_000246985.3","GCA_005888755.1","GCA_018396775.1","GCA_018396915.1","GCA_018396755.1","GCA_011367275.1","GCA_002011035.1","GCA_002490245.1","GCA_018396635.1","GCA_001399805.1","GCA_001399795.1","GCA_004376295.1","GCA_018396705.1","GCA_011051215.1","GCA_011053435.1","GCA_018396615.1","GCA_002255025.1","GCA_018396415.1","GCA_002726865.1","GCA_018396865.1","GCA_003601775.1","GCA_017601145.1","GCA_011605725.1","GCA_003661385.1","GCA_000019605.1","GCA_003947435.1","GCA_003661365.1","GCA_011605825.1","GCA_011362245.1","GCA_004028775.1","GCA_015660995.1","GCA_004348015.1","GCA_011364685.1","GCA_004347915.1","GCA_000270325.1","GCA_002898395.1","GCA_011364615.1","GCA_011364235.1","GCA_013340765.1","GCA_011333845.1","GCA_015523545.1","GCA_002011075.1","GCA_011773305.1","GCA_014361085.1","GCA_016184315.1","GCA_011358735.1","GCA_900248165.1","GCA_000200715.1","GCA_011771385.1","GCA_000220175.2","GCA_000812185.1","GCA_000018465.1","GCA_900065925.1","GCA_002787055.1","GCA_016838825.1","GCA_001870125.1","GCA_000303155.1","GCA_013114725.1","GCA_009898475.1","GCA_902812495.1","GCA_016200045.1","GCA_016871995.1","GCA_003661605.2","Ga0009305","GCA_000398765.1","GCA_015520395.1","GCA_003019615.1","GCA_003019535.1","GCA_002507085.1","GCA_003650925.1","GCA_003431325.1","GCA_000011125.1","GCA_003116855.1","GCA_000186365.1","GCA_000015945.1","GCA_000092185.1","GCA_000258425.1","GCA_009904015.1","GCA_001481685.1","GCA_000017945.1","GCA_000145985.1","GCA_011337845.1","GCA_015521325.1","GCA_003056265.1","GCA_015520265.1","GCA_015521735.1","GCA_015522635.1","GCA_001462395.1","GCA_000223395.1","GCA_000389735.1","GCA_000016605.1","GCA_900079115.1","GCA_014648235.1","GCA_003649305.1","GCA_003650785.1","GCA_011042215.1","GCA_000015225.1","GCA_000018305.1","GCA_000190315.1","GCA_000007225.1","GCA_903877165.1","GCA_018335115.1","GCA_002838995.1","GCA_011049295.1","GCA_014361195.1","GCA_008297685.1","GCA_002502685.1","GCA_002838935.1","GCA_016928095.1","GCA_002494605.1","GCA_003602415.1","GCA_000246735.1","GCA_016777175.1","GCA_002503015.1","GCA_012959275.1","GCA_003324635.1","GCA_016845365.1","GCA_018645625.1","GCA_002505775.1","GCA_018650285.1","GCA_902627615.1","GCA_002509225.1","GCA_004195655.1","GCA_016207515.1","GCA_003649915.1","GCA_003649695.1","GCA_013415715.1","GCA_000308215.1","GCA_000300255.2","GCA_003555025.1","GCA_002506325.1","GCA_009911715.1","GCA_002506995.1","GCA_009780575.1","GCA_013415865.1","GCA_003552585.1","GCA_011331255.1","GCA_004377185.1","GCA_016214785.1","GCA_001856825.1","GCA_002204705.1","GCA_002204655.1","GCA_900090055.1","GCA_002078355.1","GCA_000496135.1","GCA_014874365.1","GCA_014646795.1","GCA_000195915.1","GCA_002503205.1","GCA_018818785.1","GCA_002503985.1"]
euk_sp_excude_list=["EP00803","EP01155","EP01156","EP00792","EP00764","EP00765","EP01146","EP00766","EP00767","EP00701","EP00763","EP00702","EP00703","EP00768","EP00769","EP00704","EP00705","EP00706","EP00770","EP00708","EP00771"]

filter_fastas_keep_complex_read_list(euk_list_dir, indir, outdir, prok_sp_list=archaea_keep_list, euk_sp_excude_list=euk_sp_excude_list, list_ext=".txt")

