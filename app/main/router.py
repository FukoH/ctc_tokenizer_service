from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main.database_setup import Base

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/vocabulary',methods=['GET'])
def sentence_jsonify():
    sentence = request.args.get('query',None)
    if not sentence.strip():
        return jsonify({'message':'文本为空'})

    #TODO 分词
    # 查库
    # 返回json
    results = session.query(sentence).all()
    return jsonify(restaurants=[r.serialize for r in results])



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
