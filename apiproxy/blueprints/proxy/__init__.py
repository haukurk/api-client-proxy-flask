__author__ = 'haukurk'

from flask import Blueprint
from .proxy import apicall

mod = Blueprint('proxy', __name__, url_prefix='/proxy')

apicall.provide_automatic_options = False
apicall.methods = ['GET', 'OPTIONS', 'POST']
mod.add_url_rule('/<path:path>','apicall',apicall)