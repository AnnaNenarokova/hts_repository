from subprocess32 import call
global THREADS; THREADS = 8
global RAM; RAM = 8

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

def bbduk_trim (file_fw, file_rv, outdir, bbduk_dir=False):
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