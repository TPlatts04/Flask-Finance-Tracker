from finance_manager import db

class userInfo(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True, unique=True)
    username = db.Column("Username", db.String(24), unique=True)
    password = db.Column("Password", db.String, unique=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password