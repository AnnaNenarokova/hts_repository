from models import *

Sequence.__table__.drop(engine)
BlastHit.__table__.drop(engine)

Base.metadata.create_all(engine)

