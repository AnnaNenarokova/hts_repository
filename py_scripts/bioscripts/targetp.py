from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from subprocess32 import call
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from common_helpers.make_outdir import file_from_path, make_outdir, new_file_same_dir
from common_helpers.lookahead import lookahead
from subprocess import Popen, PIPE, STDOUT
import csv

def is_targetp_info(targetp_line):
	garbage_starts = ['### ta', 'Number', 'Cleava', 'Using ', 'Name  ', '------', 'cutoff']
	if targetp_line[:6] in garbage_starts: return False
	else: return True

def use_targetp(f_path, outf_path=False, is_plant=False, txt_out=False):
	targetp_path = '/home/anna/bioinformatics/bioprograms/targetp-1.1/'
	targetp_path += 'targetp'

	out_data = []
	seq_batch = []
	i = 0
	for seqrecord, is_last in lookahead(SeqIO.parse(f_path, "fasta")):
		seq_batch.append(seqrecord.format("fasta"))
		i+=1
		if i == 1000 or is_last:
			seq_batch = '\n'.join(seq_batch)
			targetp = Popen(targetp_path, stdout=PIPE, stdin=PIPE, stderr=PIPE)
			out_data.extend(targetp.communicate(input=seq_batch))
			seq_batch = []
			i = 0

	if txt_out:
		if not outf_path: outf_path = new_file_same_dir(f_path, new_end='_targetp_out.txt')
		with open(outf_path, 'w') as outf:
			outf.writelines(out_data)
			outf.closed

	csv_out = []
	for s in out_data:
		lines = filter(is_targetp_info, s.split('\n'))
		for line in lines:
			line = line.split()
			if line: csv_out.append(line)

		if not outf_path: outf_path = new_file_same_dir(f_path, new_end='_targetp_out.csv')
		with open(outf_path, 'w') as outf:
		    csv_writer = csv.writer(outf)
		    csv_writer.writerows(csv_out)

	return outf_path

f_path = '/home/anna/bioinformatics/euglenozoa/euglena/sequences/E_gracilis_transcriptome_final.PROTEINS.fasta'

use_targetp(f_path)