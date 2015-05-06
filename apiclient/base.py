'''
Originally forked from https://github.com/shazow/apiclient MIT 2014
License: MIT

Haukur Kristinsson 2014
Licence: MIT
'''

import json

from urllib3 import connection_from_url
from urllib import urlencode


class APIClient(object):
    BASE_URL = 'http://localhost:5000/'

    def __init__(self, rate_limit_lock=None):
        self.rate_limit_lock = rate_limit_lock
        self.connection_pool = self._make_connection_pool(self.BASE_URL)

    def _make_connection_pool(self, url):
        return connection_from_url(url)

    def _compose_url(self, path, params=None):
        return self.BASE_URL + path + '?' + urlencode(params)

    def _handle_response(self, response):
        return json.loads(response.data)

    def _request(self, method, path, params=None, form_fields=None):
        url = self._compose_url(path, params)
        self.rate_limit_lock and self.rate_limit_lock.acquire()
        req = self.connection_pool.request(method.upper(), url, form_fields)

        return self._handle_response(req)

    def call(self, path, **params):
        return self._request('GET', path, params=params)

    def post(self, path, fields=None, **params):
        return self._request('POST', path, params=params, form_fields=fields)


class APIClient_SharedSecret(APIClient):
    API_KEY_PARAM = 'key'

    def __init__(self, api_key, *args, **kw):
        super(APIClient_SharedSecret, self).__init__(*args, **kw)
        self.api_key = api_key

    def _compose_url(self, path, params=None):
        # TODO: fix this, as per our conversation at Oct. 4, 2011, 05:10 UTC
        p = {self.API_KEY_PARAM: self.api_key}

        if params:
            p.update(params)

        return self.BASE_URL + path + '?' + urlencode(p)