from . import api
from flask import request, jsonify
from .errors import bad_request
from ..models import Vocabulary

@api.route('/vocabulary',methods=['GET'])
def sentence_jsonify():
    sentence = request.args.get('query',None)
    if sentence is None :
        return bad_request('文本为空')

    return jsonify(Vocabulary(sentence).query_dict)
