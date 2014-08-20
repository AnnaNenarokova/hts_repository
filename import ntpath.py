import ntpath

def get_file_path(path):
    head, tail = ntpath.split(path)
    dir_path = [head, tail]
    return dir_path

print get_file_path('/home/anna/HTS_programming/HTS_spacers/CTG_CCGTCC_L001_1.fastq')