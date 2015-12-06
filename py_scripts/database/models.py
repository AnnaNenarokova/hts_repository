#!/usr/bin/python
from peewee import *
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import *

db_path = '/home/anna/bioinformatics/euglenozoa/mitoproteome.db'
db = SqliteDatabase(db_path)

class BaseModel(Model):
    class Meta:
        database = db

class Sequence(BaseModel):
    seq_id = CharField(index=True)
    seq_type = CharField()
    description = TextField(null=True)
    sequence = TextField()
    organism = CharField()
    source = CharField(index=True)

    @staticmethod
    def read_from_fasta(fasta_path, seq_type, organism='unknown organism', source='unknown source'):
        with db.atomic():
            for record in SeqIO.parse(fasta_path, "fasta"):
                Sequence.create(seq_id=record.id, seq_type=seq_type, description=record.description,
                                sequence=record.seq, organism=organism, source=source)

    def to_seqrecord(self):
        if self.seq_type =='dna': alphabet = 'generic_dna'
        elif self.seq_type == 'protein': alphabet = 'generic_protein'
        else:
            print 'Error: Unsupported sequence type'
            return False
        seqrecord = SeqRecord(Seq(self.sequence, alphabet), id = seq_id, description = description)
        return seqrecord

class BlastHit(BaseModel):
    query = ForeignKeyField(Sequence, related_name='query_hits')
    subject = ForeignKeyField(Sequence, related_name='subject_hits')

    @staticmethod
    def create_from_dict(blast_dicts):
        with db.atomic():
            for blast_dict in blast_dicts:
                query_id, subject_id = blast_dict['qseqid'], blast_dict['sseqid']
                if query_id and subject_id:
                    query = Sequence.select().where(Sequence.seq_id == query_id).get()
                    subject = Sequence.select().where(Sequence.seq_id == subject_id).get()
                    BlastHit.create(query=query, subject=subject)