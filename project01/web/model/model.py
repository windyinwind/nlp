from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
'''
brew install mysql-connector-c
pip install mysqlclient
'''
Base = declarative_base()
class Speech(Base):
    __tablename__ = 'speeches'
    Id = Column(Integer, primary_key = True)
    Person = Column(String)
    Say_Word = Column(String)
    Speech = Column(String)


def db(config):
    username = config['USRENAME']
    password = config['PASSWORD']
    url = config['URL']
    eng = create_engine('mysql+mysqldb://'+username+':'+password+'@'+url+'/nlp?charset=utf8')
    
    Session = sessionmaker(bind=eng)
    ses = Session()
    return ses

def get_speeches(ses, speech_min_len = 10):

    rs = ses.query(Speech).filter(func.length(Speech.Speech) > speech_min_len)
    speeches = [{'person':speech.Person, 'speech':speech.Speech} for speech in rs if len(speech.Speech) > speech_min_len]
    return  speeches

def get_persons(ses, min_count=70):

    rs = ses.query(Speech.Person, func.count(Speech.Person)).group_by(Speech.Person).all()
    person_count = [{'text':speech[0], 'count':speech[1]} for speech in rs if speech[1] > min_count]
    return  person_count

def speeches_of(ses, person):
    speeches = ses.query(Speech.Speech).filter(Speech.Person == person).filter(func.length(Speech.Speech) > 10).all()
    return  speeches
