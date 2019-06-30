from flask_sqlalchemy import SQLAlchemy
from flask import Flask

#这是第二种链接数据库的方式ORM链接
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    "mysql+pymysql://root:123456@localhost/pythontestsql?charset=utf8"

db = SQLAlchemy(app)