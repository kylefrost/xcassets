PROJECT_DIR = '/var/www/xcassets'
activate_this = '/var/www/xcassets/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os, sys
sys.path.insert(0, '/var/www/xcassets')
sys.stdout = sys.stderr
from xcassets import app as application
