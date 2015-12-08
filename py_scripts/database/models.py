#!/usr/bin/python
from peewee import *
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import *
import simplejson as json
import sys
sys.path.insert(0, "/home/anna/bioinformatics/ngs/py_scripts/")
from common_helpers.parse_csv import *

db_path = '/home/anna/bioinformatics/euglenozoa/mitoproteome.db'
db = SqliteDatabase(db_path)

class SerializedDictField(TextField):
    def db_value(self, value):
        if value == None: return None
        else: return json.dumps(value)

    def python_value(self, value):
        if value == None: return None
        else: return json.loads(value)

class BaseModel(Model):
    class Meta:
        database = db
    extra_data = SerializedDictField(null=True)

class Sequence(BaseModel):
    seqid = CharField(index=True)
    seqtype = CharField()
    organism = CharField()
    source = CharField()
    mitoscore = FloatField(null=True)
    loc = CharField(null=True)
    locrate = IntegerField(null=True)
    function = TextField(null=True, index=True)

    @staticmethod
    def read_from_f(fasta_path, seqtype, organism='unknown organism', source='unknown source', loc_dict=False, function_dict=False):
        with db.atomic():
            for record in SeqIO.parse(fasta_path, "fasta"):
                seqid = record.id
                other_data = {}
                other_data['sequence'] = str(record.seq)
                other_data['description'] = str(record.description)
                if loc_dict:
                    if 'loc' in loc_dict[seqid].keys():
                        loc = loc_dict[seqid]['loc']
                    else: loc = None
                    if 'locrate' in loc_dict[seqid].keys():
                        locrate = int(loc_dict[seqid]['locrate'])
                    else: locrate = None
                    for key in loc_dict[seqid]:
                        if key not in ['loc', 'locrate']:
                            other_data[key] = loc_dict[seqid][key]
                else:
                    loc, locrate = None, None

                if function_dict:
                    if 'function' in function_dict[seqid].keys():
                        function = function_dict[seqid]['function']
                    else: function = None
                    if 'mitoscore' in function_dict[seqid].keys():
                        mitoscore = float(function_dict[seqid]['mitoscore'])
                    else: mitoscore = None
                    for key in function_dict[seqid]:
                        if key not in ['function', 'mitoscore']:
                            other_data[key] = function_dict[seqid][key]
                else:
                    function, mitoscore = None, None

                Sequence.create(seqid=seqid, seqtype=seqtype, organism=organism, source=source, extra_data=other_data,
                                loc=loc, locrate=locrate, function=function, mitoscore=mitoscore)

    def to_seqrecord(self):
        if self.seqtype =='dna': alphabet = 'generic_dna'
        elif self.seqtype == 'protein': alphabet = 'generic_protein'
        else:
            print 'Error: Unsupported sequence type'
            return False
        seqrecord = SeqRecord(Seq(self.extra_data['sequence'], alphabet), id = seqid, description = description)
        return seqrecord

class BlastHit(BaseModel):
    query = ForeignKeyField(Sequence, related_name='query_hits')
    subject = ForeignKeyField(Sequence, related_name='subject_hits')
    evalue = FloatField()
    length = IntegerField()
    alen_qlen = FloatField()
    alen_slen = FloatField()

    @staticmethod
    def create_from_dicts(blast_dicts):
        with db.atomic():
            for blast_dict in blast_dicts:
                query_id, subject_id = blast_dict['qseqid'], blast_dict['sseqid']
                evalue, length = blast_dict['evalue'], blast_dict['length']
                qlen, slen = blast_dict['slen'], blast_dict['qlen']
                alen_qlen, alen_slen = float(length/qlen), float(length/slen)
                other_features = {}
                for feature in blast_dict:
                    if feature not in ['qseqid', 'sseqid', 'evalue', 'length']:
                        other_features[feature] = blast_dict[feature]

                query = Sequence.select().where(Sequence.seqid == query_id).get()
                subject = Sequence.select().where(Sequence.seqid == subject_id).get()
                BlastHit.create(query=query, subject=subject, evalue=evalue, length=length,
                                qlen=qlen, slen=slen, alen_qlen=alen_slen, alen_slen=alen_slen,
                                extra_data=other_features)
