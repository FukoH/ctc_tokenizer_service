from . import api
from flask import request, jsonify
from .errors import bad_request
from ..models import Vocabulary
import json

@api.route('/vocabulary',methods=['GET'])
def sentence_jsonify():
    sentence = request.args.get('query',None)
    callback = request.args.get('callback', None)
    if sentence is None or callback is None:
        return bad_request('文本为空')
    json_str= json.dumps(Vocabulary(sentence).query_dict,ensure_ascii=False)
    result = callback+'(\''+json_str+'\')'
    return result
    # return jsonify(Vocabulary(sentence).query_dict)
