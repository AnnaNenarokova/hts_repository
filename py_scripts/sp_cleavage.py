#!/usr/bin/python3
inFile = open('/home/kika/MEGAsync/Euglena longa/2013 Sekvenovanie/Galactoglycerolipids/TAG synthesis/TAG_synthesis_input.txt', 'r')
#input file in table contig_name, TMD_number, SP_cleavage, prot_seq

for protein in inFile:
#   splitting rows based on particular cells in the table
    splitted_line = protein.split('\t')
    contig = splitted_line[0]
##    TMD = int(splitted_line[1])
    SP = splitted_line[2]
    seq = splitted_line[3]
# cleveage of SP in proteins containig SP, based on its length
    try:
        SP = int(SP)
        SP_cleaved = '>{}\n{}'.format(contig,seq[SP:])
##        print(SP_cleaved)
        with open('/home/kika/MEGAsync/Euglena longa/2013 Sekvenovanie/Galactoglycerolipids/TAG synthesis/EL_TAG_hits_SP_cleaved.txt', 'a') as result:
            result.write(SP_cleaved)
# contig with protein, which doesn't contain SP, written in error file
    except ValueError as VE:
        with open('/home/kika/MEGAsync/Euglena longa/2013 Sekvenovanie/Galactoglycerolipids/TAG synthesis/EL_TAG_hits_ValueErrors.txt', 'a') as ValueErrors:
            ValueErrors.write('{}\t{}\n'.format(contig,str(VE)))
