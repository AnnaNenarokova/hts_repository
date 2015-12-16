#!/usr/bin/python
from peewee import *
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/")
from database.models import *
from py_scripts.common_helpers.parse_csv import *
import csv

def exclude_bad_functions():
    bad_functions = ['dynein', 'kinesin', 'tubulin', 'actin', 'myosin',
                 'clathrin', 'centrin',
                 'retrotransposon', 'repeat',
                 'mterf',
                 'ras',
                 'rab',
                 'kinase',
                 'phosphatase',
                 'adp-ribosylation',
                 'receptor',
                 'calmodulin',
                 'cyclophilin',
                 'transporter', 'transport', 'carrier', 'atp-binding', 'translocase', 'translocator',
                 'membrane-spanning ATPase',
                 'pump',
                 'chaperon', 'chaperonin',
                 'histone', 'dnaj',
                 'peptidase', 'protease',
                 'proteasome',
                 'ubiquitin',
                 'leucine-rich',
                 'helicase', 'recq',
                 'dead', 'deah',
                 'williams-beuren',
                 'heat',
                 'binding', 'binds',
                 'multidrug resistance protein',
                 # 'hypothetical',
                 # 'protein of unknown function',
                 # 'putative protein',
                 # 'unspecified product'
                 ]

    functions = " "
    for word in bad_functions:
        not_like = "and" + " lower(subject.function)" + "not like" + " '%" + word + "%'\n"
        functions += not_like

    return functions

def make_count_query(featuresn, verbose=False):
    count_on_blasthits = """
    select count(*) from
    (select * from sequence query
    inner join blasthit on blasthit.query_id = query.id
    inner join sequence as subject on blasthit.subject_id = subject.id
    where query.organism = 'Euglena gracilis'
    """
    group_by_query = " group by query.id) "

    raw_query = count_on_blasthits + features + group_by_query
    if verbose: print raw_query

    cursor = db.execute_sql(raw_query)
    tuples = cursor.fetchall()
    return tuples[0][0]

def make_select_query(features):
    select_on_blasthits = """
    select * from sequence query
    inner join blasthit on blasthit.query_id = query.id
    inner join sequence as subject on blasthit.subject_id = subject.id
    where query.organism = 'Euglena gracilis'
    """
    group_by_query = " group by query.id "

    raw_query = select_on_blasthits + features + group_by_query
    results = Sequence.raw(raw_query)
    return results

count_euglena = "select count(*) from sequence where query.organism = 'Euglena gracilis'"



tripa = " subject.organism = 'Tripanosoma brucei' "
homo = " subject.organism = 'Homo sapiens' "
yeast_mito = " (subject.organism = 'Saccharomyces cerevisiae' and subject.mitoscore = 100) "

blast_threshold = " (blasthit.evalue < 0.00001 and blasthit.alen_slen > 0.3) "



organisms = "(" +  homo + "or" + tripa +  ")"

functions = exclude_bad_functions()

# features = "and" + organisms + "and" + " query.loc='M' " + "and" + " query.locrate<=2 " + functions + "and" + blast_threshold

features = "and" + organisms + functions + "and" + blast_threshold

print make_count_query(features)

seqs = make_select_query(features)

csv_out = []

for seq in seqs:
    csv_out.append([seq.organism, seq.seqid, seq.function])

csv_out = sorted(csv_out, key=lambda protein: protein[2])

outfile = '/home/anna/bioinformatics/euglenozoa/euglena/filtered_functions.csv'

header = ['organism', 'seqid', 'function']

write_list_of_lists(csv_out, outfile, header=header)