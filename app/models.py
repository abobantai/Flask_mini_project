from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
class Bio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bio = db.Column(db.String(200), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user = db.relationship('User', backref=db.backref('bio', lazy=True))
    avatar = db.Column(db.String(120), nullable=True)

