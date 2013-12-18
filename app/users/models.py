from app import db
from app.snap.models import Snap 

class User(db.Model):
    __tablename__ = 'users_user'

    id = db.Column(db.Integer, primary_key=True)
    userEmail = db.Column(db.String(80), unique=True)
    userPassword = db.Column(db.String(80))
    snap = db.relationship('Snap', backref='user', lazy='dynamic')
    test = "a"



    def __init__(self, email, password):
        self.userEmail = email
        self.userPassword = password

    def __repr__(self):
        return '<User %r>' % (self.userEmail)

    def getId(self):
        return self.id