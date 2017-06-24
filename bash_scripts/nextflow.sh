#!/bin/bash
JAVA_HOME="java"
JDK_HOME="java"
JRE_HOME="java"
cd /home/nenarokova/tools
nextflow_config="/home/nenarokova/companion_local/nextflow.config"
sudo ./nextflow run sanger-pathogens/companion -c $nextflow_config -profile docker
