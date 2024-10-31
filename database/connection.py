from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from database.models import *

DB_URL = "postgresql://admin:1234@localhost:5437/missions_db"
engine = create_engine(DB_URL, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, # don't commit changes'
                                         autoflush=False,
                                         bind=engine))

def init_db():
    import database.models
    Base.metadata.create_all(bind=engine)