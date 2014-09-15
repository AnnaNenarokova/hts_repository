def get_length(inputStr):
        return len(inputStr)
f = open("/home/anna/bioinformatics/HTS-all/HTS-programming/CTG_CCGTCC_L001_1/statistics_file.txt", "r+")
f_sort = open("/home/anna/bioinformatics/HTS-all/HTS-programming/CTG_CCGTCC_L001_1/statistics_sort.txt", 'w')
lines = []
for line in f.readline():
	lines.append(lines)
print lines
lines.sort(key=get_length)
for line in lines:
	f_sort.write(lines)
f.close()
f_sort.close()