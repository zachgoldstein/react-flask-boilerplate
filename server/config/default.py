from os.path import join, abspath

SERVER_ROOT = abspath(join(abspath(__file__), "../../"))
APP_ROOT = abspath(join(SERVER_ROOT, '../'))
CLIENT_ROOT = join(APP_ROOT, 'client/')

WEBPACK_MANIFEST_PATH = join(SERVER_ROOT, 'static/assets/manifest.json')