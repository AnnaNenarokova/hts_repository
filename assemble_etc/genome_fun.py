from subprocess32 import call
global THREADS; THREADS = 8
global RAM; RAM = 8

def use_quast (contigs, outdir, reference = False, quast_dir=False):
	if not quast_dir: quast_dir = '/home/anna/bioinformatics/bioprograms/quast-2.3/'
	quast_out = outdir + 'quast_out/'
	quast = quast_dir + './quast.py'
	quast_options = ['-o', quast_out]
	if reference: quast_options = quast_options + ['-R', reference]
	use_quast = [quast] + quast_options + [contigs]
	call(use_quast)
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
					  'coli', '--gram', 'neg', '--addgenes',  '--outdir', prokka_out, '--force', sequence]
	prokka_annotate = [prokka] + prokka_options
	call(prokka_annotate)
	return prokka_out
