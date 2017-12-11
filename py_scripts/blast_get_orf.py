#!/usr/bin/python3
#!!! Check parsing record.query in the end of blast_parser function !!!
from Bio import SeqIO
import re
from Bio.Blast import NCBIXML

fasta = SeqIO.parse('/home/kika/programs/blast-2.5.0+/bin/jaculum_scaffolds_transc.fasta', 'fasta')
nt_out = open('/home/kika/MEGAsync/blasto_project/genes/replication/jac/jac_repl_nt.txt', 'w')
aa_out = open('/home/kika/MEGAsync/blasto_project/genes/replication/jac/jac_repl_aa.txt', 'w')
err_out = open('/home/kika/MEGAsync/blasto_project/genes/replication/jac/jac_repl_errors.txt', 'w')
result_handle = open('/home/kika/MEGAsync/blasto_project/genes/replication/jac/jac_repl.xml')
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
    'TAC':'Y', 'TAT':'Y', 'TAA':'B', 'TAG':'B',
    'TGC':'C', 'TGT':'C', 'TGA':'B', 'TGG':'W'}

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
	errors = []
	for record in blast_records:
		best = record.alignments[0]
		min_sstart = False
		max_send = False
		min_qstart = False
		max_qend = False
		frame = best.hsps[0].frame[1]
		if best.hsps[0].expect > 0.01:
			err_out.write('{}:\ttoo high evalue\n'.format(record.query.split(':')[0]))
		else:
			for hsp in best.hsps:
				if frame == hsp.frame[1]:
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
					errors.append(record.query.split(':')[0])
					if frame in [1, 2, 3]:
						min_sstart = best.hsps[0].sbjct_start
						max_send = best.hsps[0].sbjct_end
					else:
						min_sstart = best.hsps[0].sbjct_end
						max_send = best.hsps[0].sbjct_start
			if frame in [1, 2, 3]:
				result[best.hit_id] = [min_sstart, max_send, frame, record.query.split(':')[0], 
					record.query_length, min_qstart, max_qend]
			else:
				result[best.hit_id] = [max_send, min_sstart, frame, record.query.split(':')[0], 
					record.query_length, min_qstart, max_qend]
	errors = set(errors)
	for i in errors:
		err_out.write('{}:\thsps frames do not correspond\n'.format(i))
	return result

blast_dict = blast_parser(blast_records)
# print(blast_dict)

for contig in fasta:
	if contig.name in blast_dict.keys():
		frame = blast_dict[contig.name][2]
		ref_name = blast_dict[contig.name][3]
		if frame in [1, 2, 3]:
			print(contig.name + '_____forward')
			seq_start = blast_dict[contig.name][0]-1
			seq_end = blast_dict[contig.name][1]
			prev_stop = seq_start - 3
			if prev_stop > 2:
				while translation(contig.seq[prev_stop:prev_stop+3]) != 'B':
					prev_stop = prev_stop - 3
				else:
					prev_stop = prev_stop
			else:
				prev_stop = prev_stop
			if 'M' not in translation(contig.seq[prev_stop:seq_start-1]):
				if translation(contig.seq[seq_start:seq_start+3]) == 'M':
					new_start = seq_start
				else:
					new_start = prev_stop + 3
			else:
				new_start = prev_stop + 3*translation(contig.seq[prev_stop:seq_start-1]).find('M')
			if seq_end < len(reverse) - 3:
				if translation(contig.seq[seq_end:seq_end+3]) == 'B':
					seq_end = seq_end
				else:
					while translation(contig.seq[seq_end:seq_end+3]) != 'B':
						seq_end = seq_end + 3
					else:
						seq_end = seq_end
			else:
				seq_end = seq_end
			nucleotides = contig.seq[new_start:seq_end+3]
			protein = translation(nucleotides)
			nt_out.write('>{}__{}\n{}\n'.format(contig.name, ref_name, nucleotides))
			aa_out.write('>{}__{}\n{}\n'.format(contig.name, ref_name, protein))
		else:
			print(contig.name + '_____reverse')
			reverse = contig.seq.reverse_complement()
			seq_start = len(reverse) - blast_dict[contig.name][1]
			seq_end = len(reverse) - blast_dict[contig.name][0] + 1
			prev_stop = seq_start - 3
			if prev_stop > 2:
				while translation(reverse[prev_stop:prev_stop+3]) != 'B':
					prev_stop = prev_stop - 3
				else:
					prev_stop = prev_stop
			else:
				prev_stop = prev_stop
			if 'M' not in translation(reverse[prev_stop:seq_start-1]):
				if translation(reverse[seq_start:seq_start+3]) == 'M':
					new_start = seq_start
				else:
					new_start = prev_stop + 3
			else:
				new_start = prev_stop + 3*translation(reverse[prev_stop:seq_start-1]).find('M')
			if seq_end < len(reverse) - 3:
				print('here_1')
				if translation(reverse[seq_end:seq_end+3]) == 'B':
					print('here_2')
					seq_end = seq_end
				else:
					print('here_3')
					while translation(reverse[seq_end:seq_end+3]) != 'B':
						print('here_4')
						seq_end = seq_end + 3
					else:
						print('here_5')
						seq_end = seq_end
			else:
				print('here_6')
				seq_end = seq_end
			nucleotides = reverse[new_start:seq_end+3]
			protein = translation(nucleotides)
			nt_out.write('>{}__{}\n{}\n'.format(contig.name, ref_name, nucleotides))
			aa_out.write('>{}__{}\n{}\n'.format(contig.name, ref_name, protein))
	else:
		pass

nt_out.close()
aa_out.close()