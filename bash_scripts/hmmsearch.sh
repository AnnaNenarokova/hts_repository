#!/bin/bash

hmm="/home/nenarokova/genomes/euglena/tom40/canonical_alveolata.hmm"
subject="/home/nenarokova/genomes/euglena/sequences/E_gracilis_transcriptome_final.PROTEINS.fasta"
subject="/home/tomas/genomes/Proteoms/Ndesignis_MMETSP1114_pep.fasta"

pfam_hits="/home/nenarokova/genomes/euglena/tom40/canonical_alveolata_hits_hmmsearch.txt"

/home/nenarokova/tools/hmmer-3.1b2-linux-intel-x86_64/binaries/hmmsearch --pfamtblout $pfam_hits $hmm $subject
