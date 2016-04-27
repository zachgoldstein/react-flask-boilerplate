import os
from flask import Flask

CONFIG_FILES = {'default': '../config/default.py',
                'development': '../config/development.py',
                'production': '../config/production.py',
                'sensitive': '../instance/config.py',
                }

APP_ENV_VAR = "APP_ENV"


def create_app(cfg=None, debug=False):
  app = Flask(__name__, instance_relative_config=True, static_folder="../static")
  load_config(app, cfg)
  app.debug = debug

  register_extensions(app)

  register_debug_extensions(app)

  # import all route modules

  # register api blueprints

  # register react site blueprint
  from views.user import user
  app.register_blueprint(user, url_prefix='/api/users')
  from views.site import front_end
  app.register_blueprint(front_end, url_prefix='/')

  print "WEBPACK_MANIFEST_PATH:", app.config['WEBPACK_MANIFEST_PATH']
  print "CLIENT_ROOT", app.config['CLIENT_ROOT']

  print "APP ROUTE MAP: %s" % app.url_map

  return app


def register_extensions(app):
  from flask_webpack import Webpack
  webpack = Webpack()
  webpack.init_app(app)

  from security import authenticate, identity, jwt_error_handler, jwt_payload_callback
  from flask_jwt import JWT
  jwt = JWT(app, authentication_handler=authenticate, identity_handler=identity)
  jwt.jwt_error_callback = jwt_error_handler
  jwt.jwt_payload_callback = jwt_payload_callback

  from models import db
  db.init_app(app)

  print "app.debug %s" % app.debug
  print "app.config['SECRET_KEY'] %s" % app.config['SECRET_KEY']


def register_debug_extensions(app):
  from flask_debugtoolbar import DebugToolbarExtension
  toolbar = DebugToolbarExtension()
  toolbar.init_app(app)

  from flask_admin.contrib.mongoengine import ModelView
  import flask_admin as admin
  admin = admin.Admin(app, 'TimeTracker:Admin')

  # Add views
  from models import User, Role
  admin.add_view(ModelView(User))
  admin.add_view(ModelView(Role))


def load_config(app, cfg=None, env=None):
  # Load a default configuration file
  app.config.from_pyfile(CONFIG_FILES['default'])

  # If we're passing in a config, use that
  if cfg is not None:
    app.config.from_pyfile(cfg)
    return

  # Look in the env vars for which environment to use
  if env is None and APP_ENV_VAR in os.environ:
    env = os.environ[APP_ENV_VAR]

  if env in CONFIG_FILES:
    app.config.from_pyfile(CONFIG_FILES[env])

  # Now the sensitive data
  app.config.from_pyfile('sensitive.py')
