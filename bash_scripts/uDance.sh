#!/bin/bash
config_path=""
snakemake -c 8 --configfile $config_path --snakefile udance.smk all