from server import db

class Future(db.Model):
    ID = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    prize = db.Column(db.Integer)
    fortune = db.Column(db.string(150))
    