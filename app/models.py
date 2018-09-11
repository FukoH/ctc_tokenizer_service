
from flask import current_app
from sqlalchemy import Column, Integer, String
from . import db
import jieba

jieba.load_userdict(current_app.config['DICT_PATH'])
jieba.initialize()

class Vocabulary(db.Model):


    __tablename__ = 'vocabulary'

    id = Column(Integer, primary_key=True)
    value = Column(String(32), nullable=False)
    type = Column(Integer, nullable=False)
    sub_type = Column(String(32), nullable=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'value':self.value,
            'type':self.type,
            'sub_type':self.sub_type
        }

    def __init__(self,sentence):
        jieba.cut(sentence)

