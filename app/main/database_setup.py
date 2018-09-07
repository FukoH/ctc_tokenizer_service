import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Vocabulary(Base):
    __tablename__ = 'vocabulary'

    id = Column(Integer, primary_key=True)
    value = Column(String(32), nullable=False)
    type = Column(Integer, primary_key=False)
    sub_type = Column(String(32), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'value':self.value,
            'type':self.type,
            'sub_type':self.sub_type
        }


#TODO 连接数据库
engine = create_engine('sqlite:///restaurantmenu.db')


Base.metadata.create_all(engine)
