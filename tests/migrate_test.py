from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stu.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    # age = db.Column(db.Integer)
    # foo  = db.Column(db.String(128))