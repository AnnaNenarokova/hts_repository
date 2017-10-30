#!/usr/bin/python3
from Bio.Blast import NCBIXML
from Bio.Blast.Applications import NcbiblastxCommandline

print('running BLAST')
blast_cline = NcbiblastxCommandline(cmd='tblastn', 
									query='/home/kika/MEGAsync/blasto_project/genes/tRNA-synthetases/TiaS/Tias.fasta', 
									db='/home/kika/programs/blast-2.5.0+/bin/jac_raw_reads.fasta', 
									out='/home/kika/MEGAsync/blasto_project/genes/tRNA-synthetases/TiaS/jac_tblastn_reads.xml',
									evalue=10,
									outfmt=5,
									word_size=3,
									num_threads=4)
stdout, stderr = blast_cline()
print('BLAST done')
print('writing BLAST results to tables')

result_handle = open('/home/kika/MEGAsync/blasto_project/genes/tRNA-synthetases/TiaS/jac_tblastn_reads.xml')
blast_records = NCBIXML.parse(result_handle)
output = open('/home/kika/MEGAsync/blasto_project/genes/tRNA-synthetases/TiaS/jac_tblastn_reads.xlsx', 'w')
out_best = open('/home/kika/MEGAsync/blasto_project/genes/tRNA-synthetases/TiaS/jac_tblastn_reads_best.xlsx', 'w')

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