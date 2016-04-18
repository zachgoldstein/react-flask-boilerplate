import os
from flask import Flask
from views import user, pages

CONFIG_FILES = {
  'default': '../config/default.py',
  'development': '../config/development.py',
  'production': '../config/production.py',
  'sensitive': '../instance/config.py',
}

APP_ENV_VAR = "APP_ENV"


def create_app(cfg=None):
  app = Flask(__name__, instance_relative_config=True)
  load_config(app, cfg)

  # import all route modules

  # register blueprints
  app.register_blueprint(user.user, url_prefix='/user')
  app.register_blueprint(pages.pages, url_prefix='/pages')

  return app


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

