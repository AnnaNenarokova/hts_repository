#!/usr/bin/python3
import os
import subprocess
from Bio import SeqIO
from Bio.Blast import NCBIXML

os.chdir('/home/kika/tara/')
contigs = SeqIO.parse('CENF01.fasta', 'fasta')
circular = open('circular.fa', 'w')
candidates = open('candidates.fa', 'w')
non_circ = open('non_circular.fa', 'w')
short_long = open('short_long.fa', 'w')
repeats_out = open('repeats.fa', 'w')
# out_best = open('best_blast.tsv', 'w')
# out_blast = open('blast.tsv', 'w')

print('Searching for repeats in sequences')

# 1) search for the beginning repeat at the end of the conting
# 2) constrain the length of the contig
# 3) search for the beginning repeat in the second half of the contig + search for the last repeat in the
cand_dict = {}
circ_dict = {}
nc_dict = {}
for contig in contigs:
	print(contig.description)
	#ssearch for the beginning repeat at the end of the conting
	for i in range(len(contig.seq)):
		if contig.seq.count(contig.seq[0:i+1]) > 1:
			repeat = str(contig.seq[0:i+1])
		i += 1
	if len(repeat) >= 8 and repeat == contig.seq[-len(repeat):]:
		circ_dict[contig.description] = contig.seq
		repeats_out.write('>{}_TR@{}\n{}\n'.format(contig.description, repeat, 
			contig.seq[int(len(contig.seq)/2):]))

	if contig.description not in circ_dict:
		if len(contig.seq) > 15000 and len(contig.seq) < 100000:
			#search for the beginning repeat longer than 15bp and present in the second half of the contig
			for i in range(len(contig.seq)):
				if contig.seq.count(contig.seq[0:i+1]) > 1:
					repeat = str(contig.seq[0:i+1])
				i += 1
			if len(repeat) >= 15 and repeat in contig.seq[int(len(contig.seq)/2):]:
				cand_dict[contig.description] = contig.seq
				repeats_out.write('>{}_BR@{}\n{}\n'.format(contig.description, repeat, 
					contig.seq[int(len(contig.seq)/2):]))

			#search for the last repeat longer than 15bp and present in the first half of the contig
			for i in range(len(contig.seq)-1, -1, -1):
				if contig.seq.count(contig.seq[i:]) > 1:
					repeat = str(contig.seq[i:])
				i += 1
			if len(repeat) >= 15 and repeat in contig.seq[:int(len(contig.seq)/2)]:
				cand_dict[contig.description] = contig.seq
				repeats_out.write('>{}_LR@{}\n{}\n'.format(contig.description, repeat,
					contig.seq[:int(len(contig.seq)/2)]))

			if contig.description in cand_dict:
				pass
			else:
				nc_dict[contig.description] = contig.seq
		else:
			short_long.write('>{}\n{}\n'.format(contig.description, contig.seq))

for key, value in cand_dict.items():
	candidates.write('>{}\n{}\n'.format(key, value))
for key, value in circ_dict.items():
	circular.write('>{}\n{}\n'.format(key, value))
for key, value in nc_dict.items():
	non_circ.write('>{}\n{}\n'.format(key, value))

circular.close()
candidates.close()
non_circ.close()
short_long.close()
repeats_out.close()


# print('Creating BLASTable database')

# db = 'circular.fa'
# db_type = 'nucl'
# subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, db_type), shell=True)

# print('Database ready')
# print('Starting BLAST')

# cmd = 'tblastn'
# query = 'proteins.fasta'
# output = 'blast.xml'
# evalue = 10
# outfmt = 5
# word_size = 3
# threads = 4
# subprocess.call('{} -query {} -db {} -out {} -evalue {} -outfmt {} -word_size {} -num_threads {}'.format(
# 		cmd, query, db, output, evalue, outfmt, word_size, threads), shell=True)

# print('BLAST done')
# print('writing results to tables')

# result_handle = open(output)
# blast_records = NCBIXML.parse(result_handle)

# out_blast.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format('qseqid', 'qlen', 'sseqid', 'slen', 
# 	'alen', 'evalue', 'pident', 'bitscore', 'mismatch', 'gaps', 'qstart', 'qend', 'sstart', 'send', 'alen_qlen', 
# 	'alen_slen'))
# out_best.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format('qseqid', 'qlen', 'sseqid', 'slen', 
# 	'alen', 'evalue', 'pident', 'bitscore', 'mismatch', 'gaps', 'qstart', 'qend', 'sstart', 'send', 'alen_qlen', 
# 	'alen_slen'))

# for record in blast_records:
# 	try:
# 		best_hit = record.alignments[0].hsps[0]
# 		mismatches = best_hit.align_length - (best_hit.gaps + best_hit.positives)
# 		alen_qlen = best_hit.align_length/record.query_length
# 		alen_slen = best_hit.align_length/record.alignments[0].length
# 		out_best.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
# 			record.query, record.query_length, record.alignments[0].hit_id, record.alignments[0].length, 
# 			best_hit.align_length, best_hit.expect, best_hit.identities, best_hit.bits, mismatches, 
# 			best_hit.gaps, best_hit.query_start, best_hit.query_end, best_hit.sbjct_start, best_hit.sbjct_end, 
# 			alen_qlen, alen_slen))
# 		for aln in record.alignments:
# 			for hsp in aln.hsps:
# 				mismatches = hsp.align_length - (hsp.gaps + hsp.positives)
# 				alen_qlen = hsp.align_length/record.query_length
# 				alen_slen = hsp.align_length/aln.length
# 				out_blast.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
# 					record.query, record.query_length, aln.hit_id, aln.length, hsp.align_length, hsp.expect, 
# 					hsp.identities, hsp.bits, mismatches, hsp.gaps, hsp.query_start, hsp.query_end, hsp.sbjct_start, 
# 					hsp.sbjct_end, alen_qlen, alen_slen))
# 	except:
# 		out_blast.write('{}\t{}\t{}\n'.format(record.query, record.query_length, '***no hit found***'))
# 		out_best.write('{}\t{}\t{}\n'.format(record.query, record.query_length, '***no hit found***'))
# out_best.close()
# out_blast.close()