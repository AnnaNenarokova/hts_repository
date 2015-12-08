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
    seq_id = CharField(index=True)
    seq_type = CharField()
    organism = CharField()
    source = CharField()
    mitoscore = FloatField(null=True)
    localisation = CharField(null=True)
    loc_rate = IntegerField(null=True)
    function = TextField(null=True, index=True)

    @staticmethod
    def read_from_f(fasta_path, seq_type, organism='unknown organism', source='unknown source', loc_dict=False, function_dict=False):
        with db.atomic():
            for record in SeqIO.parse(fasta_path, "fasta"):
                seq_id = record.id
                other_data = {}
                other_data['sequence'] = str(record.seq)
                other_data['description'] = str(record.description)
                if loc_dict:
                    if 'localisation' in loc_dict[seq_id].keys():
                        localisation = loc_dict[seq_id]['localisation']
                    else: localisation = None
                    if 'loc_rate' in loc_dict[seq_id].keys():
                        loc_rate = int(loc_dict[seq_id]['loc_rate'])
                    else: loc_rate = None
                    for key in loc_dict[seq_id]:
                        if key not in ['localisation', 'loc_rate']:
                            other_data[key] = loc_dict[seq_id][key]
                else:
                    localisation, loc_rate = None, None

                if function_dict:
                    if 'function' in function_dict[seq_id].keys():
                        function = function_dict[seq_id]['function']
                    else: function = None
                    if 'mitoscore' in function_dict[seq_id].keys():
                        mitoscore = float(function_dict[seq_id]['mitoscore'])
                    else: mitoscore = None
                    for key in function_dict[seq_id]:
                        if key not in ['function', 'mitoscore']:
                            other_data[key] = function_dict[seq_id][key]
                else:
                    function, mitoscore = None, None

                Sequence.create(seq_id=seq_id, seq_type=seq_type, organism=organism, source=source, extra_data=other_data,
                                localisation=localisation, loc_rate=loc_rate, function=function, mitoscore=mitoscore)

    def to_seqrecord(self):
        if self.seq_type =='dna': alphabet = 'generic_dna'
        elif self.seq_type == 'protein': alphabet = 'generic_protein'
        else:
            print 'Error: Unsupported sequence type'
            return False
        seqrecord = SeqRecord(Seq(self.extra_data['sequence'], alphabet), id = seq_id, description = description)
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

                query = Sequence.select().where(Sequence.seq_id == query_id).get()
                subject = Sequence.select().where(Sequence.seq_id == subject_id).get()
                BlastHit.create(query=query, subject=subject, evalue=evalue, length=length,
                                qlen=qlen, slen=slen, alen_qlen=alen_slen, alen_slen=alen_slen,
                                extra_data=other_features)