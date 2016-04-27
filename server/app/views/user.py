from flask import Blueprint, jsonify, request, make_response, current_app
from flask_jwt import jwt_required, current_identity

from app.security import encrypt_password, has_role
from app.models import User, Role

user = Blueprint('api-user', __name__)


@user.route('/test_admin')
@jwt_required()
@has_role(['Admin'])
def test_role():
  # Do some stuff
  print "ADMIN - Current identity %s" % current_identity.to_json()
  return jsonify(message="Hello world")


@user.route('/me', methods=['GET'])
@jwt_required()
def current_user():
  return current_app.response_class(current_identity.to_json(),
                                    mimetype='application/json'), 200


@user.route('/<user_id>', methods=['GET'])
@jwt_required()
@has_role(['Admin', 'Manager'])
def get(user_id):
  try:
    curr_user = User.objects.get(id=user_id)
  except:
    return jsonify(message="Not Found"), 404
  if curr_user:
    return current_app.response_class(curr_user.to_json(),
                                      mimetype='application/json'), 200
  return jsonify(message="Not Found"), 404


@user.route('/<user_id>', methods=['DELETE'])
@jwt_required()
@has_role(['Admin'])
def delete(user_id):
  return {'task': 'Say "Hello, World!"'}

# Update a user.
@user.route('/<user_id>', methods=['PUT'])
@jwt_required()
@has_role(['Admin', 'Manager'])
def put(user_id):
  return {'task': 'Say "Hello, World!"'}

# Partially update a user.
@user.route('/<user_id>', methods=['PATCH'])
@jwt_required()
@has_role(['Admin', 'Manager', 'Patch'])
def patch(user_id):
  return {'task': 'Say "Hello, World!"'}

# Get a list of users
@user.route('/', methods=['GET'])
@jwt_required()
@has_role(['Admin', 'Manager'])
def get_all():
  return {'task': 'Say "Hello, World!"'}

# Note POST is not idempotent, as we need to find an ID for the new user
# Create a user
@user.route('/', methods=['POST'])
@jwt_required()
@has_role(['Admin', 'Manager'])
def post():
  if 'username' not in request.json or 'password' not in request.json:
    return jsonify(message="Not Authorised"), 404
  default_role = Role.objects(name="User").get()
  created_user = User(username=request.json['username'],
                      password=encrypt_password(request.json['password']),
                      roles=[default_role]).save()
  print "Created user! %s:" % created_user
  response = make_response(jsonify(message='Created User'), 201)
  response.headers['location'] = '/users/' + str(created_user.id)
  return response

