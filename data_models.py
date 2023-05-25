from sqlalchemy import Column, Integer, String, ARRAY
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class User(db.Model):
    __tablename__="User"

    id = Column(db.Integer, primary_key=True)
    user_id = Column(String(32), )
    user_pw = Column(String(32))
    user_name=Column(String(32))
    def __init__(self, user_id, user_name, user_pw):
        self.user_id=user_id
        self.user_name=user_name
        self.user_pw=user_pw

class Item(db.Model):
    __tablename__="Item"

    id=Column(db.Integer, primary_key=True)
    item_id=Column(String(7))
    name=Column(String(20))
    price=Column(Integer)
    discount=Column(Integer)
    def __init__(self, id, name, price, discount):
        self.item_id=id
        self.name=name
        self.price=price
        self.discount=discount