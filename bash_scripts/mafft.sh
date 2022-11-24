#!/bin/bash

input_path=""
output_path=""

mafft-linsi $input_path > $output_path # we use mafft-linsi to do a slow, accurate alignment

# mafft --auto $input_path > $output_path # we use mafft --auto to do a quick, dirty alignment