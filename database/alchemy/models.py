import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import sqlalchemy.types as types
import simplejson as json
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import *

Base = declarative_base()

class SerializedDictField(types.TypeDecorator):
    impl = types.Text

    def process_bind_param(self, value, dialect):
        if value == None: return None
        else: return json.dumps(value)

    def process_result_value(self, value, dialect):
        if value == None: return None
        else: return json.loads(value)

class Sequence(Base):
    __tablename__ = 'sequence'

    id = Column(Integer, primary_key=True)
    seqid = Column(String(255), nullable=False, index=True)
    seqtype = Column(String(255), nullable=False)
    organism = Column(String(255), nullable=False)
    source = Column(String(255))
    og = Column(String(255))
    function = Column(Text())
    mitochondrial = Column(Boolean())
    mitoscore = Column(Float())
    loc = Column(String(255))
    locrate = Column(Integer())
    extra_data = Column(SerializedDictField())

    query_blasthits = relationship("BlastHit", foreign_keys="BlastHit.query_id")
    subject_blasthits = relationship("BlastHit", foreign_keys="BlastHit.subject_id")

    queries = relationship('Sequence', secondary='blasthit',
        primaryjoin=("Sequence.id == BlastHit.subject_id"),
        secondaryjoin=("Sequence.id == BlastHit.query_id"))

    subjects = relationship('Sequence', secondary='blasthit',
        primaryjoin=("Sequence.id == BlastHit.query_id"),
        secondaryjoin=("Sequence.id == BlastHit.subject_id"))

    def to_seqrecord(self):
        if self.seqtype =='dna': alphabet = 'generic_dna'
        elif self.seqtype == 'prot': alphabet = 'generic_protein'
        else:
            print 'Error: Unsupported sequence type'
            return False
        seqrecord = SeqRecord(Seq(self.extra_data['sequence'], alphabet), name='', id = self.seqid, description = '')
        return seqrecord

class BlastHit(Base):
    __tablename__ = 'blasthit'

    id = Column(Integer, primary_key=True)
    evalue = Column(Float(), nullable=False)
    length = Column(Integer(), nullable=False)
    alen_qlen = Column(Float(), nullable=False)
    alen_slen = Column(Float(), nullable=False)
    slen = Column(Float(), nullable=False)
    qlen = Column(Float(), nullable=False)
    extra_data = Column(SerializedDictField())

    query_id = Column(Integer, ForeignKey("sequence.id"))
    query = relationship("Sequence", primaryjoin=(query_id == Sequence.id))

    subject_id = Column(Integer, ForeignKey("sequence.id"))
    subject = relationship("Sequence", primaryjoin=(subject_id == Sequence.id))