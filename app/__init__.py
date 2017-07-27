from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from .views.api.v1.users import api_v1_users
app.register_blueprint(api_v1_users, url_prefix='/api/v1/users')

from .views.users import users
app.register_blueprint(users, url_prefix='/users')

@app.route('/')
def hello_world():
  return 'Hello, World!'

app.secret_key = 'ce1b2d429a34d5371776785aac26002f654d7fe08bf387e082607571fc6f770bebd113cc5c821d216af5d5abfc01ae9f0c79c8db324c10aed9bfaad7fc7223fa'