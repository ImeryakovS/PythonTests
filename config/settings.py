import os

BASE_DIR = os.environ.get("GITHUB_WORKSPACE", os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

DATA_DIR = os.path.join(BASE_DIR, 'data')

# If GRAFANA_DB_PATH == true then use this variable
DB_PATH = os.environ.get("GRAFANA_DB_PATH")

if not DB_PATH:
    # if not - local path on Windows
    TESTS_ROOT = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.abspath(
        os.path.join(TESTS_ROOT, '..', '..', 'Mygrafana', 'Mygrafana', 'data', 'grafana.db')
    )

USERS_PATH = os.path.join(DATA_DIR, 'users.json')
DASHBOARDS_PATH = os.path.join(DATA_DIR, 'dashboards.json')
ORGANIZATIONS_PATH = os.path.join(DATA_DIR, 'organizations.json')

USERS_TEMPLATE_PATH = os.path.join(DATA_DIR, 'users.template.json')
DASHBOARDS_TEMPLATE_PATH = os.path.join(DATA_DIR, 'dashboards.template.json')
ORGANIZATIONS_TEMPLATE_PATH = os.path.join(DATA_DIR, 'organizations.template.json')

BASE_URL = os.getenv("GRAFANA_BASE_URL", "http://localhost:3000")
BASIC_AUTH = ("admin","admin")
LOW_ACCESS = ("LowAccess","test")


