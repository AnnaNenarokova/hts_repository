import os
from subprocess import call
import ntpath

def file_from_path(path):

    head, tail = ntpath.split(path)
    dir_path = [head, tail]
    return tail

def trimmomate (trimc_dir, file_fw, file_rv, output_dir):

	# java -jar <path to trimmomatic.jar> PE [-threads <threads] [-phred33 | -phred64] [-trimlog <logFile>] 
	# <input 1> <input 2> <paired output 1> <unpaired output 1> <paired output 2> <unpaired output 2> <step 1> ...

	# java -jar trimmomatic-0.30.jar PE --phred33 input_forward.fq.gz input_reverse.fq.gz output_forward_paired.fq.gz 
	# output_forward_unpaired.fq.gz output_reverse_paired.fq.gz output_reverse_unpaired.fq.gz ILLUMINACLIP:TruSeq3-PE.
	# fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36

	name_reads = file_from_path(file_fw)[0:-6]

	trimc_output = output_dir + 'TrimcOutput/'
	# print trimc_output
	if not os.path.exists(trimc_output):
	    os.makedirs(trimc_output)

	trimlog = trimc_output +'trimlog'
	paired_output_fw = trimc_output + name_reads + 'paired_output_fw' + '.fastq'
	unpaired_output_fw = trimc_output + name_reads + 'unpaired_output_fw' + '.fastq'
	paired_output_rv = trimc_output + name_reads + 'paired_output_rv' + '.fastq'
	unpaired_output_rv = trimc_output + name_reads + 'unpaired_output_rv' + '.fastq'

	adapters_file = trimc_dir + '/adapters/'+ "TruSeq3-PE-2.fa"

	trimmomatic = ['java', '-jar', trimc_dir + 'trimmomatic-0.32.jar']
	trim_options = ['PE', '-phred33', '-trimlog', trimlog, file_fw, 
	file_rv, paired_output_fw, unpaired_output_fw, paired_output_rv, unpaired_output_rv,
	'ILLUMINACLIP:'+ adapters_file + ':2:30:10', 'LEADING:20', 'TRAILING:20', 'SLIDINGWINDOW:4:20',  'MAXINFO:40:0.8', 'MINLEN:20' ] 
	# trim_extra_options = [input_fw, input_rv, ]
	trim = trimmomatic + trim_options
	# print trim
	# print ' '.join(trim_options)
	call(trim)
	return 0

def assemble_by_spades1 (spades_dir, file_fw, file_rv, output_dir, memory):

	spades = spades_dir + './spades.py'
	print spades
	spades_output = output_dir + 'SpadesOutput'
	options_spades = ['-o', spades_output, '-m '+ str(memory), '--careful']
	assemble_by_spades = [spades, '-1', file_fw, '-2', file_rv] + options_spades
	# assemble_by_spades = [spades, '--test'] # Test SPAdes
	print assemble_by_spades
	print ', '.join(assemble_by_spades)
	if not os.path.exists(spades_output):
	    os.makedirs(spades_output)

	call(assemble_by_spades)
	return 0

def assemble_by_spades (spades_dir, output_dir, name_reads, memory):

	spades = spades_dir + './spades.py'
	trimc_output = output_dir + 'TrimcOutput/'
	spades_output = output_dir + 'SpadesOutput'
	files = {'PEfw' : 'paired_output_fw.fastq', 'PErv' : 'paired_output_rv.fastq', 
	'UPfw': 'unpaired_output_fw.fastq', 'UPrv': 'unpaired_output_rv.fastq'}

	for key in files:
		files[key] = trimc_output + name_reads + files[key]
	# print files

	options_spades = ['-1', files['PEfw'], '-2', files['PErv'], '-s', files['UPfw'], '-s', files['UPrv'], 
	'-o', spades_output, '-m '+ str(memory), '--careful']
	# print options_spades

	assemble_by_spades = [spades] + options_spades
	# print assemble_by_spades
	# print ', '.join(assemble_by_spades)
	if not os.path.exists(spades_output):
	    os.makedirs(spades_output)

	call(assemble_by_spades)
	return 0

def use_quast (contigs, reference, output_dir):
	return 0

work_dir = '/home/anna/HTS-all/HTS-programming/'
trimc_dir = '/home/anna/Trimmomatic-0.32/'
spades_dir = '/home/anna/SPAdes-3.1.0-Linux/bin/'

# file_fw = '/home/anna/HTS-all/HTS-programming/0sec_ACAGTG_L001_R1_001.fastq'
# file_rv = '/home/anna/HTS-all/HTS-programming/0sec_ACAGTG_L001_R2_001.fastq'
# file_fw = '/home/anna/BISS2014/EcoliProject/Stuff/1.fastq'
# file_rv = '/home/anna/BISS2014/EcoliProject/Stuff/2.fastq'
# file_fw = '/home/anna/HTS-all/HTSes/Katya/0sec_ACAGTG_L001_R1_001.fastq'
# file_rv = '/home/anna/HTS-all/HTSes/Katya/0sec_ACAGTG_L001_R2_001.fastq'
# file_fw = '/home/anna/HTS-all/HTS-programming/1000_CTG_CCGTCC_L001_1.fastq'
# file_rv = '/home/anna/HTS-all/HTS-programming/1000_CTG_CCGTCC_L001_2.fastq'
file_fw = '/home/anna/HTS-all/HTS-programming/1000_Kan-frag_ATGTCA_L001_1.fastq'
file_rv = '/home/anna/HTS-all/HTS-programming/1000_Kan-frag_ATGTCA_L001_2.fastq'
# file_fw = '/home/anna/HTS-all/HTS-programming/10_CTG_CCGTCC_L001_1.fastq'
# file_rv = '/home/anna/HTS-all/HTS-programming/10_CTG_CCGTCC_L001_2.fastq'

name_fw = file_from_path(file_fw)
name_rv = file_from_path(file_rv)
name_reads = name_fw[0:-6]
output_dir = work_dir + name_reads + '/'
trimmomate (trimc_dir, file_fw, file_rv, output_dir)

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

memory = 5 #Gb free memory for SPAdes
assemble_by_spades(spades_dir, output_dir, name_reads, memory)
# assemble_by_spades1 (spades_dir, file_fw, file_rv, output_dir, memory)