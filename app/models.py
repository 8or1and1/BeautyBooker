from datetime import datetime

from sqlalchemy.orm import relationship

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    middle_name = db.Column(db.String(64))
    birthday = db.Column(db.DateTime)
    phone = db.Column(db.String(20))
    master = db.relationship("Master", uselist=False, backref="user")


    def __repr__(self):
        return '<User {}>'.format(self.username)


class Master(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    service_type = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Master {}>'.format(self.service_type)