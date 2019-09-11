from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
'''
brew install mysql-connector-c
pip install mysqlclient
'''
eng = create_engine('mysql+mysqldb://weiliang:edanz@localhost/nlp')
Base = declarative_base()
Session = sessionmaker(bind=eng)
ses = Session()

class Speech(Base):
    __tablename__ = 'speeches'
    Id = Column(Integer, primary_key = True)
    Person = Column(String)
    Say_Word = Column(String)
    Speech = Column(String)


def get_speeches():

    rs = ses.query(Speech).limit(10)
    
    speeches = [(speech.Person, speech.Speech) for speech in rs if len(speech.Speech) > 2]
    return speeches


