from models import User
from flask_jwt import current_identity
from flask import jsonify, current_app
from functools import wraps
from werkzeug.security import safe_str_cmp
from datetime import datetime
import bcrypt

from flask_admin.contrib.mongoengine import ModelView
from flask_jwt import jwt_required, current_identity


def authenticate(username, password):
  """
  Flask-JWT handler to check a user's username/password
  TODO: use bcrypt encoding here

  Args:
    username:
    password:

  Returns:

  """
  print "authenticating"
  user = User.objects(username=username).first()
  print "user %s" % user
  if user and compare_password(user.password, password):
    print "authenticated??"
    return user


def jwt_payload_callback(identity):
  iat = datetime.utcnow()
  exp = iat + current_app.config.get('JWT_EXPIRATION_DELTA')
  nbf = iat + current_app.config.get('JWT_NOT_BEFORE_DELTA')
  return {'exp': exp, 'iat': iat, 'nbf': nbf, 'identity': str(identity.id)}


def identity(payload):
  """
  Flask-JWT handler to determine the current user
  A auth token in the header gets decoded by Flask-JWT to get this payload with the user id

  Args:
    payload:

  Returns:

  """
  user_id = payload['identity']
  return User.objects(id=user_id).first()


def has_role(role_names):
  """
  This decorator lets us make sure that a user has one of the roles in a list
  Make sure the current authenticated user has a certain role
  """
  def has_role_decorator(func):
    @wraps(func)
    def func_wrapper(*args, **kwargs):
      for role_name in role_names:
        if current_identity.has_role(role_name):
          return func(*args, **kwargs)
      response = jsonify(message="Not Authorised")
      response.status_code = 403
      return response
    return func_wrapper
  return has_role_decorator


def jwt_error_handler(error):
  print "An error occurred during JWT processing: %s" % error
  response = jsonify(message="Not Authorised")
  response.status_code = 401
  return response


def encrypt_password(password):
  return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12))


def compare_password(hashed_password, password):
  if safe_str_cmp(bcrypt.hashpw(password.encode('utf-8'), hashed_password.encode('utf-8')), hashed_password):
    print "It matches"
    return True
  else:
    print "It does not match"
    return False
