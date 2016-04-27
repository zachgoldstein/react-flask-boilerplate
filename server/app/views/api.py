from flask import Blueprint, render_template

api = Blueprint('api', __name__)


@api.route('/get')
def site():
  return render_template('index.jinja2')