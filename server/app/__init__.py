import os
from flask import Flask
from flask_webpack import Webpack

CONFIG_FILES = {'default': '../config/default.py',
                'development': '../config/development.py',
                'production': '../config/production.py',
                'sensitive': '../instance/config.py',
                }

APP_ENV_VAR = "APP_ENV"


def create_app(cfg=None):
  app = Flask(__name__, instance_relative_config=True, static_folder="../static")
  load_config(app, cfg)

  # import all route modules

  # register api blueprints

  # register react site blueprint
  from views.user import user
  app.register_blueprint(user, url_prefix='/user')
  from views.site import front_end
  app.register_blueprint(front_end, url_prefix='/')

  print "WEBPACK_MANIFEST_PATH:",app.config['WEBPACK_MANIFEST_PATH']
  print "CLIENT_ROOT", app.config['CLIENT_ROOT']

  register_extensions(app)

  return app


def register_extensions(app):

  # setup webpack
  webpack = Webpack()
  webpack.init_app(app)


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

