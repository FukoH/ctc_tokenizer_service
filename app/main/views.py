from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
# from .forms import NameForm
from .. import db
# from ..models import User
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# @main.route('/', methods=['GET', 'POST'])
# def index():
#
#
#     form = NameForm()
#     if form.validate_on_submit():
#
#         return redirect(url_for('.index'))
#     return render_template('index.html',
#                            form=form, name=session.get('name'),
#                            known=session.get('known', False),
#                            current_time=datetime.utcnow())


@main.route('/vocabulary',methods=['GET'])
def sentence_jsonify():
    sentence = request.args.get('query',None)
    if not sentence.strip():
        return jsonify({'message':'文本为空'})

    #TODO 分词
    # 查库
    # 返回json
    results = session.query(sentence).all()
    return jsonify(restaurants=[r.serialize for r in results])