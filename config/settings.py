import os

BASE_DIR = os.environ.get("GITHUB_WORKSPACE", os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

DATA_DIR = os.path.join(BASE_DIR, 'data')

USERS_PATH = os.path.join(DATA_DIR, 'users.json')
DASHBOARDS_PATH = os.path.join(DATA_DIR, 'dashboards.json')
ORGANIZATIONS_PATH = os.path.join(DATA_DIR, 'organizations.json')

USERS_TEMPLATE_PATH = os.path.join(DATA_DIR, 'users.template.json')
DASHBOARDS_TEMPLATE_PATH = os.path.join(DATA_DIR, 'dashboards.template.json')
ORGANIZATIONS_TEMPLATE_PATH = os.path.join(DATA_DIR, 'organizations.template.json')

BASE_URL = 'http://localhost:3000'
BASIC_AUTH = ("admin","admin")
LOW_ACCESS = ("LowAccess","test")
