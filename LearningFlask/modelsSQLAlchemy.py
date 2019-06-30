from config import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

#这是一个用面向对象数据库ORM框架模式开发
# 用的是SQLAlchemy来链接，这是一个案例，如何来链接数据。

class BlogPost(db.Model):
    __tablename__ = "blogposts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String(512), nullable=False)
    author_id = db.Column(db.Integer, ForeignKey("users.id"))

    def __init__(self, title, description):
        self.title = title
        self.description = description

class User(db.Model):
    __tablename__ = "users"
    # 这里的意思是表的名字是 users 取出来的每一个对象是User
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128))
    posts = relationship("BlogPost", backref = "author")

    def __init__(self, name, email, password):
        self.name = name
        self.email =email
        self.password = password


