#!/usr/bin/python
infile_path = '/home/anna/bioinformatics/euglenozoa_anzhelika/Dataset_cd_hit_est_0_9/Results_Aug07/WorkingDirectory/OrthologousGroups.txt'
infile = open(infile_path, 'r')
id_path="/home/anna/bioinformatics/euglenozoa_anzhelika/Dataset_cd_hit_est_0_9/complete_ORFs/all_complete_ORFs.txt"
complete = []
with open(id_path) as id_file:
    for line in id_file:
        complete.append(line.rstrip())
    id_file.close()

og_count=0

for row in infile:
    sp_count = {
    "Ngru": 0,
    "Rcos": 0,
    "Egym": 0,
    "Egracilis": 0,
    "Dpapillatum": 0,
    "Ndes": 0,
    "Bsal": 0,
    "Tbru": 0,
    "Lmaj": 0
    }
    og = row[:9]
    ids = row[11:].rstrip().split(" ")
    count = len(ids)
    if count >= 9:
        for id in ids:
            for sp in sp_count:
                if sp in id:
                    if id in complete:
                        sp_count[sp]+=1

    complete_count = 0
    for sp in sp_count:
        if sp_count[sp] > 0:
            complete_count += 1

    if complete_count == 9:
        og_count += 1
print og_count

