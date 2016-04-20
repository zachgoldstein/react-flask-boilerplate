from flask import Blueprint

user = Blueprint('user', __name__)


# CRUD methods here...

@user.route('/<user_url_slug>')
def dashboard(user_url_slug):
  # Do some stuff
  return "Hello world"
