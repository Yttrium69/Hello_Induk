from flask_sqlalchemy import SQLAlchemy
from server import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32))
    user_pw = db.Column(db.String(32))
    user_name=db.Column(db.String(32))
    def __init__(self, user_id, user_name, user_pw):
        self.user_id=user_id
        self.user_name=user_name
        self.user_pw=user_pw