from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
'''
brew install mysql-connector-c
pip install mysqlclient
'''
eng = create_engine('mysql+mysqldb://root:edanz@localhost/nlp?charset=utf8')
Base = declarative_base()
Session = sessionmaker(bind=eng)
ses = Session()

class Speech(Base):
    __tablename__ = 'speeches'
    Id = Column(Integer, primary_key = True)
    Person = Column(String)
    Say_Word = Column(String)
    Speech = Column(String)


def get_speeches(speech_min_len = 10):

    rs = ses.query(Speech).filter(func.length(Speech.Speech) > speech_min_len)
    speeches = [{'person':speech.Person, 'speech':speech.Speech} for speech in rs if len(speech.Speech) > speech_min_len]
    return  speeches


