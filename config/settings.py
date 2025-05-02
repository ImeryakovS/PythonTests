import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, 'data')

USERS_PATH = os.path.join(DATA_DIR, 'users.json')
DASHBOARDS_PATH = os.path.join(DATA_DIR, 'dashboards.json')
USERS_TEMPLATE_PATH = os.path.join(DATA_DIR, 'users.template.json')
DASHBOARDS_TEMPLATE_PATH = os.path.join(DATA_DIR, 'dashboards.template.json')

BASE_URL = 'http://localhost:3000'
BASIC_AUTH = ("admin","admin")
LOW_ACCESS = ("LowAccess","test")
