#!/bin/bash

demux="/home/qiime1/bin/bbmap/demuxbyname.sh"

$demux in=r#.fq out=out_%_#.fq prefixmode=f names=GGACTCCT+GCGATCTA,TAAGGCGA+TCTACTCT,...
