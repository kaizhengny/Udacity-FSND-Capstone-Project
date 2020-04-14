import os
import json
from sqlalchemy import Column, String, Integer, DateTime
from flask_sqlalchemy import SQLAlchemy


os.environ['DATABASE_URL'] = 'postgres://udqijabqbykwjn:52395c47e4fda825b612692ac7546993462f1d06a35342525193a22936cc88d6@ec2-54-80-184-43.compute-1.amazonaws.com:5432/d8v0vk8ncinddo'
database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


# Movie
# With attribute title and releasedate

class Movie(db.Model):  
    __tablename__ = 'Movie'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    releasedate = Column(String)
    #actor_id = Column(Integer,ForeignKey('actor.id'), nullable=True)

    def __init__(self, title, releasedate):
        self.title = title
        self.releasedate = releasedate
        #self.actor_id = actor_id

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
        'id': self.id,
        'title': self.title,
        'releasedate': self.releasedate
        #'actor': Actor.query.filter(id==self.actor_id).with_entities(name)
        }


# Actor
# With attribute name, age and gender

class Actor(db.Model):
    __tablename__ = 'Actor'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age =  Column(Integer)
    gender = Column(String)

    def __init__(self, name, age, gender):
        self.name = name 
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()
  
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
        'id': self.id,
        'name': self.name,
        'age': self.age,
        'gender':self.gender
    }

