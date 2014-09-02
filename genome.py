import os
from subprocess import call
import ntpath

def file_from_path (path):

    head, tail = ntpath.split(path)
    dir_path = [head, tail]
    return tail

def trim_by_trimmomatic (trimc_dir, file_fw, file_rv, output_dir):

	name_reads = file_from_path(file_fw)[0:-6]

	trimc_output = output_dir + 'TrimcOutput/'

	if not os.path.exists(trimc_output):
	    os.makedirs(trimc_output)

	trimlog = trimc_output +'trimlog'
	paired_output_fw = trimc_output + name_reads + 'paired_output_fw' + '.fastq'
	unpaired_output_fw = trimc_output + name_reads + 'unpaired_output_fw' + '.fastq'
	paired_output_rv = trimc_output + name_reads + 'paired_output_rv' + '.fastq'
	unpaired_output_rv = trimc_output + name_reads + 'unpaired_output_rv' + '.fastq'

	adapters_file = trimc_dir + 'adapters/'+ "TruSeq3-PE-2.fa"

	trimmomatic = ['java', '-jar', trimc_dir + 'trimmomatic-0.32.jar']
	trim_options = ['PE', '-phred33', '-trimlog', trimlog, file_fw, file_rv, 
					paired_output_fw, unpaired_output_fw, paired_output_rv, unpaired_output_rv,
					'ILLUMINACLIP:'+ adapters_file + ':2:30:10', 'LEADING:20', 'TRAILING:20', 'SLIDINGWINDOW:4:20',  
					'MAXINFO:40:0.8', 'MINLEN:20' ] 
	trim = trimmomatic + trim_options
	# print ' '.join(trim_options)
	call(trim)
	return trimc_output

def assemble_by_spades1 (spades_dir, file_fw, file_rv, output_dir, memory):

	spades_output = output_dir + 'SpadesOutput/'
	spades = spades_dir + './spades.py'
	spades_options = ['-o', spades_output, '-m '+ str(memory), '--careful']
	assemble_by_spades = [spades, '-1', file_fw, '-2', file_rv] + spades_options
	# assemble_by_spades = [spades, '--test'] # Test SPAdes

	if not os.path.exists(spades_output):
	    os.makedirs(spades_output)

	call(assemble_by_spades)
	return spades_output

def assemble_by_spades (spades_dir, trimc_output, output_dir, name_reads, memory):

	spades_output = output_dir + 'SpadesOutput/'
	spades = spades_dir + './spades.py'
	files = {'PEfw' : 'paired_output_fw.fastq', 'PErv' : 'paired_output_rv.fastq', 
			 'UPfw': 'unpaired_output_fw.fastq', 'UPrv': 'unpaired_output_rv.fastq'}

	for key in files:
		files[key] = trimc_output + name_reads + files[key]

	spades_options = ['-1', files['PEfw'], '-2', files['PErv'], '-s', files['UPfw'], '-s', files['UPrv'], 
					  '-o', spades_output, '-m '+ str(memory), '--careful']
	# print spades_options

	assemble_by_spades = [spades] + spades_options

	if not os.path.exists(spades_output):
	    os.makedirs(spades_output)

	call(assemble_by_spades)
	return spades_output

def use_quast (contigs, reference, output_dir):

	quast_output = output_dir + 'QuastOutput/'
	quast = quast_dir + './quast'
	quast_options = []
	use_quast = quast + quast_options
	return quast_output

def scaffold_by_abacas (abacas_dir, contigs, reference, output_dir, name_reads):

	abacas_output = output_dir + 'AbacasOutput/'
	abacas = ['perl', abacas_dir + 'abacas.pl']
	abacas_options = ['-r', reference, '-q', contigs, '-b', '-c', '-m', '-p', nucmer]
	scaffold_by_abacas = abacas + abacas_options
	return abacas_output

def annotate_by_prokka (prokka_dir, sequence, output_dir, name_reads):

	prokka_output = output_dir + 'ProkkaOutput/'
	prokka = prokka_dir + './prokka'
	prokka_options = ['--centre', 'XXX', '--kingdom', 'Bacteria', '--genus', 'Escherichia', '--species', 'coli', '--outdir', prokka_output, '--force', sequence]
	annotate_by_prokka = [prokka] + prokka_options
	call(annotate_by_prokka)
	return prokka_output


work_dir = '/home/anna/HTS-all/HTS-programming/'
trimc_dir = '/home/anna/Trimmomatic-0.32/'
spades_dir = '/home/anna/SPAdes-3.1.0-Linux/bin/'
abacas_dir = '/home/anna/Abacas/abacas.pl'
prokka_dir = '/home/anna/prokka-1.10/bin/' 
quast_dir = '/home/anna/quast-2.3/quast.py'

file_fw = '/home/anna/BISS2014/EcoliProject/Stuff/1.fastq'
file_rv = '/home/anna/BISS2014/EcoliProject/Stuff/2.fastq'
# file_fw = '/home/anna/HTS-all/HTSes/Katya/0sec_ACAGTG_L001_R1_001.fastq'
# file_rv = '/home/anna/HTS-all/HTSes/Katya/0sec_ACAGTG_L001_R2_001.fastq'
# file_fw = '/home/anna/HTS-all/HTS-programming/1000_CTG_CCGTCC_L001_1.fastq'
# file_rv = '/home/anna/HTS-all/HTS-programming/1000_CTG_CCGTCC_L001_2.fastq'
#file_fw = '/home/anna/HTS-all/HTS-programming/1000_Kan-frag_ATGTCA_L001_1.fastq'
#file_rv = '/home/anna/HTS-all/HTS-programming/1000_Kan-frag_ATGTCA_L001_2.fastq'


name_fw = file_from_path(file_fw)
name_rv = file_from_path(file_rv)
name_reads = name_fw[0:-6]
output_dir = work_dir + name_reads + '/'

#trimc_output = trim_by_trimmomatic(trimc_dir, file_fw, file_rv, output_dir)
trimc_output = output_dir + 'TrimcOutput/'

memory = 5 #Gb free memory for SPAdes
#spades_output = assemble_by_spades(spades_dir, trimc_output, output_dir, name_reads, memory)
spades_output = output_dir + 'SpadesOutput/'

contigs = spades_output + 'contigs.fasta'
use_quast (contigs, reference, output_dir)
#scaffold_by_abacas (abacas_dir, contigs, reference, output_dir, name_reads)
#annotate_by_prokka (prokka_dir, contigs, output_dir, name_reads)


# input_dir = '/home/anna/HTS-all/HTSes/'
# HTSes = [('CTG_CCGTCC_L001_1.fastq', 'CTG_CCGTCC_L001_2.fastq'), ('Kan-frag_ATGTCA_L001_1.fastq', 'Kan-frag_ATGTCA_L001_2.fastq'),  
# ('T4ai_AGTTCC_L001_1.fastq', 'T4ai_AGTTCC_L001_2.fastq'), ('T4bi_1.fastq', 'T4bi_2.fastq'), ('T4C1T_TAGCTT_L001_1.fastq', 'T4C1T_TAGCTT_L001_2.fastq')]
# for fw, rv in HTSes:
# 	file_fw = input_dir + fw
# 	file_rv = input_dir + rv
# 	name_fw = file_from_path(file_fw)
# 	name_rv = file_from_path(file_rv)
# 	name_reads = name_fw[0:-6]
# 	output_dir = work_dir + name_reads + '/'
# 	print output_dir
# 	trimmomate (trimc_dir, file_fw, file_rv, output_dir)
# assemble_by_spades1 (spades_dir, file_fw, file_rv, output_dir, memory)


# java -jar /home/anna/BRIG-0.95-dist/BRIG.jar #open BRIG
