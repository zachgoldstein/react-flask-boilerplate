from flask import Blueprint, render_template

front_end = Blueprint('front_end', __name__)


@front_end.route('/')
def site():
  return render_template('index.jinja2')

