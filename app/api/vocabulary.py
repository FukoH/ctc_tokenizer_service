from . import api
from flask import request, jsonify
from flask import session
from .errors import bad_request

@api.route('/vocabulary',methods=['GET'])
def sentence_jsonify():
    sentence = request.args.get('query',None)
    if not sentence.strip():
        return bad_request('文本为空')

    #TODO 分词
    # 查库
    # 返回json
    results = session.query(sentence).all()
    return jsonify(restaurants=[r.serialize for r in results])