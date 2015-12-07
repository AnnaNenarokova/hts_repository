#!/usr/bin/python
from peewee import *
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import *
import simplejson as json

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
    localisation = CharField(null=True)
    function = TextField(null=True, index=True)

    @staticmethod
    def read_from_f(fasta_path, seq_type, organism='unknown organism', source='unknown source', info_dict=False):
        with db.atomic():
            for record in SeqIO.parse(fasta_path, "fasta"):
                seq_id = record.id
                other_data = {}
                other_data['sequence'] = str(record.seq)
                other_data['description'] = str(record.description)
                if info_dict:
                    localisation = info_dict[seq_id]['localisation']
                    function = info_dict[seq_id]['function']
                    for feature in blast_dict:
                        if feature not in ['localisation', 'function']:
                            other_features[feature] = blast_dict[feature]
                    Sequence.create(seq_id=seq_id, seq_type=seq_type, organism=organism, source=source,
                                    extra_data=other_data, localisation=localisation, function=function)
                else:
                    Sequence.create(seq_id=seq_id, seq_type=seq_type, organism=organism, source=source,
                                    extra_data=other_data)


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