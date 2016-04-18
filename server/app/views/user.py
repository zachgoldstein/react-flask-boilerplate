from flask import Blueprint, render_template

user = Blueprint('user', __name__)


@user.route('/<user_url_slug>')
def dashboard(user_url_slug):
  # Do some stuff
  # return render_template('user/dashboard.html')
  return "Hello world"
