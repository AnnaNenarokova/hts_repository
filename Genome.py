import os
from subprocess import call
spades_dir = '/home/anna/SPAdes-3.1.0-Linux/bin/'
work_dir = '/home/anna/BISS2014/EcoliProject/Stuff/'
name_fw = '1.fastq'
name_rv = '2.fastq'
file_fw = work_dir + name_fw
file_rv = work_dir + name_rv
spades = spades_dir + './spades.py'
print spades
spades_output = work_dir + 'SpadesOutput'
options_spades = ['-o', spades_output, '-m 5', '--only-assembler']
assemble_by_flash = [spades, '-1', file_fw, '-2', file_rv] + options_spades
print assemble_by_flash

if not os.path.exists(spades_output):
    os.makedirs(spades_output)

call(assemble_by_flash)