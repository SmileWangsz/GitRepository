from config import db
from modelsSQLAlchemy import User, BlogPost

#create database and table create
db.create_all()


#insert data
db.session.add(User("micka", "kala@gmail.com", "1234556"))
db.session.add(User("nial", "nial@gmail.com", "1234556"))
db.session.add(User("admin", "admin@gmail.com", "1234556"))
db.session.add(User("wangsz", "wangsz@gmail.com", "1234556"))

db.session.add(BlogPost("Good", "I\'m good " ))
db.session.add(BlogPost("Well", "I\'m well " ))
db.session.add(BlogPost("Nice", "I\'m nice " ))
db.session.add(BlogPost("Okay", "I\'m okay " ))
db.session.add(BlogPost("Right", "I\'m right " ))
db.session.add(BlogPost("Stupid", "I\'m stupit " ))


db.session.commit()

