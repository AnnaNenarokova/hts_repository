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
    AND ( (subject.organism = 'Trypanosoma brucei' AND subject.mitoscore = 100)
        OR  subject.organism = 'Homo sapiens'
        OR (subject.organism = 'Saccharomyces cerevisiae' AND subject.loc = 'Mito'))
"""

rows = exe_query(query, db_path)
query_dict = dict_list_to_dict(rows, 'query_id')

bad_functions = [
                 # 'dynein', 'kinesin', 'tubulin', 'actin', 'myosin', 'formin',
                 # 'clathrin', 'centrin',
                 # 'transposon', 'repeat','ppr',
                 # 'mterf',
                 # 'ras',
                 # 'rab',
                 # 'kinase', 'phosphatase',
                 # 'adp-ribosylation',
                 # 'receptor',
                 # 'cyclophilin',
                 # 'transport', 'carrier',
                 # 'mrp', 'transloc', 'abc', 'permease', 'porter', 'atp-binding cassette',
                 # 'lactamase',
                 # 'pump',
                 # 'endosomal integral membrane protein; putative',
                 # 'stomatin',
                 # 'chaperon', 'chaperonin',
                 # 'histon', 'dnaj', 'nucleosome remodeling',
                 # 'peptidas', 'protease',
                 # 'proteasome',
                 # 'ubiquitin',
                 # 'leucine-rich', 'leucine zipper',
                 # 'dead', 'deah',
                 # 'williams-beuren',
                 # 'poly(a) binding protein',
                 # 'mrb1-',
                 # 'kiaa0141'
                 ]

needed_keys = [
    "query_id",
    "query_function",
    "query_mitoscore",
    "query_loc",
    "query_locrate",
    "subject_id",
    "subject_organism",
    "subject_function",
    "subject_loc",
    "subject_locrate",
    "evalue",
    "qlen",
    "slen",
    "length",
    "alen_slen",
    "alen_qlen"
    ]

print len(query_dict)

results = {}

for query in query_dict:
    function_is_good = True
    for hit in query_dict[query]:
        if function_is_good:
            for function in bad_functions:
                if function in hit['subject_function'].lower():
                    function_is_good = False
                    break
    if function_is_good:
        results[query] = sorted(query_dict[query], key=lambda blasthit: float(blasthit['evalue']))

print len(results)

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

csv_list = []
function_list = []

for query in results:
    is_first = True
    for blasthit in results[query]:
        row = []
        for key in needed_keys:
            row.append(blasthit[key])

        if is_first == True:
            best_row = row
            is_first = False

        is_best = True
        non_specific_functions = [
                 # 'hypothetical',
                 # 'protein of unknown function',
                 # 'putative protein',
                 # 'unspecified product',
                 # 'circadian clock',
                 # 'insulin',
                 # 'crystallin',
                 # 'carcinoma',
                 # 'tumor',
                 # 'death',
                 # 'apoptosis',
                 # 'chromosome',
                 # 'growth',
                 # 'heat',
                 # 'prostaglandin'
                 ]
        for function in non_specific_functions:
            if function in blasthit['function']:
                is_best = False

        if is_best == True:
            best_row = row
            break

    csv_list.append(best_row)
    function_list.append(best_row[7])

function_set = set(function_list)
print len(function_set)

outfile = '/home/anna/bioinformatics/euglena_project/euglena/filtered_results.csv'
write_list_of_lists(csv_list, outfile, delimiter=',', header=needed_keys)

csv_list_functions = []

for function in function_set:
    csv_list_functions.append([function])

outfile = '/home/anna/bioinformatics/euglena_project/euglena/filtered_set_of_functions.csv'
write_list_of_lists(csv_list_functions, outfile, delimiter=',')

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