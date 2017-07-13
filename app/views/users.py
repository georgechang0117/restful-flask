from flask import Blueprint, request, jsonify

users = Blueprint('users', __name__, template_folder='templates')

@users.errorhandler(404)
def page_not_found():
  msg = {
    'url': request.url,
    'status': 404
  }
  return jsonify(msg), 404

user_list = {
  1: { "name": "Robin", "email": "robin@gmail.com" },
  2: { "name": "george", "email": "george@gmail.com"},
}

@users.route('/', methods=['GET'])
def index():
  return jsonify(user_list), 201

@users.route('/', methods=['POST'])
def create():
  if len(user_list) > 0:
    last_key = user_list.keys()[-1]
    key = last_key + 1
  else:
    key = 1
  name = request.form["name"]
  email = request.form["email"]
  user_list[key] = {"name": name, "email": email}
  return jsonify(user_list), 201


@users.route('/<int:id>', methods=['GET'])
def get(id):
  if id in user_list:
    user = user_list[id]
    return jsonify(user), 201
  else:
    return page_not_found()

@users.route('/<int:id>', methods=['PUT'])
def put(id):
  if id in user_list:
    if "name" in request.form:
      user_list[id]["name"] = request.form["name"]
    if "email" in request.form:
      user_list[id]["email"] = request.form["email"]
    return jsonify(user_list[id]), 201
  else:
    return page_not_found()

@users.route('/<int:id>', methods=['DELETE'])
def destroy(id):
  if id in user_list:
    user_list.pop(id, None)
    return jsonify(user_list), 201
  else:
    return page_not_found()