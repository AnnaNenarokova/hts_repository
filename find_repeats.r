rm(list = ls()) 
gc() #cleans RAM 
library(ShortRead)
repeat_fw = 'GAGTTCCCCGCGCCAGCGGGGATAAACCGC'
repeat_rv = 'GCGGTTTATCCCCGCTGGCGCGGGGAACTC'
reads_file = '/home/anna/HTS-all/HTS-programming/CTG_CCGTCC_L001_1/FlashOutput/CTG_CCGTCC_L001_1.extendedFrags.fasta'
min = 1
max = 1000
reads = sread(readFasta(reads_file))
print (reads)
#seq = 'CGGCATCACCTTTGGCTTCGGCTGCGGTTTCTCCCCGCTGGCGCGGGGAACTCTGCGTAAGCGTATCGCCGCGCGTCTGCGAAAGCGGTTTATCCCCGCTGGCGCGGGGAACTCGCGGGATCGTCACCCTCAGCAGCGAAAGACAGTGGTTTATCCTCGCTGGTGCGGGGAACTCTCTAAAAGCTTACATTTGTTCTTAAAGCATTTTTTTCCATAAAAACAACCCATCAACCTTAGATCGGAAGAGCAC'
#seq <- DNAString(seq)
a = 0
for (i in 1:length(reads))
{
  seq = reads[[i]]
  match_fw  <- matchPattern(repeat_fw, seq, max.mismatch=4, with.indels=FALSE)
  matrix_match_fw = as.matrix(ranges(match_fw))
  match_rv  <- matchPattern(repeat_rv, seq, max.mismatch=4, with.indels=FALSE)
  matrix_match_rv = as.matrix(ranges(match_rv))
  match_fw2  <- matchPattern(repeat_fw, seq, max.mismatch=4, with.indels=TRUE)
  matrix_match_fw2 = as.matrix(ranges(match_fw2))
  match_rv2  <- matchPattern(repeat_rv, seq, max.mismatch=4, with.indels=TRUE)
  matrix_match_rv2 = as.matrix(ranges(match_rv2))
  if (length(matrix_match_fw) != length(matrix_match_fw2)) {a = a+1}
  if (length(matrix_match_rv) != length(matrix_match_rv)) {a = a+1}
  #print(paste ("FORWARD", length(matrix_match_fw), "REVERSE", length(matrix_match_rv), "FORWARD", length(matrix_match_fw2), "REVERSE", length(matrix_match_rv2)))
  #print(paste (length(matrix_match_fw), length(matrix_match_rv), length(matrix_match_fw2), length(matrix_match_rv2)))
}
print (a)
  #print (matrix_match_fw)
  #print("REVERSE")
  #print (matrix_match_rv)
  #print (length(matrix_match_rv))
  #for (i in 1:length(seqs)){}

