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
