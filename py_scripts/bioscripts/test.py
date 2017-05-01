#!/usr/bin/python
l=[
"CTTTATT",
"GTTTCTG",
"TCTGTAC",
"TTTATTG",
"TTCTGTA",
"CTGTACT",
"TTTCTGT",
"CGCCCGT",
"CGCCCGG",
"GGGACCG",
"CCCGCCT",
"CGCCCAT",
"CCCGGAT",
"GTCGCAT",
"CGGGAAT",
"CGCCCCT",
"CGGGGAC",
"CCGGATT",
"CCCCCCT",
"CCGGCTT",
"CGCCGGG",
"CTCGGGG",
"AATCTAG",
"CGCGGCT",
"CGGAAAG",
"CCGGGAT",
"CCCGGGT",
"CCGGTAT",
"TCCGGAC",
"CCCGAGT",
"CCCCGCT",
"ACTTTAT",
"GTACTTT",
"TACTTTA",
"CTCGAAT",
"CGGTATA",
"CTCGGCT",
"CTCGGTT",
"CGGTCCC",
"TTCCGGG",
"CTCGAGT",
"CTCGGGT",
"CTCGGAT",
"CGCGCGC",
"CAGGACT"
]
forward="AACGCATTTTTTGTTACAGTTTCTGTACTTTATTG"
reverse="CAATAAAGTACAGAAACTGTAACAAAAAATGCGTT"

sl_f=[]
sl_r=[]
rest=[]

for i in l:
    if forward.find(i) != -1:
        sl_f.append(i)
    elif reverse.find(i) != -1:
        sl_r.append(i)
    else:
        rest.append(i)

print sl_f
print sl_r
print rest
