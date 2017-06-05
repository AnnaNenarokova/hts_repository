#!/usr/bin/python3
from Bio.Blast import NCBIXML
from Bio.Blast.Applications import NcbiblastxCommandline

blast_cline = NcbiblastxCommandline(cmd='tblastn', 
									query='/home/kika/programs/blast-2.5.0+/bin/input.txt', 
									db='/home/kika/programs/blast-2.5.0+/bin/jaculum_scaffolds.fasta', 
									out='/home/kika/programs/blast-2.5.0+/bin/blast.xml',
									evalue=1, 
									outfmt=5,
									word_size=3)
stdout, stderr = blast_cline()

result_handle = open('/home/kika/programs/blast-2.5.0+/bin/blast.xml')
blast_records = NCBIXML.parse(result_handle)
output = open('/home/kika/programs/blast-2.5.0+/bin/blast_out.xlxs', 'w')
out_best = open('/home/kika/programs/blast-2.5.0+/bin/blast_best_out.xlxs', 'w')

output.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format('qseqid', 'qlen', 'sseqid', 'slen', 
	'alen', 'evalue', 'pident', 'bitscore', 'mismatch', 'gaps', 'qstart', 'qend', 'sstart', 'send', 'alen_qlen', 
	'alen_slen'))
out_best.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format('qseqid', 'qlen', 'sseqid', 'slen', 
	'alen', 'evalue', 'pident', 'bitscore', 'mismatch', 'gaps', 'qstart', 'qend', 'sstart', 'send', 'alen_qlen', 
	'alen_slen'))

for record in blast_records:
	mismatches = record.alignments[0].hsps[0].align_length - (record.alignments[0].hsps[0].gaps + record.alignments[0].hsps[0].positives)
	alen_qlen = record.alignments[0].hsps[0].align_length/record.query_length
	alen_slen = record.alignments[0].hsps[0].align_length/record.alignments[0].length
	out_best.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
		record.query, record.query_length, record.alignments[0].hit_id, record.alignments[0].length, 
		record.alignments[0].hsps[0].align_length, record.alignments[0].hsps[0].expect, 
		record.alignments[0].hsps[0].identities, record.alignments[0].hsps[0].bits, 
		mismatches, record.alignments[0].hsps[0].gaps, record.alignments[0].hsps[0].query_start, 
		record.alignments[0].hsps[0].query_end, record.alignments[0].hsps[0].sbjct_start, 
		record.alignments[0].hsps[0].sbjct_end, alen_qlen, alen_slen))
	for aln in record.alignments:
		for hsp in aln.hsps:
			mismatches = hsp.align_length - (hsp.gaps + hsp.positives)
			alen_qlen = hsp.align_length/record.query_length
			alen_slen = hsp.align_length/aln.length
			output.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
				record.query, record.query_length, aln.hit_id, aln.length, hsp.align_length, hsp.expect, 
				hsp.identities, hsp.bits, mismatches, hsp.gaps, hsp.query_start, hsp.query_end, hsp.sbjct_start, 
				hsp.sbjct_end, alen_qlen, alen_slen))

out_best.close()
output.close()