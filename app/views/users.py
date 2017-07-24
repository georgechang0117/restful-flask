from ..models.user import User
import flask
from flask import Blueprint, request, Response, jsonify, render_template, abort, redirect, url_for
from functools import wraps
from jinja2 import TemplateNotFound
from .. import db

users = Blueprint('users', __name__, template_folder='templates')

def check_auth(username, password):
  return username == 'robin' and password == 'ischarming'
  
def authenticate():
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


@users.errorhandler(404)
def page_not_found():
  return abort(404)

@users.route('/', methods=['GET'])
@requires_auth
def index():
  users = User.query.all()
  return render_template('users/index.html', users = users)

@users.route('/new', methods=['GET'])
def new():
  user = User()
  return render_template('users/new.html', users = user)

@users.route('/create', methods=['POST'])
def create():
  username = request.form['username']
  email = request.form['email']
  user = User(username, email)
  db.session.add(user)
  db.session.commit()
  return redirect(url_for('users.index'))

@users.route('/<int:id>', methods=['GET'])
def show(id):
  try:
    user = User.query.filter_by(id=id).first()
    return render_template('users/show.html', user = user)
  except TemplateNotFound:
    abort(404)

@users.route('/<int:id>/edit', methods=['GET'])
def edit(id):
  try:
    user = User.query.filter_by(id=id).first()
    return render_template('users/edit.html', user = user)
  except TemplateNotFound:
    abort(404)

@users.route('/<int:id>', methods=['POST'])
def update(id):
  user = User.query.filter_by(id=id).first()
  email = request.form['email']
  user.email = email
  return redirect(url_for('users.index'))

@users.route('/<int:id>/delete', methods=['POST'])
def destroy(id):
  user = User.query.filter_by(id=id).first()
  db.session.delete(user)
  db.session.commit()
  return redirect(url_for('users.index'))