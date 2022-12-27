#!/bin/bash
 
indir="/Users/vl18625/work/euk/markers_euks/nina_markers/ae/68_final_ae_markers/linsi_bmge/"
outdir="/Users/vl18625/work/euk/markers_euks/nina_markers/ae/asgard_only/linsi_bmge/"

# Declare an array of string with type
declare -a arcogs=("arCOG00779" "arCOG00865" "arCOG00868" "arCOG01228" "arCOG01560" "arCOG01885" "arCOG01887" "arCOG01950" "arCOG04049" "arCOG04070" "arCOG04072" "arCOG04086" "arCOG04087" "arCOG04094" "arCOG04096" "arCOG04097" "arCOG04108" "arCOG04109" "arCOG04113" "arCOG04129" "arCOG04169" "arCOG04182" "arCOG04185" "arCOG04186" "arCOG04209" "arCOG04223" "arCOG04239" "arCOG04240" "arCOG04241" "arCOG04242" "arCOG04243" "arCOG04288" "arCOG04304" "arCOG04314")
 
# Iterate the string array using for loop
for arcog in ${arcogs[@]}; do
   echo $arcog
   cp $indir$arcog".faa" $outdir$arcog".faa"
done