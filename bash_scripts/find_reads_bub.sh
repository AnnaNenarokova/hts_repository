#!/bin/bash
sudo find / \( -name '*.fastq*' -o -name '*.fq*' \) -type f -size +1G >> /home/nenarokova/all_reads_bub.txt