from flask import Flask

app = Flask(__name__)

from .views.users import users
app.register_blueprint(users, url_prefix='/users')

@app.route('/')
def hello_world():
  return 'Hello, World!'
