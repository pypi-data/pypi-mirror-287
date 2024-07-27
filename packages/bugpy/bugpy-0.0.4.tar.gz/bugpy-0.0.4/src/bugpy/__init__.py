from .db_manager import Connection
import os
import toml

def get_version():
    with open(os.path.join(os.path.dirname(__file__), 'pyproject.toml'), 'r') as f:
        pyproject_data = toml.load(f)
    return pyproject_data['project']['version']

__version__ = get_version()

print(f"Loaded bugpy version v{__version__}")