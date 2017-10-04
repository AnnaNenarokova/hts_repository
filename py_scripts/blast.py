#!/usr/bin/python3
from Bio.Blast import NCBIXML
from Bio.Blast.Applications import NcbiblastxCommandline

print('starting BLAST')
blast_cline = NcbiblastxCommandline(cmd='tblastn', 
									query='/media/4TB1/blastocrithidia/kika_workdir/p57_trinity_translated.fasta', 
									db='/media/4TB1/blastocrithidia/kika_workdir/PRJNA284294_trinity.fasta', 
									out='/media/4TB1/blastocrithidia/kika_workdir/bexlh_blast.xml',
									evalue=10,
									outfmt=5,
									word_size=3,
									num_threads=30)
stdout, stderr = blast_cline()
print('BLAST done')
print('writing BLAST results to tables')

result_handle = open('/media/4TB1/blastocrithidia/kika_workdir/bexlh_blast.xml')
blast_records = NCBIXML.parse(result_handle)
output = open('/media/4TB1/blastocrithidia/kika_workdir/bexlh_blast.xlsx', 'w')
out_best = open('/media/4TB1/blastocrithidia/kika_workdir/bexlh_best_blast.xlsx', 'w')

output.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format('qseqid', 'qlen', 'sseqid', 'slen', 
	'alen', 'evalue', 'pident', 'bitscore', 'mismatch', 'gaps', 'qstart', 'qend', 'sstart', 'send', 'alen_qlen', 
	'alen_slen'))
out_best.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format('qseqid', 'qlen', 'sseqid', 'slen', 
	'alen', 'evalue', 'pident', 'bitscore', 'mismatch', 'gaps', 'qstart', 'qend', 'sstart', 'send', 'alen_qlen', 
	'alen_slen'))

for record in blast_records:
	try:
		best_hit = record.alignments[0].hsps[0]
		mismatches = best_hit.align_length - (best_hit.gaps + best_hit.positives)
		alen_qlen = best_hit.align_length/record.query_length
		alen_slen = best_hit.align_length/record.alignments[0].length
		out_best.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
			record.query, record.query_length, record.alignments[0].hit_id, record.alignments[0].length, 
			best_hit.align_length, best_hit.expect, best_hit.identities, best_hit.bits, mismatches, 
			best_hit.gaps, best_hit.query_start, best_hit.query_end, best_hit.sbjct_start, best_hit.sbjct_end, 
			alen_qlen, alen_slen))
		for aln in record.alignments:
			for hsp in aln.hsps:
				mismatches = hsp.align_length - (hsp.gaps + hsp.positives)
				alen_qlen = hsp.align_length/record.query_length
				alen_slen = hsp.align_length/aln.length
				output.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
					record.query, record.query_length, aln.hit_id, aln.length, hsp.align_length, hsp.expect, 
					hsp.identities, hsp.bits, mismatches, hsp.gaps, hsp.query_start, hsp.query_end, hsp.sbjct_start, 
					hsp.sbjct_end, alen_qlen, alen_slen))
	except:
		output.write('{}\t{}\t{}\n'.format(record.query, record.query_length, '***no hit found***'))
		out_best.write('{}\t{}\t{}\n'.format(record.query, record.query_length, '***no hit found***'))
out_best.close()
output.close()