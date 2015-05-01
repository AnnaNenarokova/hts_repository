import re

f = sys.argv[1]
f = open(f_name, 'r')

f_out_name = f_name[0:-8] + '_filtered.vcf'
out = []
for line in f.readlines():
	match = re.match('.*DP4=((\d+),(\d+),(\d+),(\d+)).*', line)
	if match:
	  a = float(match.group(2))
	  b = float(match.group(3))
	  c = float(match.group(4))
	  d = float(match.group(5))
	fw_rv_ratio = (a + c)/(b + d)
	if fw_rv_ratio < 5 and fw_rv_ratio > 0.2:
		out.append(line)

f_out = open(f_out_name, 'w')
out_file.write(out)