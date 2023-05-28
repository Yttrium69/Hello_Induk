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

class Option(db.Model):
    __tablename__="Option"
    id=Column(db.Integer, primary_key=True)
    item_id=Column(String(7))
    option_title=Column(String(50))
    option_price=Column(Integer)
    option_id=Column(String)


class Post(db.Model):
    __tablename__="Post"
    id=Column(db.Integer, primary_key=True)
    item_id=Column(String(7))
    capacity=Column(String)
    caution=Column(String(200))
    discription=Column(String(200))

class Order(db.Model):
    __tablename__="Order"
    id=Column(db.Integer, primary_key=True)
    order_id=Column(String(8))
    status=Column(String)
    item_id=Column(String(7))
    time=Column(String)
    count=Column(Integer)
    option_list=Column(String)
    user_id=Column(String)

class Wishlist(db.Model):
    __tablename__="Wishlist"
    id=Column(db.Integer, primary_key=True)
    user_id=Column(String)
    item_id=Column(String(7))