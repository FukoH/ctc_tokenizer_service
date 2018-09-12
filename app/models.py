from flask import current_app
from sqlalchemy import Column, Integer, String
from . import db
import jieba
import jieba.posseg as pseg


# jieba.load_userdict(current_app.config['DICT_PATH'])
# jieba.initialize()


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
            'value': self.value,
            'type': self.type,
            'sub_type': self.sub_type
        }

    def __init__(self, sentence):
        words = pseg.cut(sentence)
        js = {}
        condition = []
        groupBy = []
        target = []
        for word, flag in words:
            if not flag.startswith('type'):
                continue

            for tags in flag.split('z'):  # tags: typexconditionz keyxdept    typextarget
                key_value = tags.split('x')
                if key_value[0] == 'type':
                    if key_value[1] == 'target':
                        target.append(word)
                elif key_value[0] == 'key':
                    condition.append({'key': key_value[1], 'value': word, 'relation': '='})
                elif key_value[0] == 'groupBy':
                    groupBy.append({'value': key_value[1]})
        js['target'] = target
        js['condition'] = condition
        js['groupBy'] = groupBy

        self.query_dict = js
