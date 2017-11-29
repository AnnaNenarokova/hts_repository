#!/usr/bin/python3
from Bio import SeqIO
from Bio.Blast import NCBIXML

fasta = SeqIO.parse('/home/kika/programs/blast-2.5.0+/bin/p57_DNA_scaffolds.fa', 'fasta')
# nt_out = open('/home/kika/MEGAsync/blasto_project/genes/replication/p57/p57_repl_nt.txt', 'w')
result_handle = open('/home/kika/MEGAsync/blasto_project/genes/replication/p57/p57_repl.xml')
blast_records = NCBIXML.parse(result_handle)

gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'B', 'TAG':'Z',
    'TGC':'C', 'TGT':'C', 'TGA':'J', 'TGG':'W'}

def translation(sequence):
    cut_seq = []
    for i in range(0,len(sequence)-2,3):
        cut_seq.append(sequence[i:i+3])
    aa = []
    for codon in cut_seq:
        if 'N' in codon:
            aa.append('X')
        else:
            aa.append(gencode[codon])
    return ''.join(aa)

def blast_parser(blast_records):
	result = {}
	for record in blast_records:
		best = record.alignments[0]
		min_sstart = False
		max_send = False
		min_qstart = False
		max_qend = False
		frame = best.hsps[0].frame[1]
		frame_state = ''
		if frame < 0:
			frame_state = 0
		else:
			frame_state = 1
		if best.hsps[0].expect > 0.01:
			print(record.query + '___too high evalue')
		else:
			for hsp in best.hsps:
				hsp_state = ''
				if hsp.frame[1] < 0:
					hsp_state = 0
				else:
					hsp_state = 1
				if hsp_state == frame_state:
					if not min_qstart:
						min_qstart = hsp.query_start
						if frame in [1, 2, 3]:
							min_sstart = best.hsps[0].sbjct_start
						else:
							min_sstart = best.hsps[0].sbjct_end
					if not max_qend:
						max_qend = hsp.query_end
						if frame in [1, 2, 3]:
							max_send = best.hsps[0].sbjct_end
						else:
							max_send = best.hsps[0].sbjct_start
					if min_qstart > hsp.query_start:
						min_qstart = hsp.query_start
						if frame in [1, 2, 3]:
							min_sstart = hsp.sbjct_start
						else:
							min_sstart = hsp.sbjct_end
					if max_qend < hsp.query_end:
						max_qend = hsp.query_end
						if frame in [1, 2, 3]:
							max_send = hsp.sbjct_end
						else:
							max_send = hsp.sbjct_start
				else:
					print(record.query + '___frames do not correspond')
			if frame in [1, 2, 3]:
				result[best.hit_id] = [min_sstart, max_send, frame, record.query, record.query_length, min_qstart, max_qend]
			else:
				result[best.hit_id] = [max_send, min_sstart, frame, record.query, record.query_length, min_qstart, max_qend]
	return result

blast_dict = blast_parser(blast_records)
# print(blast_dict)

for contig in fasta:
	if contig.name in blast_dict.keys():
		seq_start = blast_dict[contig.name][0]
		seq_end = blast_dict[contig.name][1]
		frame = blast_dict[contig.name][2]
		ref_name = blast_dict[contig.name][3]
		ref_length = blast_dict[contig.name][4]
		ref_start = blast_dict[contig.name][5]
		ref_end = blast_dict[contig.name][6]
		ref_dif = ref_length - ref_end
		if frame in [1, 2, 3]:
			if ref_start == 1:
				if contig.seq[seq_start-1:seq_start+2] == 'M':
					seq_start = seq_start-1
				else:
					while translation(contig.seq[seq_start-1:seq_start+2]) != 'M':
						if seq_start > 3:
							seq_start = (seq_start-1) - 3
						else:
							seq_start = seq_start-1
					else:
						seq_start = seq_start-1
			else:
				while translation(contig.seq[seq_start-(3*ref_start)-1:seq_start-(3*ref_start)+2]) != 'M':
					if seq_start > 3*ref_start - 3:
						seq_start = seq_start-(3*ref_start)-1 - 3
					else:
						seq_start = seq_start-(3*ref_start)-1
				else:
					seq_start = seq_start-(3*ref_start)-1
			if ref_end == ref_length:
				if contig.seq[seq_end-4:seq_end-1] == 'B':
					seq_end = seq_end-1
				else:
					while translation(contig.seq[seq_end-4:seq_end-1]) != 'B':
						if seq_end < len(contig.seq):
							seq_end = (seq_end-1) + 3
						else:
							seq_end = seq_end-1
					else:
						seq_end = seq_end-1
			else:
				print(contig.name + '_1')
				while translation(contig.seq[seq_end+(3*ref_dif)-4:seq_end+(3*ref_dif)-1]) != 'B':
					print(contig.name + '_2')
					if len(contig.seq) < seq_end + (3*ref_dif) + 3:
						print(contig.name + '_3')
						seq_end = seq_end+(3*ref_dif)-1 + 3
					else:
						print(contig.name + '_4')
						seq_end = seq_end+(3*ref_dif)-1
				else:
					print(contig.name + '_5')
					seq_end = seq_end+(3*ref_dif)-1
			print('{}_____{}_{}'.format(contig.name, contig.seq[seq_start:seq_start+3], contig.seq[seq_end-3:seq_end]))
			# print('{}_____{}'.format(contig.name, contig.seq[seq_start:seq_start+3]))
		else:
			print(contig.name + '_____reverse')
	else:
		pass