#!/bin/bash
fasta="/home/shared/BANK/diplonema_dataset/euglenozoa_anzhelika/all_euglenozoans.faa"
db_path="/home/shared/BANK/diplonema_dataset/euglenozoa_anzhelika/all_euglenozoans.dmnd"
threads="30"
diamond makedb --in $fasta --db $db_path --threads $threads
