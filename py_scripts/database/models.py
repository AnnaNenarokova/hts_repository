#!/usr/bin/python
from peewee import *
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import *

class BaseModel(Model):
    class Meta:
        database = db
    return None

class Sequence(BaseModel):
    seq_id = CharField()
    seq_type = CharField()
    description = TextField(null=True)
    sequence = TextField()
    organism = CharField()
    source = CharField()

    @staticmethod	
    def read_from_fasta(fasta_path, seq_type, organism='unknown organism', source='unknown source'):
    	for record in SeqIO.parse(fasta_path, "fasta"):
    		Sequence.create(seq_id=record.id, seq_type=seq_type, description=record.description, sequence=record.seq, source=source)
		return None

   	def to_seqrecord(self):
    	if self.seq_type =='dna': alphabet = 'generic_dna'
    	elif self.seq_type == 'protein': alphabet = 'generic_protein'
    	else: 
    		print 'Error: Unsupported sequence type'
    		return False
    	seqrecord = SeqRecord(Seq(self.sequence, alphabet), id = seq_id, description = description)
    	return seqrecord

   	return None

class BlastHit(BaseModel):
	query = ForeignKeyField(Protein, related_name='query_hits')
	subject = ForeignKeyField(Protein, related_name='subject_hits')
	return None

	def create_from_dict(blast_dict):
		pass
