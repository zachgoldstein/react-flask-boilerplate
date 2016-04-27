from os.path import join, abspath
from datetime import timedelta

SERVER_ROOT = abspath(join(abspath(__file__), "../../"))
APP_ROOT = abspath(join(SERVER_ROOT, '../'))
CLIENT_ROOT = join(APP_ROOT, 'client/')

WEBPACK_MANIFEST_PATH = join(SERVER_ROOT, 'static/assets/manifest.json')

MONGODB_DB = 'app'
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

JWT_AUTH_URL_RULE = "/api/users/auth"
JWT_EXPIRATION_DELTA = timedelta(hours=1)

DEBUG_TB_PANELS = ['flask.ext.mongoengine.panels.MongoDebugPanel',
                   'flask_debugtoolbar.panels.versions.VersionDebugPanel',
                   'flask_debugtoolbar.panels.timer.TimerDebugPanel',
                   'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
                   'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
                   'flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel',
                   'flask_debugtoolbar.panels.template.TemplateDebugPanel',
                   'flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel',
                   'flask_debugtoolbar.panels.logger.LoggingPanel',
                   'flask_debugtoolbar.panels.route_list.RouteListDebugPanel',
                   'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel']
