#!/bin/sh

of='/home/kika/tools/OrthoFinder-2.1.2/orthofinder'
proteins='/home/kika/tools/OrthoFinder-2.1.2/ExampleData/'
blast_method=diamond

$of -f $proteins -S $blast_method -t 16