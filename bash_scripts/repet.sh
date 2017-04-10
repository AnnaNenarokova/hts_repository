#!/bin/bash
jexport REPET_PATH="/home/nenarokova/tools/REPET_linux-x64-2.5"
export PATH=$REPET_PATH/denovo_pipe/:$PATH
export PATH=$REPET_PATH/bin/:$PATH
repet_dir="/media/4TB1/blasto/p57_repet/"
TEdenovo.py -P P57 -C /media/4TB1/blasto/p57_repet/TEdenovo.cfg -S 2 -s Blaster
