import os
from subprocess32 import call
from ntpath import split

def file_from_path (path):
    head, tail = split(path)
    return tail

def trimc_trim (file_fw, file_rv, outdir, threads=4, trimc_dir=False):
	if not trimc_dir: trimc_dir = '/home/anna/bioinformatics/bioprograms/Trimmomatic-0.32/'
	trimc_out = outdir + 'trimc_out/'
	if not os.path.exists(trimc_out):
	    os.makedirs(trimc_out)

	trimlog = trimc_out +'trimlog'
	paired_out_fw = trimc_out + 'paired_out_fw' + '.fastq'
	unpaired_out_fw = trimc_out + 'unpaired_out_fw' + '.fastq'
	paired_out_rv = trimc_out + 'paired_out_rv' + '.fastq'
	unpaired_out_rv = trimc_out + 'unpaired_out_rv' + '.fastq'

	adapters_file = trimc_dir + 'adapters/'+ "TruSeq3-PE-2.fa"

	trimmomatic = ['java', '-jar', trimc_dir + 'trimmomatic-0.32.jar']
	trim_options = ['PE', '-threads', str(threads), '-phred33', '-trimlog', trimlog, file_fw, file_rv, 
					paired_out_fw, unpaired_out_fw, paired_out_rv, unpaired_out_rv,
					'ILLUMINACLIP:'+ adapters_file + ':2:30:10', 'LEADING:20', 'TRAILING:20', 'SLIDINGWINDOW:4:20',  
					'MAXINFO:40:0.8', 'MINLEN:20' ] 
	trim = trimmomatic + trim_options
	print ' '.join(trim)
	call(trim)
	return trimc_out

def bbduk_trim (file_fw, file_rv, outdir, RAM=6, threads=4, bbduk_dir=False):
	if not bbduk_dir: bbduk_dir = '/home/anna/bioinformatics/bioprograms/bbmap/'
	bbduk_out = outdir + 'bbduk_out/'
	print bbduk_out
	if not os.path.exists(bbduk_out): os.makedirs(bbduk_out)
	adapters = bbduk_dir + 'resources/'+ "truseq.fa"

	bbduk = [bbduk_dir + './bbduk.sh']
	for file_in in (file_fw, file_rv):
		name_reads = file_from_path(file_in)[0:-6]
		file_out = bbduk_out + name_reads + '.fastq'
		adapter_options = ['-Xmx' + str(RAM) +'g', 'in=' + file_in, 'out=' + file_out, 'ref=' + adapters, 'ktrim=r', 'k=28', 'mink=12', 'hdist=1']
		quality_options = ['-Xmx' + str(RAM) +'g', 'in='+ file_in, 'out='+ file_out, 'qtrim=rl', 'trimq=10'] 
		call(bbduk + adapter_options)
		call(bbduk + quality_options)
	return bbduk_out

def spades_assemble(outdir, test=False, spades_dir=False, file_fw=False, file_rv=False, trim_out=False, RAM=6):
	if not spades_dir: spades_dir = '/home/anna/bioinformatics/bioprograms/SPAdes-3.1.1-Linux/bin/'

	spades_out = outdir + 'spades_out/'
	spades = spades_dir + './spades.py'

	if test: spades_assemble= [spades, '--test'] # Test SPAdes

	else:

		if trim_out:
			files = {'PEfw' : 'paired_out_fw.fastq', 'PErv' : 'paired_out_rv.fastq', 
					 'UPfw': 'unpaired_out_fw.fastq', 'UPrv': 'unpaired_out_rv.fastq'}
			for key in files:
				files[key] = trimc_out + files[key]
				spades_options = ['-1', files['PEfw'], '-2', files['PErv'], '-s', files['UPfw'], '-s', files['UPrv'], 
								  '-o', spades_out, '-m '+ str(RAM), '--careful']
				spades_assemble= [spades] + spades_options

		elif file_fw and file_rv:
			spades_options = ['-o', spades_out, '-m '+ str(RAM), '--careful']
			spades_assemble = [spades, '-1', file_fw, '-2', file_rv] + spades_options

		else: print "Error: spades_assemble haven't get needed values"

		if not os.path.exists(spades_out): os.makedirs(spades_out)
		call(spades_assemble)

	return spades_out

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
					  'coli', '--outdir', prokka_out, '--force', sequence]
	prokka_annotate = [prokka] + prokka_options
	call(prokka_annotate)
	return prokka_out

def handle_HTS (file_fw, file_rv, outdir, only_trim=False, only_assemble=False,  only_annotate=False, threads=8):
	if not only_assemble: 
		trimc_out = bbduk_trim(file_fw, file_rv, outdir, threads)
	else: 
		trimc_out = outdir + 'bbduk_out/'

	if not only_trim:
		spades_out = spades_assemble(outdir, trimc_out)
		contigs = spades_out + 'contigs.fasta'
		prokka_annotate (contigs, outdir)
		# use_quast (contigs, reference, outdir)
		# scaffold_abacas (abacas_dir, contigs, reference, outdir)
		
	return 0

def handle_files (workdir, file_fw=False, file_rv=False, HTS_dir=False, HTSes=False, only_trim=False, 
				  only_assemble=False, only_annotate=False):
	if file_fw and file_rv:
		name_fw = file_from_path(file_fw)
		name_rv = file_from_path(file_rv)
		name_reads = name_fw[0:-6]
		outdir = workdir + name_reads + '/'
		if not os.path.exists(outdir): os.makedirs(outdir)
		if not only_trim: 
			handle_HTS (file_fw, file_rv, outdir)
		else: 
			handle_HTS (file_fw, file_rv, outdir, only_trim=True)

	elif HTS_dir and HTSes:
		for fw, rv in HTSes:
			file_fw = HTS_dir + fw
			file_rv = HTS_dir + rv
			name_fw = file_from_path(file_fw)
			name_rv = file_from_path(file_rv)
			name_reads = name_fw[0:-6]
			outdir = workdir + name_reads + '/'
			if not os.path.exists(outdir): os.makedirs(outdir)
			if not only_trim: 
				handle_HTS (file_fw, file_rv, outdir)
			else: 
				handle_HTS (file_fw, file_rv, outdir, only_trim = True)

	else: print "Error: handle_HTSes haven't get needed values"

	return 0

workdir = '/home/anna/bioinformatics/HTS-all/HTS-programming/'

# file_fw = '/home/anna/bioinformatics/BISS2014/EcoliProject/Stuff/1.fastq'
# file_rv = '/home/anna/bioinformatics/BISS2014/EcoliProject/Stuff/2.fastq'
file_fw = '/home/anna/bioinformatics/HTS-all/HTSes/Katya/0sec_ACAGTG_L001_R1_001.fastq'
file_rv = '/home/anna/bioinformatics/HTS-all/HTSes/Katya/0sec_ACAGTG_L001_R2_001.fastq'
# file_fw = '/home/anna/bioinformatics/HTS-all/HTSes/CTG_CCGTCC_L001_1.fastq'
# file_rv = '/home/anna/bioinformatics/HTS-all/HTSes/CTG_CCGTCC_L001_2.fastq'
# file_fw = '/home/anna/bioinformatics/HTS-all/HTSes/ERR015599_1.fastq'
# file_rv = '/home/anna/bioinformatics/HTS-all/HTSes/ERR015599_1.fastq'

# handle_files(workdir, file_fw, file_rv, only_trim = True)

HTSes =[('CTG_CCGTCC_L001_1.fastq', 'CTG_CCGTCC_L001_2.fastq'), ('Kan-frag_ATGTCA_L001_1.fastq', 'Kan-frag_ATGTCA_L001_2.fastq'),  
('T4ai_AGTTCC_L001_1.fastq', 'T4ai_AGTTCC_L001_2.fastq'), ('T4bi_1.fastq', 'T4bi_2.fastq'), ('T4C1T_TAGCTT_L001_1.fastq', 'T4C1T_TAGCTT_L001_2.fastq')]

HTS_dir = '/home/anna/bioinformatics/HTS-all/HTSes/'

handle_files(workdir, HTS_dir = HTS_dir, HTSes = HTSes)