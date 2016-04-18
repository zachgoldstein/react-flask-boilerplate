from flask import Blueprint, render_template

pages = Blueprint('pages', __name__)


@pages.route('/<pages_url_slug>')
def landing(pages_url_slug):
  # Do some stuff
  # return render_template('user/dashboard.html')
  return "LANDING... Hello world"