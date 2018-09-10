import jieba
import config
jieba.initialize()

class Tokenizer:

    def __init__(self,dict_path):
        jieba.load_userdict(dict_path)
        jieba.initialize()

    def cut(self,sentence):
        jieba.cut(sentence,)