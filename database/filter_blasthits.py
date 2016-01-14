import sqlite3
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.raw_query_to_dict import *
from py_scripts.common_helpers.parse_csv import *

db_path = "/home/anna/Dropbox/PhD/mitoproteome.db"

query = """
    SELECT *,
        query.seqid as query_id,
        subject.seqid as subject_id,
        query.function as query_function,
        subject.function as subject_function,
        query.loc as query_loc,
        subject.loc as subject_loc,
        query.locrate as query_locrate,
        subject.locrate as subject_locrate,
        query.mitoscore as query_mitoscore,
        subject.organism as subject_organism
    FROM sequence query
    INNER JOIN blasthit ON blasthit.query_id = query.id
    INNER JOIN sequence AS subject ON subject.id = blasthit.subject_id
    WHERE query.organism = 'Euglena gracilis'
    AND blasthit.evalue < 0.00001 AND blasthit.alen_slen > 0.3
    AND (subject.organism = 'Tripanosoma brucei'
        OR  subject.organism = 'Homo sapiens'
        OR (subject.organism = 'Saccharomyces cerevisiae' AND subject.mitoscore = 100))
"""

rows = exe_query(query, db_path)
query_dict = dict_list_to_dict(rows, 'query_id')

very_bad_functions = [
                 'dynein', 'kinesin', 'tubulin', 'actin', 'myosin',
                 'clathrin', 'centrin',
                 'transposon', 'repeat',
                 'mterf',
                 'ras',
                 'rab',
                 'kinase',
                 'phosphatase',
                 'adp-ribosylation',
                 'receptor',
                 'calmodulin',
                 'cyclophilin',
                 'transport', 'carrier', 'transloc', 'ABC', 'permease',
                 'pump',
                 'stomatin',
                 'chaperon', 'chaperonin',
                 'histone', 'dnaj',
                 'peptidase', 'protease',
                 'proteasome',
                 'ubiquitin',
                 'leucine-rich',
                 'dead', 'deah',
                 'williams-beuren',
                 'poly(a) binding protein',
                 'aldo-keto reductase',
                 'mrb1',
                 'heat shock',
                 'kiaa0141',
                 'thioredoxin reductase', 'glutathione reductase', 'trypanothione reductase', 'mercuric reductase', 'lipoamide dehydrogenase'
                 ]

bad_functions = [
                 'heat',
                 'zinc-finger', 'zinc finger',
                 'multidrug resistance protein',
                 'binding',
                 'hypothetical',
                 'protein of unknown function',
                 'putative protein',
                 'unspecified product'
                 ]

needed_keys = [
    "subject_function",
    "query_function",
    "evalue",
    "subject_organism",
    "qlen",
    "slen",
    "length",
    "alen_slen",
    "alen_qlen",
    "query_mitoscore",
    "query_loc",
    "query_locrate",
    "subject_loc",
    "subject_locrate",
    "query_id",
    "subject_id"
    ]

print len(query_dict)

results = {}

for query in query_dict:
    function_is_good = True
    for hit in query_dict[query]:
        if function_is_good:
            for function in very_bad_functions:
                if function in hit['subject_function'].lower():
                    function_is_good = False
                    break
    if function_is_good:
        results[query] = sorted(query_dict[query], key=lambda blasthit: float(blasthit['evalue']))

print len(results)
print ''

csv_list = []
i=0
for query in results:
    for blasthit in results[query]:
        row = []
        for key in needed_keys:
            row.append(blasthit[key])
        csv_list.append(row)
        i+=1
    csv_list.append([])

print i

outfile = '/home/anna/bioinformatics/euglenozoa/euglena/filtered_results.csv'
write_list_of_lists(csv_list, outfile, delimiter=',', header=needed_keys)

# i=0
# for key in results:
#     if i<500:
#         # print key
#         for blasthit in results[key]:
#             for k in blasthit.keys():
#                 print k
#             exit(0)
#             print blasthit['subject_function']
#         print ''
#     i+=1