activate_this  = '/var/www/apiproxy/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
import sys
sys.path.append("/var/www/apiproxy/app")
from apiproxy import app as application