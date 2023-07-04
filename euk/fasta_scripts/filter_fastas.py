#!/usr/bin/python3
from os import listdir
from Bio import SeqIO
from Bio.Seq import Seq
import re

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

def filter_fasta_keep_sp(keep_list, infasta, outfasta, species_id_delimiter="-", euk=False):
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

def filter_abce_keep_sp(keep_list, infasta, outfasta):
	out_records = []
	euk_regex = "\w+_EP\d+-P\d+"
	for record in SeqIO.parse(infasta, "fasta"):
		seq_id = record.id.split("-")[0]
		if re.match(euk_regex, record.id):
			species_id = seq_id.split("_")[1]
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

def filter_fastas_exclude_sp_simple(exclude_list, infasta_path, outfasta_path):
	out_records = []
	for record in SeqIO.parse(infasta_path, "fasta"):
		species_id = record.id
		if species_id not in exclude_list:
			out_records.append(record)
	SeqIO.write(out_records, outfasta_path, "fasta")
	return outfasta_path

def filter_fastas_keep_seqs(keep_list, infasta_path, outfasta_path):
	out_records = []
	for record in SeqIO.parse(infasta_path, "fasta"):
		seq_id = record.id
		if seq_id in keep_list:
			out_records.append(record)
	SeqIO.write(out_records, outfasta_path, "fasta")
	return outfasta_path

keep_list = ["GCA_016294985.1","GCA_019057385.1","GCA_016292335.1", "GCA_019056805.1","GCA_016840905.1","GCA_001940725.1","GCA_002728275.1","GCA_016839295.1","GCA_001940645.1","GCA_016840025.1","GCA_016840425.1","Heimdallarchaeum_endolithica_PR6","GCA_019057815.1","GCA_008000775.1","GCA_001940655.1","GCA_019057795.1","GCA_019058015.1","GCA_019058365.1","GCA_019058445.1","GCA_019058515.1","GCA_005191425.1","GCA_019058315.1","GCA_011365055.1","GCA_014729935.1","GCA_001940665.1","GCA_016839265.1","GCA_019058495.1","GCA_016839805.1","GCA_004524445.1","GCA_004524565.1","GCA_008080745.1","GCA_011364985.1","GCA_016840825.1","GCA_011362025.1","GCA_016840465.1","GCA_018901755.1","GCA_015521825.1","GCA_016198755.1","GCA_001784635.1","GCA_011333035.1","GCA_017608955.1","GCA_018304545.1","GCA_011335085.1","GCA_016181005.1","GCA_018304615.1","GCA_016202815.1","GCA_016931255.1","GCA_015520105.1","GCA_016932215.1","GCA_018816245.1","GCA_000806115.1","GCA_015522745.1","GCA_016187335.1","GCA_016198685.1","GCA_018920315.1","GCA_002785505.1","GCA_001742785.1","GCA_002254565.1","GCA_003663045.1","GCA_016931955.1","GCA_014727915.1","GCA_001723855.1","GCA_016935655.1","GCA_019429125.1","GCA_018897155.1","GCA_015520605.1","GCA_009392915.1","GCA_003553825.1","GCA_018304505.1","GCA_017608805.1","GCA_016205145.1","GCA_017610205.1","GCA_000830275.1","GCA_000402355.1","GCA_016187745.1","GCA_016699555.1","GCA_018304425.1","GCA_015521515.1","GCA_003661685.1","GCA_015522845.1","GCA_016926295.1","GCA_016212395.1","GCA_902384795.1","GCA_902385155.1","GCA_013426015.1","GCA_002204695.1","GCA_002214165.1","GCA_014874295.1","GCA_902385515.1","GCA_903884115.1","GCA_001871475.1","GCA_011362975.1","GCA_902384585.1","GCA_016212525.1","GCA_016935455.1","GCA_018304385.1","GCA_018812625.1","GCA_903828955.1","GCA_903835385.1","GCA_002792955.1","GCA_011358415.1","GCA_016188965.1","GCA_018819225.1","GCA_902384935.1","GCA_016194335.1","GCA_017608385.1","GCA_902385255.1","GCA_014729335.1","GCA_007130955.1","GCA_011333755.1","GCA_011364745.1","GCA_000008085.1","GCA_000387965.1","GCA_001552015.1","GCA_003568775.1","GCA_011331665.1","GCA_002762835.1","GCA_018691935.1","GCA_902385655.1","GCA_018650665.1","GCA_902385625.1","GCA_903828205.1","GCA_002763115.1","GCA_016211995.1","GCA_002897655.1","GCA_017609175.1","GCA_017609405.1","GCA_017609755.1","GCA_017991485.1","GCA_018303885.1","GCA_018304175.1","GCA_018653175.1","GCA_018815925.1","GCA_902385635.1","GCA_001786395.1","GCA_017609115.1","GCA_002780285.1","GCA_017609885.1","GCA_018818285.1","GCA_013331705.1","GCA_002763075.1","GCA_018303825.1","GCA_002499655.1","GCA_002503995.1","GCA_015121965.1","GCA_002763265.1","GCA_002687815.1","GCA_013329215.1","GCA_018648525.1","GCA_000806155.1","GCA_000830315.1","GCA_002688355.1","GCA_018302225.1","GCA_018303545.1","GCA_018671245.1","GCA_018829185.1","GCA_000402515.1","GCA_002505585.1","GCA_016188045.1","GCA_014240455.1","GCA_017608345.1","GCA_903878405.1","GCA_002505525.1","GCA_002779235.1","GCA_016203225.1","GCA_017609645.1","GCA_018302815.1","GCA_019323015.1","GCA_018221105.1","GCA_903904885.1","GCA_002762865.1","GCA_001871415.1","GCA_011368255.1","GCA_016192995.1","GCA_013202845.1","GCA_005222965.1","GCA_000830295.1","GCA_016185945.1","GCA_002762785.1","GCA_016185625.1","GCA_018302605.1","GCA_018657845.1","GCA_018671675.1","GCA_018696595.1","GCA_018812765.1","GCA_003695265.1","GCA_016187565.1","GCA_014729995.1","GCA_015519985.1","GCA_016180135.1","GCA_016180195.1","GCA_017608625.1","GCA_018263355.1","GCA_018303285.1","GCA_018303425.1","GCA_018646625.1","GCA_018653045.1","GCA_019322485.1","GCA_019323755.1","GCA_007117065.1","GCA_016927245.1","GCA_016930415.1","GCA_002688315.1","GCA_016935265.1","GCA_018668595.1","GCA_002762985.1","GCA_003599145.1","GCA_000806095.1","GCA_016180285.1","GCA_016935985.1","GCA_018658365.1","GCA_000220355.1","GCA_001761425.1","GCA_009617975.1","Halo_Nar1","GCA_017610385.1","GCA_016432325.1","GCA_003663345.1","GCA_003554845.1","GCA_003663355.1","GCA_016932615.1","GCA_018220935.1","GCA_018220955.1","GCA_018221005.1","GCA_014189685.1","GCA_002502135.1","GCA_002494525.1","GCA_011361855.1","GCA_011367225.1","GCA_001515205.2","GCA_003661465.1","GCA_003555245.1","GCA_000008665.1","GCA_000025285.1","GCA_000025505.1","GCA_000194625.1","GCA_000385565.1","GCA_002011165.1","GCA_900156425.1","GCA_000196895.1","GCA_000023965.1","GCA_000026045.1","GCA_000755225.1","GCA_003730195.1","GCA_007421925.1","GCA_009617995.1","GCA_900100385.1","GCA_900102305.1","GCA_000006805.1","GCA_000336675.1","GCA_000022205.1","GCA_000306765.2","GCA_001282785.1","GCA_002952775.1","GCA_006861655.1","GCA_900107665.1","GCA_900114455.1","GCA_000025625.1","GCA_000230715.3","GCA_000328525.1","GCA_000328685.1","GCA_003430825.1","GCA_900103505.1","GCA_018609935.1","GCA_003021085.1","GCA_003675855.1","GCA_007118975.1","GCA_009889665.1","GCA_000063445.1","GCA_004212075.1","GCA_000015765.1","GCA_000304355.2","GCA_004102725.1","GCA_001571385.1","GCA_000784355.1","GCA_001315945.1","GCA_000017625.1","GCA_017873855.1","GCA_018263335.1","GCA_000021965.1","GCA_000013445.1","GCA_015660865.1","GCA_001914405.1","GCA_002153915.1","GCA_018263395.1","GCA_004211975.1","GCA_004193545.1","GCA_019429385.1","GCA_000685155.1","GCA_000013725.1","GCA_000196655.1","GCA_000328665.1","GCA_000970205.1","GCA_000014945.1","GCA_000204415.1","GCA_000235565.1","GCA_003162615.1","GCA_000711905.1","GCA_016207465.1","GCA_003194425.1","GCA_011049045.1","GCA_001766825.1","GCA_002897955.1","GCA_002011125.1","GCA_003695745.1","GCA_015521895.1","GCA_000012545.1","GCA_000016525.1","GCA_000024185.1","GCA_000404165.1","GCA_002072215.1","GCA_002813695.1","GCA_003491285.1","GCA_018141185.1","GCA_000166095.1","GCA_000008645.1","GCA_003584625.1","GCA_000023985.1","GCA_000017185.1","GCA_000214415.1","GCA_002945325.1","GCA_000007185.1","GCA_001587575.1","GCA_004212155.1","GCA_000007305.1","GCA_000246985.3","GCA_000725425.1","GCA_002214585.1","GCA_015520705.1","GCA_005888755.1","GCA_018396775.1","GCA_018396915.1","GCA_018396755.1","GCA_011367275.1","GCA_002011035.1","GCA_002490245.1","GCA_018396635.1","GCA_001399795.1","GCA_001399805.1","GCA_004376295.1","GCA_011051215.1","GCA_011053435.1","GCA_018396615.1","GCA_018396705.1","GCA_002255025.1","GCA_018396415.1","GCA_002726865.1","GCA_003601775.1","GCA_018396865.1","GCA_017601145.1","GCA_011605725.1","GCA_011041895.1","GCA_003661385.1","GCA_000019605.1","GCA_003947435.1","GCA_003661365.1","GCA_011605825.1","GCA_011362245.1","GCA_004028775.1","GCA_004348015.1","GCA_015660995.1","GCA_011364685.1","GCA_004347915.1","GCA_000270325.1","GCA_002898395.1","GCA_011364235.1","GCA_011364615.1","GCA_013340765.1","GCA_011333845.1","GCA_002011075.1","GCA_015523545.1","GCA_011773305.1","GCA_014361085.1","GCA_016184315.1","GCA_011358735.1","GCA_900248165.1","GCA_000018465.1","GCA_000200715.1","GCA_000220175.2","GCA_000812185.1","GCA_002787055.1","GCA_011771385.1","GCA_016838825.1","GCA_900065925.1","GCA_000303155.1","GCA_001870125.1","GCA_009898475.1","GCA_013114725.1","GCA_016200045.1","GCA_902812495.1","GCA_016871995.1","GCA_003661605.2","Ga0009305","GCA_000398765.1","GCA_015520395.1","GCA_003019535.1","GCA_003019615.1","GCA_002507085.1","GCA_003650925.1","GCA_000011125.1","GCA_003431325.1","GCA_003116855.1","GCA_000015945.1","GCA_000092185.1","GCA_000186365.1","GCA_000258425.1","GCA_009904015.1","GCA_000017945.1","GCA_001481685.1","GCA_000145985.1","GCA_003056265.1","GCA_011337845.1","GCA_015521325.1","GCA_015520265.1","GCA_015521735.1","GCA_015522635.1","GCA_000223395.1","GCA_001462395.1","GCA_000016605.1","GCA_000389735.1","GCA_014648235.1","GCA_900079115.1","GCA_003649305.1","GCA_003650785.1","GCA_000015225.1","GCA_011042215.1","GCA_000018305.1","GCA_000190315.1","GCA_000007225.1","GCA_018335115.1","GCA_903877165.1","GCA_002838995.1","GCA_011049295.1","GCA_008297685.1","GCA_014361195.1","GCA_002502685.1","GCA_002838935.1","GCA_016928095.1","GCA_000246735.1","GCA_002494605.1","GCA_002503015.1","GCA_003602415.1","GCA_012959275.1","GCA_016777175.1","GCA_002505775.1","GCA_003324635.1","GCA_016845365.1","GCA_018645625.1","GCA_018650285.1","GCA_002509225.1","GCA_004195655.1","GCA_902627615.1","GCA_016207515.1","GCA_000025665.1","GCA_003649915.1","GCA_003649695.1","GCA_013415715.1","GCA_000308215.1","GCA_000300255.2","GCA_002506325.1","GCA_002506995.1","GCA_003555025.1","GCA_009780575.1","GCA_009911715.1","GCA_013415865.1","GCA_003552585.1","GCA_011331255.1","GCA_004377185.1","GCA_016214785.1","GCA_001856825.1","GCA_000195915.1","GCA_000496135.1","GCA_002078355.1","GCA_002204655.1","GCA_002204705.1","GCA_002503205.1","GCA_014646795.1","GCA_014874365.1","GCA_900090055.1","GCA_018818785.1","GCA_002503985.1","GCA_002127415.1","GCA_005223185.1","GCA_013360195.1","GCA_000178955.2","GCA_011053475.1","GCA_000226295.1","GCA_000242615.3","GCA_001664505.1","GCA_000687145.1","GCA_011362725.1","GCA_012103255.1","GCA_001618865.1","GCA_000348785.1","GCA_002418265.1","GCA_005696695.1","GCA_004322855.1","GCA_900105925.1","GCA_900104725.1","GCA_002214185.1","GCA_003589885.1","GCA_900143685.1","GCA_014360655.1","GCA_003568865.1","GCA_000025265.1","GCA_012837825.1","GCA_005223085.1","GCA_005223095.1","GCA_003648815.1","GCA_900142435.1","GCA_000021545.1","GCA_000185805.1","GCA_002973605.1","GCA_011370625.1","GCA_000427095.1","GCA_000724625.1","GCA_013314775.1","GCA_003599815.1","GCA_012729785.1","GCA_002440765.1","GCA_000246855.1","GCA_900176595.1","GCA_900105165.1","GCA_000020525.1","GCA_000258405.1","GCA_000013045.1","GCA_000196175.1","GCA_002430665.1","GCA_001748245.1","GCA_004102645.1","GCA_011373285.1","GCA_903898825.1","GCA_002897695.1","GCA_003228585.1","GCA_013151915.1","GCA_015775515.1","GCA_002383355.1","GCA_012520575.1","GCA_012517755.1","GCA_000284335.1","GCA_012517765.1","GCA_001886815.1","GCA_008501795.1","GCA_013150955.1","GCA_003711085.1","GCA_000242915.2","GCA_005843985.1","GCA_000517565.1","GCA_000194135.1","GCA_013152955.1","GCA_003650255.1","GCA_002841685.1","GCA_003553445.1","GCA_000008725.1","GCA_000750955.1","GCA_011064725.1","GCA_011064935.1","GCA_001545115.1","GCA_011064965.1","GCA_000237205.1","GCA_001303765.1","GCA_001796255.1","GCA_011064875.1","GCA_011065125.1","GCA_000092785.1","GCA_003339615.1","GCA_000199675.1","GCA_001306175.1","GCA_000281175.1","GCA_012729455.1","GCA_014360755.1","GCA_000017805.1","GCA_000025005.1","GCA_001953175.1","GCA_003228115.1","GCA_011047455.1","GCA_011053995.1","GCA_008838325.1","GCA_009392805.1","GCA_009392005.1","GCA_004297775.1","GCA_004208415.1","GCA_011053965.1","GCA_000177635.2","GCA_000469585.1","GCA_014203025.1","GCA_000146065.1","GCA_002742885.1","GCA_014382685.1","GCA_000020945.1","GCA_013178255.1","GCA_013153035.1","GCA_011055945.1","GCA_011056185.1","GCA_011057335.1","GCA_000155555.1","GCA_000019485.1","GCA_000464785.1","GCA_000204075.1","GCA_000346485.2","GCA_000484535.1","GCA_001870225.1","GCA_000353285.1","GCA_000015645.1","GCA_000195975.1","GCA_000013225.1","GCA_002075285.3","GCA_000317065.1","GCA_000010065.1","GCA_000018105.1","GCA_003503675.1","GCA_003149375.1","GCA_000010985.1","GCA_000025725.1","GCA_000218625.1","GCA_000376665.1","GCA_004684245.1","GCA_000092425.1","GCA_000513475.1","GCA_003506475.1","GCA_003366055.1","GCA_001871075.1","GCA_011389435.1","GCA_001871015.1","GCA_003135135.1","GCA_903893315.1","GCA_011329495.1","GCA_011367125.1","GCA_000143965.1","GCA_000186885.1","GCA_001577525.1","GCA_000266945.1","GCA_000013405.1","GCA_000014965.1","GCA_000512235.1","GCA_014075295.1","GCA_004213355.1","GCA_002898375.1","GCA_000020965.1","GCA_000021645.1","GCA_002878375.1","GCA_005882775.1","GCA_003139695.1","GCA_003162415.1","GCA_011042595.1","GCA_011049115.1","GCA_013153415.1","GCA_012518435.1","GCA_012840595.1","GCA_012839755.1","GCA_011334575.1","GCA_012839925.1","GCA_014360335.1","GCA_001777915.1","GCA_001781595.1","GCA_002412795.1","GCA_903844735.1","GCA_011357805.1","GCA_005893275.1","GCA_001800135.1","GCA_000020145.1","GCA_001027545.1","GCA_002412545.1","GCA_003168375.1","GCA_902790465.1","GCA_902764865.1","GCA_013335425.1","GCA_003152075.1","GCA_003163255.1","GCA_001618605.1","GCA_002030045.1","GCA_002436025.1","GCA_000474745.1","GCA_900167415.1","GCA_001797525.1","GCA_903861835.1","GCA_001780375.1","GCA_903928075.1","GCA_000024285.1","GCA_900660745.1","GCA_001278705.1","GCA_003925875.1","GCA_000702585.1","GCA_007066085.1","GCA_000756715.2","GCA_000510645.1","GCA_002005165.1","GCA_000237085.1","GCA_008705175.1","GCA_002874775.1","GCA_002201475.1","GCA_002998295.1","GCA_004101785.1","GCA_000012865.1","GCA_013178305.1","GCA_000328625.1","GCA_001544015.1","GCA_900176005.1","GCA_000020005.1","GCA_003367905.1","GCA_900142275.1","GCA_013178125.1","GCA_000009905.1","GCA_000014725.1","GCA_000184705.1","GCA_000016545.1","GCA_000213235.1","GCA_004340685.1","GCA_002313635.1","GCA_003019675.1","GCA_000023905.1","GCA_000695095.2","GCA_013696835.1","GCA_009840115.1","GCA_011367535.1","GCA_003142155.1","GCA_002839855.1","GCA_012730045.1","GCA_002422525.1","GCA_013359265.1","GCA_002403075.1","GCA_903912525.1","GCA_011772205.1","GCA_008501765.1","GCA_011389025.1","GCA_013152225.1","GCA_009841265.1","GCA_000403035.1","GCA_003645885.1","GCA_009840435.1","GCA_903864835.1","GCA_003242895.1","GCA_001771425.1","GCA_004124385.1","GCA_004402915.1","GCA_002347855.1","GCA_011359065.1","GCA_000091165.1","GCA_011058515.1","GCA_011330975.1","GCA_000739535.1","GCA_002748425.1","GCA_003258315.1","GCA_000165485.1","GCA_002305895.1","GCA_000024805.1","GCA_002343915.1","GCA_001931535.1","GCA_903842345.1","GCA_011055735.1","GCA_000341545.2","GCA_009873655.1","GCA_002500605.1","GCA_000755505.1","GCA_001273775.1","GCA_001803795.1","GCA_000020985.1","GCA_001567115.1","GCA_014584505.1","GCA_013177805.1","GCA_011334725.1","GCA_013626165.1","GCA_003485765.1","GCA_013203315.1","GCA_004102945.1","GCA_002421665.1","GCA_013335095.1","GCA_002840305.1","GCA_011047195.1","GCA_004297205.1","GCA_001818495.1","GCA_001818315.1","GCA_007375725.1","GCA_903889905.1","GCA_000997185.1","GCA_001780055.1","GCA_004563595.2","GCA_002401425.1","GCA_001430805.1","GCA_002839505.1","GCA_001029795.1","GCA_001776935.1","GCA_001029755.1","GCA_001029675.1","GCA_001790195.1","GCA_002794035.1","GCA_000995965.1","GCA_001819495.1","GCA_003599755.1","GCA_003599335.1","GCA_001029635.1","GCA_000803625.1","GCA_004136275.1","GCA_004138405.1","GCA_004297735.1","GCA_011332705.1","GCA_001029735.1","GCA_000503835.1","GCA_900232105.1","GCA_012728835.1","GCA_011371585.1","GCA_009691765.1","GCA_009002475.1","GCA_000284115.1","GCA_002007645.1","GCA_008065095.1","GCA_000196115.1","GCA_014193115.1","GCA_007751475.1","GCA_011334435.1","GCA_003645735.1","GCA_002709695.1","GCA_006738645.1","GCA_002117145.1","GCA_000144605.1","GCA_000013025.1","GCA_000152825.2","GCA_007197755.1","GCA_002717245.1","GCA_002722055.1","GCA_002746255.1","GCA_000427665.1","GCA_002937855.1","GCA_001898075.1","GCA_000742475.1","GCA_000469665.2","GCA_000515255.1","GCA_000226315.1","GCA_004210305.1","GCA_000293845.2","GCA_000012345.1","GCA_000163555.2","GCA_900167455.1","GCA_902799835.1","GCA_000021745.1","GCA_000143145.1","GCA_000192745.1","GCA_000155675.2","GCA_003324715.1","GCA_003970735.1","GCA_002938315.1","GCA_000013085.1","GCA_003403095.1","GCA_000746585.2","GCA_000166935.1","GCA_002787635.1","GCA_002291925.1","GCA_009784235.1","GCA_000616095.1","GCA_002722885.1","GCA_000375545.1","GCA_000186705.2","GCA_009768975.1","GCA_000299935.1","GCA_000264455.2","GCA_002937655.1","GCA_002937675.1","GCA_002937625.1","GCA_002691145.1","GCA_002937495.1","GCA_002422365.1","GCA_002436405.1","GCA_002422845.1","GCA_001767855.1","GCA_002728255.1","GCA_011523425.1","GCA_009780035.1","GCA_002355415.1","GCA_000021485.1","GCA_003967195.1","GCA_000245015.1","GCA_002708265.1","GCA_004209755.1","GCA_900637305.1","GCA_000227745.3","GCA_000007765.2","GCA_003751635.1","GCA_902459485.1","GCA_000321415.2","GCA_013267215.1","GCA_002215215.1","GCA_900187095.1","GCA_004421105.1","GCA_001293165.1","GCA_900103345.1","GCA_001579945.1","GCA_001447805.1","GCA_900101365.1","GCA_000419525.1","GCA_001677435.1","GCA_007556775.1","GCA_000014865.1","GCA_002109495.1","GCA_001872725.1","GCA_001873795.1","GCA_002795805.1","GCA_011388275.1","GCA_011363065.1","GCA_011046415.1","GCA_011329245.1","GCA_002069365.1","GCA_002791075.1","GCA_003647695.1","GCA_011773985.1","GCA_001774505.1","GCA_003327425.1","GCA_009917695.1","GCA_012520995.1","GCA_014382365.1","GCA_002995645.1","GCA_001783715.1","GCA_001790855.1","GCA_001790865.1","GCA_003695725.1","GCA_000092845.1","GCA_900112165.1","GCA_001829315.1","GCA_000266885.1","GCA_000143985.1","GCA_000236685.1","GCA_000184345.2","GCA_000507245.1","GCA_008329945.1","GCA_013360565.1","GCA_007132505.1","GCA_003290465.1","GCA_001443005.1","GCA_011375965.1","GCA_000165795.1","GCA_000522425.1","GCA_900079095.1","GCA_003696125.1","GCA_000212395.1","GCA_003057965.1","GCA_011374175.1","GCA_003648675.1","GCA_001547735.1","GCA_013153205.1","GCA_009936215.1","GCA_000023325.1","GCA_004117075.1","GCA_003648225.1","GCA_012514975.1","GCA_002366995.1","GCA_003697085.1","GCA_001871695.1","GCA_002780065.1","GCA_005239945.1","GCA_003498085.1","GCA_003485015.1","GCA_002085385.1","GCA_011371545.1","GCA_002428525.1","GCA_011368175.1","GCA_002069885.1","GCA_002435745.1","GCA_001017655.1","GCA_004555175.1","GCA_012103575.1","GCA_002429065.1","GCA_000170755.1","GCA_000025905.1","GCA_000172155.1","GCA_001791795.1","GCA_002069765.1","GCA_002423385.1","GCA_011329265.1","GCA_004377355.1","GCA_013177935.1","GCA_900498245.1","GCA_000447245.1","GCA_002791595.1","arch_EP01087","arch_EP01091","arch_EP01094","arch_EP01104","arch_EP00727","arch_EP00023","arch_EP01113","arch_EP00026","arch_EP01114","arch_EP01117","arch_EP00029","arch_EP01125","arch_EP01127","arch_EP01130","arch_EP00031","arch_EP01086","arch_EP00033","arch_EP00039","arch_EP00120","arch_EP00134","arch_EP00145","arch_EP00150","arch_EP00857","arch_EP00129","arch_EP00131","arch_EP00157","arch_EP00865","arch_EP01134","arch_EP00103","arch_EP00104","arch_EP00083","arch_EP00067","arch_EP00072","arch_EP00110","arch_EP00794","arch_EP00057","arch_EP00098","arch_EP00107","arch_EP00119","arch_EP00127","arch_EP00159","arch_EP00162","arch_EP00163","arch_EP00002","arch_EP00004","arch_EP00164","arch_EP00202","arch_EP00852","arch_EP00738","arch_EP00229","arch_EP00206","arch_EP00210","arch_EP00247","arch_EP00248","arch_EP00260","arch_EP00269","arch_EP00895","arch_EP00271","arch_EP00741","arch_EP00736","arch_EP00167","arch_EP00176","arch_EP00185","arch_EP00279","arch_EP00802","arch_EP00298","arch_EP00300","arch_EP00314","arch_EP00900","arch_EP00379","arch_EP00333","arch_EP00810","arch_EP00820","arch_EP00390","arch_EP00742","arch_EP00927","arch_EP00931","arch_EP00397","arch_EP00454","arch_EP00455","arch_EP00466","arch_EP00457","arch_EP00808","arch_EP00473","arch_EP01083","arch_EP01084","arch_EP00924","arch_EP00513","arch_EP00813","arch_EP00797","arch_EP01082","arch_EP00609","arch_EP00611","arch_EP00749","arch_EP00750","arch_EP00503","arch_EP00753","arch_EP00656","arch_EP01062","arch_EP00667","arch_EP00671","arch_EP00681","arch_EP00759","arch_EP01027","arch_EP00761","arch_EP00686","arch_EP01080","arch_EP00762","arch_EP01028","arch_EP00696","arch_EP00697","arch_EP00698","arch_EP01146","arch_EP00770","arch_EP00771"]
indir = "/Users/vl18625/work/euk/markers_euks/nina_markers/abe/87_markers/linsi_bmge/"
outdir = "/Users/vl18625/work/euk/markers_euks/nina_markers/abe/87_markers/linsi_bmge_filtered_29_06_23/"
# filter_fastas_keep_sp(keep_list, indir, outdir, species_id_delimiter="-", euk=False, abce=False)

exclude_list = ["Idunnarchaeote_GBS17", "Idunnarchaeote_GBS24"]
indir="/Users/vl18625/work/euk/markers_euks/nina_markers/01_07_23/archaea/faa_unfiltered/"
outdir="/Users/vl18625/work/euk/markers_euks/nina_markers/01_07_23/archaea/faa_no_idun/"
filter_fastas_exclude_sp(exclude_list, indir, outdir, species_id_delimiter="-")
