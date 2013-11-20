from app import db


class Snap(db.Model):
    __tablename__ = 'snap'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users_user.id'))
    date = db.Column(db.String(200))
    title = db.Column(db.String(200))
    mini = db.Column(db.String(200))
    imgName = db.Column(db.String(200))

    def __init__(self, title, mini, imgName):
        self.title = title
        self.mini = mini
        self.imgName = imgName


    def setSnap(self, imgName):
        self.imgName = imgName

    def getMini(self):
        return self.mini
