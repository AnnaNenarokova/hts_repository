#!/usr/bin/python
import os
from subprocess32 import call
from ntpath import split
global ONLY_TRIM; ONLY_TRIM = False
global ONLY_ASSEMBLE; ONLY_ASSEMBLE = True
global ONLY_ANNOTATE; ONLY_ANNOTATE = False
global THREADS; THREADS = 8

def file_from_path (path):
    head, tail = split(path)
    return tail

def trimc_trim (file_fw, file_rv, outdir, trimc_dir=False):
	if not trimc_dir: trimc_dir = '/home/anna/bioinformatics/bioprograms/Trimmomatic-0.32/'
	trim_out = outdir + 'trim_out/'
	if not os.path.exists(trim_out):
	    os.makedirs(trim_out)

	trimlog = trim_out +'trimlog'
	paired_out_fw = trim_out + 'paired_out_fw' + '.fastq'
	unpaired_out_fw = trim_out + 'unpaired_out_fw' + '.fastq'
	paired_out_rv = trim_out + 'paired_out_rv' + '.fastq'
	unpaired_out_rv = trim_out + 'unpaired_out_rv' + '.fastq'

	adapters_file = trimc_dir + 'adapters/'+ "TruSeq3-PE-2.fa"

	trimmomatic = ['java', '-jar', trimc_dir + 'trimmomatic-0.32.jar']
	trim_options = ['PE', '-threads', str(THREADS), '-phred33', '-trimlog', trimlog, file_fw, file_rv, 
					paired_out_fw, unpaired_out_fw, paired_out_rv, unpaired_out_rv,
					'ILLUMINACLIP:'+ adapters_file + ':2:30:10', 'LEADING:20', 'TRAILING:20', 'SLIDINGWINDOW:4:20',  
					'MAXINFO:40:0.8', 'MINLEN:20' ] 
	trim = trimmomatic + trim_options
	print ' '.join(trim)
	call(trim)
	return trim_out

def bbduk_trim (file_fw, file_rv, outdir, RAM=6, bbduk_dir=False):
	if not bbduk_dir: bbduk_dir = '/home/anna/bioinformatics/bioprograms/bbmap/'
	bbduk_out = outdir + 'bbduk_out/'
	print bbduk_out
	if not os.path.exists(bbduk_out): os.makedirs(bbduk_out)
	adapters = bbduk_dir + 'resources/TruSeq3-PE-2.fa'
	bbduk = [bbduk_dir + './bbduk.sh']
	file_out_fw = bbduk_out + 'fw.fastq'
	file_out_rv = bbduk_out + 'rv.fastq'
	bbduk_options = ['-Xmx'+str(RAM)+'g', 'in1='+file_fw, 'in2='+file_rv, 'out1='+file_out_fw, 'out2='+file_out_rv, 'minlen=25', 'qtrim=rl', 'trimq=10', 'ktrim=r', 'k=25', 'mink=11', 'ref='+adapters, 'hdist=3']
	call(bbduk + bbduk_options)
	return bbduk_out

def spades_assemble(outdir, test=False, spades_dir=False, file_fw=False, file_rv=False, bbduk_out = False, trim_out=False, RAM=7):
	if not spades_dir: spades_dir = '/home/anna/bioinformatics/bioprograms/SPAdes-3.1.1-Linux/bin/'

	spades_out = outdir + 'spades_out/'
	spades = spades_dir + './spades.py'

	if test: spades_assemble= [spades, '--test'] # Test SPAdes

	else:

		if trim_out:
			files = {'PEfw' : 'paired_out_fw.fastq', 'PErv' : 'paired_out_rv.fastq', 
					 'UPfw': 'unpaired_out_fw.fastq', 'UPrv': 'unpaired_out_rv.fastq'}
			for key in files:
				files[key] = trim_out + files[key]
				spades_options = ['-1', files['PEfw'], '-2', files['PErv'], '-s', files['UPfw'], '-s', files['UPrv'], 
								  '-o', spades_out, '-m '+ str(RAM), '--careful']
				spades_assemble= [spades] + spades_options

		elif file_fw and file_rv:
			spades_options = ['-o', spades_out, '-m '+ str(RAM), '--only-assembler']
			spades_assemble = [spades, '-1', file_fw, '-2', file_rv] + spades_options

		else: print "Error: spades_assemble haven't get needed values"

		if not os.path.exists(spades_out): os.makedirs(spades_out)
		call(spades_assemble)
		
	print(' '.join(spades_assemble))
	return spades_out

def velvet_assemble(outdir, test=False, velvet_dir=False, file_fw=False, file_rv=False, bbduk_out = False, trim_out=False, RAM=7):
	if not velvet_dir: velvet_dir = '/home/anna/bioinformatics/bioprograms/velvet_1.2.10/'

	velvet_out = outdir + 'velvet_out/'	
	if not os.path.exists(velvet_out): os.makedirs(velvet_out)
	velvet = [velvet_dir + './VelvetOptimiser.pl']
	velvet_options = ['-g', '4.6', '-t', str(THREADS), '-d', velvet_out]
	velvet_assemble = velvet + ['-f', '\'' + '-shortPaired -fastq ' + file_fw + ' -shortPaired2 -fastq ' + file_rv + '\'']

	print ' '.join(velvet_assemble)
	call(velvet_assemble)
	return velvet_out

def use_quast (contigs, reference, outdir, quast_dir=False):
	if not quast_dir: quast_dir = '/home/anna/bioinformatics/bioprograms/quast-2.3/quast.py'
	quast_out = outdir + 'quast_out/'
	quast = quast_dir + './quast'
	quast_options = []
	use_quast = quast + quast_options
	return quast_out

def abacas_scaffold (contigs, reference, outdir, abacas_dir=False):
	if not abacas_dir: abacas_dir = '/home/anna/bioinformatics/bioprograms/Abacas/abacas.pl'
	abacas_out = outdir + 'abacas_out/'
	abacas = ['perl', abacas_dir + 'abacas.pl']
	abacas_options = ['-r', reference, '-q', contigs, '-b', '-c', '-m', '-p', nucmer]
	scaffold_abacas = abacas + abacas_options
	return abacas_out

def prokka_annotate (sequence, outdir, prokka_dir=False):
	if not prokka_dir: prokka_dir = '/home/anna/bioinformatics/bioprograms/prokka-1.10/bin/'
	prokka_out = outdir + 'prokka_out/'
	prokka = prokka_dir + './prokka'
	prokka_options = ['--centre', 'XXX', '--kingdom', 'Bacteria', '--genus', 'Escherichia', '--species', 
					  'coli', '--gram', 'neg', '--rfam', '--addgenes',  '--outdir', prokka_out, '--force', sequence]
	prokka_annotate = [prokka] + prokka_options
	call(prokka_annotate)
	return prokka_out

def handle_hts (file_fw, file_rv, outdir):
	if not ONLY_ASSEMBLE: 
		trim_out = bbduk_trim(file_fw, file_rv, outdir)
		if not ONLY_TRIM:
			spades_out = spades_assemble(outdir, trim_out)
			contigs = spades_out + 'contigs.fasta'
			prokka_annotate (contigs, outdir)
			# use_quast (contigs, reference, outdir)
			# scaffold_abacas (abacas_dir, contigs, reference, outdir)
	else: 
		# trim_out = outdir + 'bbduk_out/'
		velvet_out = velvet_assemble(outdir, file_fw=file_fw, file_rv=file_rv)
		
	return 0

def handle_files (workdir, file_fw=False, file_rv=False, hts_dir=False, htses=False):
	if file_fw and file_rv:
		name_fw = file_from_path(file_fw)
		name_rv = file_from_path(file_rv)
		name_reads = name_fw[0:-6]
		outdir = workdir + name_reads + '/'
		if not os.path.exists(outdir): os.makedirs(outdir)
		handle_hts (file_fw, file_rv, outdir)

	elif hts_dir and htses:
		for fw, rv in htses:
			file_fw = hts_dir + fw
			file_rv = hts_dir + rv
			name_fw = file_from_path(file_fw)
			name_rv = file_from_path(file_rv)
			name_reads = name_fw[0:-6]
			outdir = workdir + name_reads + '/'
			if not os.path.exists(outdir): os.makedirs(outdir)
			handle_hts (file_fw, file_rv, outdir)

	else: print "Error: handle_htses haven't get needed values"

	return 0

workdir = '/home/anna/bioinformatics/hts/outdirs/'
file_fw = '/home/anna/bioinformatics/hts/htses/dasha/Ecoli-B_trimmed_paired_R1.fastq'
file_rv = '/home/anna/bioinformatics/hts/htses/dasha/Ecoli-B_trimmed_paired_R2.fastq'
handle_files(workdir, file_fw, file_rv)

# htses =[('CTG_CCGTCC_L001_1.fastq', 'CTG_CCGTCC_L001_2.fastq'), ('Kan-frag_ATGTCA_L001_1.fastq', 'Kan-frag_ATGTCA_L001_2.fastq'),  
# ('T4ai_AGTTCC_L001_1.fastq', 'T4ai_AGTTCC_L001_2.fastq'), ('T4bi_1.fastq', 'T4bi_2.fastq'), ('T4C1T_TAGCTT_L001_1.fastq', 'T4C1T_TAGCTT_L001_2.fastq')]

# hts_dir = '/home/anna/bioinformatics/hts/htses/'

# handle_files(workdir, hts_dir = hts_dir, htses = htses)

# reference = '/home/anna/bioinformatics/hts/stuff/pt7blue-T4.fasta'
reference = '/home/anna/bioinformatics/output_from_server/contigs.fasta'

outdir = '/home/anna/bioinformatics/hts/outdirs/'
prokka_annotate (reference, outdir)
