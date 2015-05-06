from flask import Flask, render_template
from flask_wtf.csrf import CsrfProtect
from flask import request
import config
from samstatisticapp.blueprints import proxy
from raven.contrib.flask import Sentry

# WTFORMS CSRF.
csrf = CsrfProtect()

# Init Flask.
app = Flask(__name__, static_folder=config.STATIC_FOLDER_DEV, static_url_path='/static')

# Init CSRF for ITTECH API Safety
csrf.init_app(app)

# Create config from config object.
app.config.from_object('config')

# Initialize Sentry
sentry = Sentry(app)

# Register proxy module - NOTE: CORS should not be allowed to star to avoid access from other sources
app.register_blueprint(proxy.mod)
