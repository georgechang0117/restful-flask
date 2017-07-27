from .. import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.Text)


    def __init__(self, email, password, username):
      self.email = email
      self.set_password(password)
      self.username = username

    def set_password(self, password):
      self.password_hash = generate_password_hash(password)

    def check_password(self, password):
      return check_password_hash(self.password_hash, password)

    def __repr__(self):
      return '<User %r>' % self.username

    @classmethod
    def login(cls, email, password):
      user = cls.query.filter_by(email = email).first()
      if user != None:
        if user.check_password(password):
          return user
        else:
          return None
      return None
