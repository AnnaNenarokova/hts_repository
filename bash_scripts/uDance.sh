#!/bin/bash
config_path=""
snakemake --jobs 14 --configfile $config_path --snakefile udance.smk all